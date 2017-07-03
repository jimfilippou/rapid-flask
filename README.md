# flask-starter-boilerplate

I had trouble figuring out complex flask setups so i made this starter-friendly boilerplate to get your project up and running with ease by implementing maintainability and clean code principles. It includes custom logins and registers as well as response minification and modular blueprinted controllers.

## Setting it up

First after cloning the repo create a virtual environment

`virtualenv env`

Then Activate that environment

`.\env\Scripts\activate`

Install dependencies

`pip install -r requirements.txt`

Initialize database

`python manage.py db init`

Run the app

`python manage.py runserver`

## Project structure
```
    app
    ├───blueprints
    │   ├───authentication
    │   └───tools
    ├───static
    │   ├───css
    │   ├───img
    │   └───js
    │       
    └───templates
