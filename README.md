# rapid-flask

<div align="center">

![alt text](http://frozenvortex.com/rapid-flask/rapid.png "vscoderocks")



[![Build Status](https://travis-ci.org/jimfilippou/rapid-flask.svg?branch=master)](https://travis-ci.org/jimfilippou/rapid-flask)
[![Dependency Status](https://gemnasium.com/badges/github.com/jimfilippou/rapid-flask.svg)](https://gemnasium.com/github.com/jimfilippou/rapid-flask)

</div>

A boilerplate for **Flask** applications, as minimal as possible

This starter-friendly boilerplate's aim is to get your project up and running with ease by implementing maintainability and clean code principles. 


# Setting it up, is dead simple

Clone the repository 

`git clone https://github.com/jimfilippou/rapid-flask.git`

Cool, now after you have cloned the repo lets create a __virtualenv__. Simply use the following line and if you see that it's missing just do this `pip install virtualenv`

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

# Debugging in vscode

There is a folder .vscode in this project, so you only go straight to debugging. No configurations needed, just go to the debug toolbar and run the debugger. 

# Testing

`nosetests`


# What can i do?

The app is splitted into modules, the main module is **app** .
+ You can import blueprints easily 
+ You can run tests with no setup
+ You can use some prebuilt tools and buids some others yourself
+ You can contribute to this repo, i don't bite
