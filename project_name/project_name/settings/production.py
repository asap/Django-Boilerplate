from .base import *

DEBUG = TEMPLATE_DEBUG = False

INSTALLED_APPS += [
	'gunicorn',
]
