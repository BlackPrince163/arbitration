# Инструкция по запуску
1. `python3 -m venv venv` - инициализация виртуального окружения
2. `source venv/bin/activate` - вход в виртуальное окружение
3. `pip install -r requirements.txt` - установка зависимостей
4. `docker-compose up -d ` - поднятие базы данных (если установлен Docker)
5. `python manage.py migrate` - запуск миграций
6. `python manage.py runserver` - запуск приложения
