"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.1.

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
SECRET_KEY = 'django-insecure-s#3_hk)05gh(g6a#8y^lniqbjsa-avanf^onkl9ack1pqit-)#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 웹서버 도메인 또는 아이피주소 설정
ALLOWED_HOSTS = ['127.0.0.1']


# Application definition
# 앱이 만들어 지면 이곳에 항상 등록하기
INSTALLED_APPS = [
    'webcrawlingapp',
    'practiceapp',
    'mysqlapp',
    'frontapp',
    'firstapp',
    'secondapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'config.urls'
# html 파일을 관리할 위치 지정 /BASE_DIR / 'templates']
TEMPLATES = [
    {   
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# 데이터베이스 연결 설정하는 곳
DATABASES = {
    ### SQLite3 데이터베이스는 디폴트로 사용
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    ### MySQL 데이터베이스 서버 연결
    # mysql 패키지 설치 해야함 : pip install mysqlclient
    'mysql': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pknu',
        'USER': 'pknu',
        'PASSWORD': 'dbdb',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
### default가 아닌 DB 사용시 아래 리스트 추가
# [DB를 사용할 앱이름.파일이름.클래스이름]
DATABASE_ROUTERS = ['mysqlapp.router.DBRouter', 'practiceapp.router.DBRouter',
                    'webcrawlingapp.router.DBRouter']

### DB 실행 내용을 프롬프트에서 확인하기 위해 아래 추가
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
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


# 웹에 표시할 언어 지정
LANGUAGE_CODE = 'ko-kr'
# 웹에서 사용 할 시간대
TIME_ZONE = 'Asia/Seoul'


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# css.js, image 등을 관라할 폴더
STATICFILES_DIR = [
    BASE_DIR / 'static',
    
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
