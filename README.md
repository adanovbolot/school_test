docker на минимальных требованиях

    
    база данные для docker    
    
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'root',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'db',
        'PORT': '5432',
    }
}

две команды для запуска

    docker-compose build
    docker-compose up
    or
    docker-compose up -d

стоп    
    
    docker-compose stop
    

создайте виртуальное окружение

    python -m venv env
    

    примечание: если не работает .env файл
    переместите его в main/.env

    либо проверить нет ли между данными пробелы

все зависимости хранятся в папке 

requirements.txt

    Django==4.0.6
    django-environ==0.9.0
    django-phonenumber-field==6.3.0
    phonenumbers==8.12.52
    Pillow==9.2.0
    psycopg2-binary==2.9.3


для установки зависимостей

    pip install -r requirements.txt

создать .env файл, создать свои скрытые данные для проектa

    все поля которые нужно заполнить

    SECRET_KEY = env("SECRET_KEY")
    
    DEBUG = env('DEBUG')
    
    ALLOWED_HOSTS = ['*']
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env("DATABASE_NAME"),
            'USER': env("DATABASE_USER"),
            'PASSWORD': env("DATABASE_PASSWORD"),
            'HOST': env("DATABASE_HOST"),
            'PORT': env("DATABASE_PORT"),
        }
    }
    
        
    DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
    EMAIL_BACKEND = env('EMAIL_BACKEND')
    EMAIL_HOST = env('EMAIL_HOST')
    EMAIL_PORT = env('EMAIL_PORT')
    EMAIL_USE_TLS = env('EMAIL_USE_TLS')
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')


создать базу данных postgresql
    
    для учебного проекта можно использовать по умолчанию
    
    CREATE DATABASE myproject;
    
    CREATE USER myprojectuser WITH PASSWORD 'password';

    ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
    ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE myprojectuser SET timezone TO 'UTC';
    
    GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

    
    подключите все данные для database.
    
запуск миграции
    
    python manage.py migrate


    python manage.py makemigrations school
    
    python manage.py makemigrations users

создайте хозяина дома

собрать все статически файлы

    python manage.py collectstatic

создайте хозяина дома

    python manage.py createsuperuser


запуск проекта
    
    python manage.py runserver
по требованию не нужен front, поэтому я взял внутренний css(base.css)
главное backend рабочий

для меня это был первый опыт по, templates

    спасибо большое, за такой тест_проект

По frontend требований никаких не предъявляется. Интерфейс на ваше усмотрение и он не будет оцениваться


как работает проект?

проект работает на минималках

очень простая

0) регистрация
   1) добавьте ваши данные ('http://127.0.0.1:8000/')
   2) создайте студентов ('http://127.0.0.1:8000/school/add-student/')
    
       при отправке формы, на email, по новому закону:
       ''Чтобы обеспечить безопасность вашего аккаунта, с 30 мая 2022 года Google больше не поддерживает использование сторонних приложений или устройств, которые просят вас войти в аккаунт Google, используя только имя пользователя и пароль.'''
    

    мне помогла это статья: https://django.fun/qa/418975/


4) создайте класс ('http://127.0.0.1:8000/school/class_choice/')
4) Добавить новую школу ('http://127.0.0.1:8000/school/add-school/')

    конец!!!


**так получилось, что в нашей компании нельзя, заниматься другими проектами**
**мне пришлось, в день сидеть только по 2 часа**

спасибо за понимание 
всего хорошего

буду ждать ответ./Болот