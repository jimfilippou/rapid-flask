"""
This module makes the app runnable with a single command

Available commands:
> python manage.py runserver
> python manage.py runcleaner
> python manage.py runlinter

"""
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager as Manager_Rugby

from pylint.lint import Run as lint_module

from app import app, db

from clean import clean

migrate = Migrate(app, db)
manager = Manager_Rugby(app)

manager.add_command('db', MigrateCommand)

@manager.command
def runcleaner():
    clean()

@manager.command
def runlinter():
    lint_module(['app'])


if __name__ == '__main__':
    manager.run()
