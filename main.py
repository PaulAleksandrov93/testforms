from fastapi import FastAPI, Form, HTTPException
from pydantic import BaseModel
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
import re

app = FastAPI()
db = TinyDB('templates.json')

class FormData(BaseModel):
    f_name1: str
    f_name2: str

def validate_email(email):
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return bool(re.match(email_regex, email))

def validate_phone(phone):
    phone_regex = re.compile(r"\+7 \d{3} \d{3} \d{2} \d{2}")
    return bool(re.match(phone_regex, phone))

def validate_date(date):
    date_regex1 = re.compile(r"\d{2}\.\d{2}\.\d{4}")
    date_regex2 = re.compile(r"\d{4}-\d{2}-\d{2}")

    return bool(re.match(date_regex1, date)) or bool(re.match(date_regex2, date))

def save_to_database(data):
    db.insert(data)

def get_template_matching_fields(data):
    templates = db.all()
    for template in templates:
        template_fields = set(template.keys()) - {'name'}
        data_fields = set(data.keys())
        
        if template_fields.issubset(data_fields):
            match = True
            for field in template_fields:
                field_type = template[field]
                field_value = data[field]

                if field_type == 'email' and not validate_email(field_value):
                    match = False
                    break
                elif field_type == 'phone' and not validate_phone(field_value):
                    match = False
                    break
                elif field_type == 'date' and not validate_date(field_value):
                    match = False
                    break

            if match:
                save_to_database(data)  # Сохраняем данные в базу
                return template['name']

    return None

def infer_field_types(data):
    field_types = {}
    for field, value in data.items():
        if '@' in value:
            field_types[field] = 'email'
        elif value.startswith('+7'):
            field_types[field] = 'phone'
        elif '.' in value:
            field_types[field] = 'date'
        else:
            field_types[field] = 'text'
    return field_types

# Тестовые данные для инициализации базы
db.insert({
    "name": "Sample Form",
    "f_name1": "email",
    "f_name2": "phone"
})

@app.post("/get_form")
async def get_form(data: FormData):
    matching_template = get_template_matching_fields(data.dict())

    if matching_template:
        return {'template_name': matching_template}
    else:
        field_types = infer_field_types(data.dict())
        return field_types