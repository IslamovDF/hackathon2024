# Проект для конкурса разработчиков Хантатон 2024
## Сиcтема для управления заявками в службу поддержки
## Используемые источники:
https://docs.djangoproject.com/en/5.1/intro/tutorial01/
https://habr.com/ru/articles/234307/

## Используемые версии
Django==5.1.3
Python==3.11.9

# Установка
```commandline
python -m pip install Django
mkdir helpdeck_project
django-admin startproject helpdesk helpdeck_project
```

# Запуск сервера (разработки)
перед запуском переходим в папку helpdeck_project (далее везде где работаем с manage.py)
```commandline
cd helpdeck_project 
python manage.py runserver
```

# Создание пакета Django tasks
```commandline
python manage.py startapp tasks
```

# Создаем файл для роутинга
```commandline
tasks/urls.py
```

# Правим основной файл роутинга
```commandline
helpdesk/urls.py
```

# Проводим миграцию
```commandline
python manage.py migrate
```

# Создаем модели
./tasks/models.py

# Миграция новой модели
```commandline
python manage.py makemigrations tasks
python manage.py sqlmigrate tasks 0001 вывод в консоль содержимго миграции
python manage.py migrate
```

# Создание суперпользователя
```commandline
python manage.py createsuperuser
```

# Полезные заметки
- выход из консоли Django Ctrl + Z и Enter
- Часовой пояс устанавливается в settings.py: TIME_ZONE = 'Asia/Yekaterinburg'

# Добавляем разработанный пакет tasks в админ панель
./tasks/admin.py


