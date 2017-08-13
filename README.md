 
![alt text](http://i.imgur.com/KMrM6YZ.png "Phyal -> python Phial")

# rapid-flask

[![Build Status](https://travis-ci.org/jimfilippou/rapid-flask.svg?branch=master)](https://travis-ci.org/jimfilippou/rapid-flask)

A boilerplate for **Flask** applications, as simple as possible

I made this starter-friendly boilerplate to get your project up and running with ease by implementing maintainability and clean code principles. 
 

# Setting it up

Clone the repository with this command 

`git clone https://github.com/jimfilippou/flask-boilerplate.git`

Cool now after you have cloned the repo lets create a __virtualenv__. Simply use the following line and if you see that it's missing just do this `pip install virtualenv`

`virtualenv env`

Then Activate that environment (Windows)

`.\env\Scripts\activate`

Install dependencies

`pip install -r requirements.txt`

Initialize database

`python manage.py db init`

Run the app

`python manage.py runserver`

Run the app within network  

`python manage.py runserver --host 0.0.0.0`

# Testing

`nosetests`

## Additional commands

You might have noticed inside manage.py i added a 'runlinter' and a 'runcleaner' command.
Basically runlinter lints the code to maintain a clean and maintainable code, i have added custom configuration for interactive and detailed reports.

To lint the app module

`pylint app`

The runcleaner command is a bit special and **opinionated**. During development i like to have things organized, and compiled python files do not help. I am using Visual studio code and when i run the server i get filled with .pyc files all over the place and that kinda makes me mad. So i made the `python manage.py runcleaner` command to clear the place from .pyc files. BUT in order for it to work change line 28 with your OWN path! otherwise it will not work.

To clean directory

`python manage.py runcleaner`

# What can i do?

The app is splitted into modules, the main module s **app** .
+ You can import blueprints to init.py with just 2 lines, 
+ You can clean up your code with linters
+ You can run tests with no setup
+ You can use some prebuilt tools and buids some others yourself
+ You can contribute to this repo, i don't bite
