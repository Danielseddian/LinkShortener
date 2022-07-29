## LinkShortener service for make short links from long ones (demo)
### Base for service to short links

# Сервис для создания сокращенных ссылок (демо)
## По запросу пользователя создает короткую ссылку из длинной, которая будет действовать определенное время.
#### Токи доступа:
- /api/v1/short_link/ # [POST] - создает которую ссылку и возвращает ее пользователю
- /<str:short>/ # [GET] - перенаправляет пользователя по короткой ссылке на внешний ресурс и сохраняет информацию о пользователе (IP-адрес, устройство, дата перехода)
#### Стек библиотек:
- Django==4.0.6
- python-dotenv==0.20.0
- python-environ==0.4.54
- django-bulk-update-or-create==0.3.0
- djangorestframework==3.13.1

## Подготовка к запуску:
#### 1. Создать файл .env в папке source и добавить пары ключ=значение по примеру из .env.example
#### 2. Выполнить команды через консоль:
> python3 -m venv venv # (venv). название виртуального окружаения, обычно, venv

> . venv/bin/activate # для Windows: venv/Scripts/activate

> pip install -r requirements.txt 
## Запуск сервера:
> python manage.py migrate --run-syncdb  # создание и разметка БД

> python manage.py createsuperuser # создание суперпользователя (для открытия Админки и просмтотра статистики)

> python manage.py runserver # запуск сервера (по умолчанию: http://127.0.0.1:8000/)
