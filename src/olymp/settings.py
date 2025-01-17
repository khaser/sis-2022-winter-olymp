import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=s2^n#we8blg(92#$sf9et%wtg!ikx2kod0(-$$3@!_(ab1s&+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ '2022.wolymp.lksh.ru', 'localhost' ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'ejudge',
    'users',
    'monitor',
    'map.apps.MapConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'olymp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'olymp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'ejudge': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ejudge',
        'USER': 'w2021-olymp',
        'PASSWORD': 'w2021-olymp',
        'HOST': '192.168.32.207',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

LOGIN_URL = '/users/login/'
LOGOUT_URL = '/users/logout/'


# Olymp project settings

PROBLEMS_STATEMENTS_DIR = os.path.join(BASE_DIR, 'statements')
if not os.path.exists(PROBLEMS_STATEMENTS_DIR):
    os.mkdir(PROBLEMS_STATEMENTS_DIR)
else:
    if not os.path.isdir(PROBLEMS_STATEMENTS_DIR):
        raise Exception('Problems statements (settings.PROBLEMS_STATEMENTS_DIR) exists but is not a directory')


EJUDGE_CONTEST_ID = 43998
EJUDGE_SERVE_CFG = os.path.join(BASE_DIR, '..', 'serve.cfg')
# EJUDGE_SERVE_CFG = '/home/judges/%06d/conf/serve.cfg' % EJUDGE_CONTEST_ID
EJUDGE_SERVE_CFG_ENCODING = 'utf-8'

CONTEST_START_TIME = datetime.datetime(2022, 12, 31, 15, 30, 0)
CONTEST_DURATION = 600

MAXIMUM_PENALTY = 0.7

TELEGRAM_BOT_TOKEN = ''
TELEGRAM_CHAT_ID = 0
