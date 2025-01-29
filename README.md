# Курсовой проект №5

<i>Это DRF-проект трекера полезных привычек Habit Tracker</i>

## Описание проекта

## Установка:

1. Клонируйте репозиторий:

```
https://github.com/AlexandrPavlushenko/HabitTracker.git
```

2. Установите зависимости:

```
poetry install
```

3. Создайте и заполните данными файл <b>.env</b> по шаблону <b>.env.sample</b>, который находится в корне проекта

4. Создайте и примините миграции
```
python manage.py makemigrations
python manage.py migrate
```

5. В проекте есть фикстуры для создания базы пользователей и привычек

```
   python manage.py loaddata users_fixture.json --format json
   python manage.py loaddata habits_fixture.json --format json
```
## Тесты:
Код покрыт тестами на 89%
