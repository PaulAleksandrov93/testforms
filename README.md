# FastAPI Form Recognition App

Web-приложение для определения заполненных форм с использованием FastAPI и TinyDB.

## Установка и запуск

1. Убедитесь, что у вас установлен Python 3.6 или выше.
2. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/your_username/fastapi-form-app.git
    cd fastapi-form-app
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Запустите приложение:

    ```bash
    uvicorn main:app --reload
    ```

5. Откройте другой терминал и запустите тестовый скрипт:

    ```bash
    ./test_script.sh
    ```

    Обратите внимание, что у вас может потребоваться предоставить права на выполнение скрипта:

    ```bash
    chmod +x test_script.sh
    ```

## Замечания

- Убедитесь, что порт 8000 доступен для использования.
- Вам также может потребоваться установить `curl`, если он не установлен.