# flask-boilerplate   [![Build Status](https://travis-ci.org/jimfilippou/flask-starter-boilerplate.svg?branch=master)](https://travis-ci.org/jimfilippou/flask-starter-boilerplate)


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

## Testing

`nosetests`

## Additional commands

You might have noticed inside manage.py i added a 'runlinter' and a 'runcleaner' command.
Basically runlinter lints the code to maintain a clean and maintainable code, i have added custom configuration for interactive and detailed reports.

To lint the app module

`pylint app`

The runcleaner command is a bit special and opinionated. During development i like to have things organized, and compiled python files do not help. I am using Visual studio code and when i run the server i get filled with .pyc files all over the place and that kinda makes me mad. So i made the `python manage.py runcleaner` command to clear the place from .pyc files. BUT in order for it to work change line 28 with your OWN path! otherwise it will not work.

To clean directory

`python manage.py runcleaner`