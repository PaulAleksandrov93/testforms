#!/bin/bash

# Тестовые данные для POST-запроса
data1='{"f_name1": "test@example.com", "f_name2": "+7 123 456 78 90"}'
data2='{"f_name1": "invalid_email", "f_name2": "1234567890"}'

# POST-запрос с корректными данными
echo "Testing with valid data:"
curl -X POST "http://localhost:8000/get_form" -H "accept: application/json" -H "Content-Type: application/json" -d "$data1"
echo -e "\n"

# POST-запрос с некорректными данными
echo "Testing with invalid data:"
curl -X POST "http://localhost:8000/get_form" -H "accept: application/json" -H "Content-Type: application/json" -d "$data2"
echo -e "\n"