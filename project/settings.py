# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b%q0$g8ykfgiv41&h0kg@jl*v)2=$!j4vv!ukm*dqiabrfn50z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']


# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	'tinymce',
	'sorl.thumbnail',
	'constance',
	'autofixture',	
	'debug_toolbar',

	'store',
)



MIDDLEWARE_CLASSES = (
	'debug_toolbar.middleware.DebugToolbarMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT=os.path.join(BASE_DIR,'static/')
STATICFILES_DIRS = (BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media/')

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS':[
			'templates/',
			'templatetags/',
		],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
                'constance.context_processors.config',
			],
		},
	},
]

CONSTANCE_CONFIG = {
	'HEADER_TEXT': ('', u'Заголовок в топ-меню'),
	'ADDRESS1': ('г. Люберцы,', u'Адрес(строка 1)'),
	'ADDRESS2': ('ул. Котельническая, д.4', u'Адрес(строка 2)'),

	'PHONE': ('+7(495) 778 19 99,', u'Телефон'),
	'REQUISITES': ('Инн 5027200091 / кпп 502701001 / огрн 1135027004771', u'Реквизиты'),

	'EMAIL_ADMIN': ('djmadbit@gmail', u'Email куда будут приходить заявки'),
	'EMAIL_FROM': ('djmadbit@gmail', u'Email откуда будут уходить заявки'),
	'EMAIL_PASSWORD': ('showmeyourskill', u'Пароль'),
	'EMAIL_PORT': ('587', u'Порт'),
	'EMAIL_SMTP': ('smtp.gmail.com', u'SMTP сервер'),
	
}



######################################################################
######################	 DEBUG		##############################
######################################################################
DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

try:
    from production_settings import *
except:
    pass
