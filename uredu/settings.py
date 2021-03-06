"""
Django settings for uredu project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r_k)^a)=-mo3octui8*&20*#0)g=1vq7yuv*e^@7+_%kl^hrn)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

"""
Change Default User Model
"""
AUTH_USER_MODEL = 'accounts.Users'

# Application definition

INSTALLED_APPS = [
    # Jamin dùng để sửa UI của trang Admin panel
    'jazzmin',
    # Corsheaders dùng để tránh bị chặn lỗi cors ở front-end
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps create to manage
    'accounts.apps.AccountsConfig',
    'students.apps.StudentsConfig',
    'rooms.apps.RoomsConfig',
    'teachers.apps.TeachersConfig',
    'teams.apps.TeamsConfig',
    'timetables.apps.TimetablesConfig',
    'subjects.apps.SubjectsConfig',
    'semesters.apps.SemestersConfig',
    'exams_scores.apps.ExamsScoresConfig',
    'constants.apps.ConstantsConfig',
    # Config Rest APIs
    'rest_framework',
    # JWT Token Authentication
    'rest_framework_simplejwt',
    # Logout Sẽ add refresh token vào blacklist
    'rest_framework_simplejwt.token_blacklist',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Corsheaders
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'uredu.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'uredu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


"""
Set up database mysql connection
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'uredu',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

"""
Set up authentication by JWT token
"""
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # Có thể thêm scope để giới hạn truy cập từng view
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/day',
        'user': '100/day',
    },
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # )
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

"""
Quản lý hình ảnh media và các file static tĩnh
"""
MEDIA_URL = '/images/'
MEDIA_ROOT = BASE_DIR / 'static/images'

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from datetime import timedelta, datetime
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=3),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=15),
    # 'ROTATE_REFRESH_TOKENS': True,
    # 'BLACKLIST_AFTER_ROTATION': True
}


"""
Email settings
"""
import ssl
from django.utils import timezone

EMAIL_USERNAME = 'sangtest13@gmail.com'
EMAIL_PASSWORD = 'lgssluunyswgencs'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_CONTEXT = ssl.create_default_context()
EMAIL_RESET_TOKEN_EXPIRE_MINUTES = timedelta(minutes=15)
TIME_NOW = timezone.now()
RESET_STRING_TOKEN = 'ured'
