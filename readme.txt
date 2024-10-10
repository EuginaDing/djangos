C:\Users\tinca>python --version
Python 3.10.2

C:\Users\tinca>mkdir djangos

C:\Users\tinca>cd djangos

C:\Users\tinca\djangos>python -m venv my_env

C:\Users\tinca\djangos>.\my_env\Scripts\activate

(my_env) C:\Users\tinca\djangos>pip install django
//project=hello
(my_env) C:\Users\tinca\djangos>django-admin startproject hello .

(my_env) C:\Users\tinca\djangos>python manage.py migrate

(my_env) C:\Users\tinca\djangos>python manage.py runserver

Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-C.
//app=calc, travello, account
(my_env) C:\Users\tinca\djangos>python manage.py startapp calc

(my_env) C:\Users\tinca\djangos>python manage.py startapp travello

//templates for all html files in settings.py for html temp
import os
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR,'templates')],


//static to link style...
//create folder static and copy plugin...style...js...img...
settings.py:
    STATIC_URL = "/static/"
    STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
    STATIC_ROOT=os.path.join(BASE_DIR,'assets')

#asset folder with All static by collectstatic       
(my_env) PS C:\Users\tinca\djangos> python manage.py collectstatic
//load and register static styles
#index.html
{% load static %}

//ORM to download a postgesql connector
pip install psycopg2  

INSTALLED_APPS = [
    'travello',
    'account',
    ...]

//for each app, run migration, if no table yet, run make and sql queries 
pip install Pillow #image lib //for all image processing
python manage.py makemigrations // initial Course/object table in py: 0001_initial.py
python manage.py sqlmigrate travello 0001 //generate sql queries for Course tables > 0001
python manage.py migration //to let db run sql 

python manage.py createsuperuser //can create remove update, delete

'''   dest1=Course()
    dest1.name='Study Law of Physics'
    dest1.img='img_1.jpg'
    dest1.desc='core course'
    dest1.desc_enroll=1259
    dest1.price=20
    dest1.special=True

    dest2=Course()
    dest2.name='Logo Design Course'
    dest2.img='img_2.jpg'
    dest2.desc='core course'
    dest2.desc_enroll=2164
    dest2.price=99
    dest2.special=False

    dest3=Course()
    dest3.name='JS Programming Language'
    dest3.img='img_3.jpg'
    dest3.desc='non core course'
    dest3.desc_enroll=539
    dest3.price=199
    dest3.special=False
    dests=[dest1, dest2, dest3]
'''








