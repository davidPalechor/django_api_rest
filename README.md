# Django RESTful app
Sample application built in Python 3.6/Django 2.0.6 

## Config
* `pip install -r requirements.txt`

## Run
* On root directory run on terminal `python manage.py migrate`
* Then run `python manage.py runserver`
* Go to `localhost:8000` on your browser

## Usage
* *GET* `localhost:8000/get/`
* *POST* `localhost:8000/post/` 
* *PUT* `localhost:8000/put/`
* *DELETE* `localhost:8000/delete/`

For POST and PUT methods the test data is like:
```javascript
{
  "name": "John",
  "last_name": "Doe",
  "email": "johndoe@email.com",
  "tel": "123456",
  "address": "24 Str",
  "art": "Picasso",
  "movies": "infinity war",
  "music": "rock/pop"
}
```

For DELETE method you just need email field:
```javascript
{
  "email": "johndoe@email.com"
}
```
All fields are required except 'art', 'movies' and 'music' fields.

**All methods were tested via [postman](https://www.getpostman.com/)** except GET method, which you can test in your browser typing the link described previously.
