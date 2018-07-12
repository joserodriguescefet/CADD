"""
Django settings for cadd_project project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
#from django.core.mail import send_mail

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2tv7f1**(!cqlhrt69sfi#pj0k0d!qyg#a_6j@!k1jj&hu3x5a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admindocs',     # Admin Docs
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Aplicações de terceiros
    'widget_tweaks',
    # Minhas Aplicações
    'accounts.apps.AccountsConfig',
    'cadd.apps.CaddConfig',
    'sca.apps.ScaConfig',
]

# Configurações de e-mails (não está em produção)
#EMAIL_HOST = 'smtp.sendgrid.net'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'testsite_app'
#EMAIL_HOST_PASSWORD = 'mys3cr3tp4ssw0rd'
#EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = 'TestSite Team <noreply@example.com>'
# Envio de e-mail propriamente dito (colocar em reuniões)
#send_mail('subject', 'corpo', 'email', ['receiver1@example.com', 'receiver2@example.com'])
# During development only
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cadd_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'accounts.context.context_processors',
            ],
        },
    },
]

WSGI_APPLICATION = 'cadd_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASE_ROUTERS = ['cadd_project.router.DatabaseRouter']

# Configurações de banco devem ser ajustadas para a versão de produção
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cadddb',
        'USER': 'root',
        'PASSWORD': 'root',
#        'HOST': '172.20.10.2', # celular
        'HOST': '192.168.1.4', # wifi
        'PORT': '3311',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    },

    'sca': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'scadb',
        'USER': 'root',
        'PASSWORD': 'root',
#        'HOST': '172.20.10.2', # celular
        'HOST': '192.168.1.4', # wifi
        'PORT': '3311',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_FORMAT = 'd/m/Y'

FILE_CHARSET="utf-8"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = '/accounts/login/'
