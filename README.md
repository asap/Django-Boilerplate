# CBS Local Django project template

This file should be overwritten after a new project is created.

## Installation

    $ django-admin.py startproject [name] . --template=/path/to/Django-Boilerplate -n Procfile,.gitignore,*.py

## Heroku

    $ heroku create --stack cedar --buildpack git@github.com:cbslocal/heroku-buildpack-python.git [name]

    $ heroku create --stack cedar --buildpack git@github.com:cbslocal/heroku-buildpack-python.git --remote staging [name-staging]
    $ heroku config:add DJANGO_DEBUG=True --remote staging

### Deployment

Production
    $ git push heroku master

Staging
    $ git push staging staging:master

For further reading, see [Managing Multiple Environemnts for an App](https://devcenter.heroku.com/articles/multiple-environments)
