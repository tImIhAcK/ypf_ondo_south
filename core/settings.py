import os
from pathlib import Path
from django.urls import reverse_lazy
from dotenv import load_dotenv
import dj_database_url
# import django_heroku
# django_heroku.settings(locals())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-wtns8-+#(fked)61!ke@n8s&2@@$)0@4%ayfnkbc#y1#wf4=xs'
SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production
DEBUG = os.getenv('DEBUG')
# DEBUG = True

USE_L10N = False
USE_TZ = False

ALLOWED_HOST = []
ALLOWED_HOSTS = ['ypfonline.up.railway.app', '127.0.0.1']

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_TRUSTED_ORIGIN = ['https://ypfonline.up.railway.app', 'http://ypfonline.up.railway.app']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    # "crispy_bootstrap5",
    "crispy_forms",
    'phonenumber_field',
    'smart_selects',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   
    'home',
    'custom_admin'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#database
DATABASE_URL = os.getenv('DATABASE_URL')
DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),

}



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATIC_ROOT =os.path.join(BASE_DIR, 'staticfiles')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = reverse_lazy('admin:login')
LOGIN_REDIRECT_URL = reverse_lazy('admin:index')



# JAZZMIN SETINGS
JAZZMIN_SETTINGS = {
    "site_title": "YPF ONDO SOUTH DASHBOARD", 
    "site_logo": "images/logo 1.png",
    "site_header": "YPF ONDO SOUTH",
    "site_brand": "",
    "welcome_sign": "YPF ONDO SOUTH DASHBOARD",
    "search_model": "custom_admin.Participant",
    "site_logo_classes":None,
    "footer_fixed": True,
    "sidebar_fixed": True,
    
    "custom_css": 'css/custom_admin.css',
    "custom_js": 'js/custom_admin.js',
}

# JAZZMIN_UI_TWEAKS = {
#     "theme": "darkly",
# }

# Cripsy Settings
# CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
# CORS_ORIGIN_ALLOW_ALL = True


CRISPY_TEMPLATE_PACK = "bootstrap4"