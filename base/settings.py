from django.contrib.messages import constants as messages
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

AUTH_USER_MODEL='accounts.Account'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m!$b^sz*lb#naq$r_c%c&kc5sdoxyk96w#83%82m7*g&4@q893'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

AUTHENTICATION_BACKENDS = [
    'accounts.backends.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'main',
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

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'base.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



if DEBUG == False:
    
    STATIC_URL = 'static/'
    MEDIA_URL='media/'

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    }
    
    STATICFILES_DIRS=[
        os.path.join(BASE_DIR,'static'),
        os.path.join(BASE_DIR,'media')
    ]
    STATIC_ROOT=os.path.join(BASE_DIR,'static_cdn')
    
    MEDIA_ROOT=os.path.join(BASE_DIR,'media_cdn')

    INTERNAL_IPS = [
        "127.0.0.1",
    ]
    ACCOUNT_PROTOCOL ='http'
else:
    #ALLOWED_HOSTS = [''] update allowed hosts for production
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'neondb',
        'USER': 'redodevs',
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': "ep-green-mouse-30061062.us-east-2.aws.neon.tech",
        'PORT': '5432',
    }
    }

    # CLOUDINARY_STORAGE={
    #     'CLOUD_NAME': 'dnb8rethz',
    #     'API_KEY': os.environ.get('API_KEY'),
    #     'API_SECRET': os.environ.get('API_SECRET')
    # }
    
    # DEFAULT_FILE_STORAGE='cloudinary_storage.storage.MediaCloudinaryStorage'


    ACCOUNT_PROTOCOL ='https'
    STATIC_URL='https://theetawee.github.io/company_staticfiles/'
    
    
    


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_USE_TLS = True

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

LOGIN_URL= 'login'