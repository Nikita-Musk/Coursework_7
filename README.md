# Coursework_7
# Полезные привычки

Приложение для отслеживания полезных привычек, позволяющее пользователям создавать, редактировать и управлять своими привычками, а также получать напоминания через Telegram.

## Описание проекта

Проект позволяет пользователям:

- Создавать и управлять полезными привычками.
- Устанавливать вознаграждения за выполнение привычек.
- Привязывать приятные привычки к полезным.
- Получать напоминания о выполнении привычек через Telegram.

Для работы с проектом необходимо.

- Клонировать репозиторий на компьютер.
- Создать зависимости: poetry install.
- Создайте и примените мигации (python manage.py makemigrations, python manage.py migrate)
- Создайте файл .env, внесите свои данные, используя образец .env.sample
- Установите Redis, запустите командой redis-server
- Для запуска проекта наберите в терминале команду python manage.py runserver
- Создать привычки можно в программе Postman.
- В терминале запустите celery worker командой: celery -A config worker -l INFO , если вы используете windows, то добавьте -P eventlet
- Во втором терминале запустите celery beat командой: celery -A config beat -l info -S django
- Зайдите в телеграм бот(GETMYID и получите ваш id)(BotFather и создайте бота) 

Запуск Docker

- Создайте привычки на сервере или описанным выше способом
- В Терминале введите команду: docker-compose up -d --build