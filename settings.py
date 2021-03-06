
# Django settings for recap-server project.

import os 
import logging

from uploads.recap_config import config

ROOT_PATH = os.path.dirname(__file__)

DEBUG = config["DJANGO_DEBUG"]
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    config["DJANGO_ADMIN"],  # ('Your Name', 'your_email@domain.com'),
)

SERVER_EMAIL = "recaplogger@gmail.com"
DEFULT_FROM_EMAIL = "recaplogger@gmail.com"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'recaplogger@gmail.com'
EMAIL_HOST_PASSWORD = config['EMAIL_HOST_PASSWORD']
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
EMAIL_TLS = True


logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(name)s: %(message)s',
    filename = ROOT_PATH + '/debug.log',
    filemode = 'a'
)


MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'          # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = config["DATABASE_NAME"]  # Or path to database file if using sqlite3.
DATABASE_USER = config["DATABASE_USER"]            # Not used with sqlite3.
DATABASE_PASSWORD = config["DATABASE_PASSWORD"]   # Not used with sqlite3.
DATABASE_HOST = ''                 # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''                 # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = config['DJANGO_SECRET_KEY']

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    ROOT_PATH + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'recap-server.uploads',
)
