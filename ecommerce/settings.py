"""
Django settings for ecommerce project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5+*j5f+=ob)t3k(k_%m$82#fh33y%yjah%^($++2vh#wsw-f4-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True




# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'django_extensions',
    'shops',
    'south',
    'django_pdb',
    'bootstrap3',
    "payments",
    'endless_pagination',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_pdb.middleware.PdbMiddleware',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR,'templates' )
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
     'django.template.loaders.eggs.Loader',
)
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)
ROOT_URLCONF = 'ecommerce.urls'

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'django-test',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '/opt/lampp/var/mysql/mysql.sock',   # Or an IP Address that your DB is hosted on
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR,'/static/')
STATIC_URL = '/static/'
STATIC_PATH = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = (
   STATIC_PATH,
)


REGISTRATION_OPEN = True                # If True, users can register
ACCOUNT_ACTIVATION_DAYS = 7     # One-week activation window; you may, of course, use a different value.
# REGISTRATION_AUTO_LOGIN = True  # If True, the user will be automatically logged in.
# LOGIN_REDIRECT_URL = '/rango/'  # The page you want users to arrive at after they successful log in
# LOGIN_URL = '/accounts/login/'  # The page users are directed to if they are not logged in,
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'hitesh.gurjar786@gmail.com'
EMAIL_HOST_PASSWORD = 'H!tesh@#$88'
EMAIL_PORT = 587
ALLOWED_HOSTS = ['localhost', '127.0.0.1','.herokuapp.com', ]
MEDIA_ROOT = '/home/yuva/Desktop/python/ecommerce/media/'
MEDIA_URL = '/media/'
STATICFILES_FINDERS = ( 
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STRIPE_SECRET_KEY = os.environ.get(
    "STRIPE_SECRET_KEY",
    "sk_test_tBcbnfnWfCmoTjN0DWCIAhi9"
)
STRIPE_PUBLIC_KEY = os.environ.get(
    "STRIPE_PUBLIC_KEY",
    "pk_test_6vtmBkrnNkTO1BguxcGsxW65"
)
# TEMPLATE_CONTEXT_PROCESSORS = [
#     "payments.context_processors.payments_settings",
#     'django.contrib.auth.context_processors.auth',
# ]
