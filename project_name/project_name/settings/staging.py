from .base import *

DEBUG = TEMPLATE_DEBUG = True

INSTALLED_APPS += [
	'gunicorn',
]
