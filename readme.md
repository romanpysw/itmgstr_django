# TestTaksLib
## Роман Сысоев
https://github.com/romanpysw

Тестовое задание Python/django

## Описание

 - Приложение testtakslib -- корневое:
     - configs.py -- файл конфигураций проекта, создает переменные окружения
- Приложение libapp -- целевое:
    -  Роут: GET /libapp/writers/<writer_id>
        Возвращает информацию о писателе и его книгах в формате JSON
    - libapp/managment/commands/init.py -- обработчик комманды "python manage.py init", которая создает в БД нужные таблицы, а также заполяет их тестовыми данными

 - requirements.txt -- Зависимости проекта

 - Используемая база данных -- PostgreSQL

 - Django ORM -- 2 класса:
    - Writer
    - Book

