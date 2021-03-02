# backend-django-restfulapi-game-suit
 **_Aplikasi game suit kertas batu gunting menggunakan django restful api framework_**

### membuat aplikasi Game RESTful API Django --

1. buat virtual environment python


    $ python -m venv myenv

   
    $ myenv\Scripts\activate.bat

install package :
   
   - django = web framework python
   
   - django rest framework = restful api
   
   - django cors header = middleware frontend

	
	$ pip install django djangorestframework django-cors-headers

create project django
   

	$ django-admin startproject myproject

run server
   

    $ python manage.py runserver

create app django

	$ python manage.py startapp games

API Endpoint , Open Postman

    Method : POST
    Url : http://127.0.0.1:8000/run/

Request : "value : rock , paper, scissor"
    
    {
        "user_choice": "rock"
    }