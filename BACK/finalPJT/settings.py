"""
Django settings for finalPJT project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-la15c8g$(z%t@cc)a7xvdnzidf(a98$qis&(@qu=h4!$2zuq1&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    #local apps
    'movies',
    'accounts',
    'articles',

    #3rd party app
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken', # token 기반 auth

    # CORS 
    'corsheaders',

    # DRF auth
    'dj_rest_auth', # signup 제외 auth관련 담당
    'dj_rest_auth.registration', # signup
    
    # signup을 위해 필요함.
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    #native apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites' # dj-rest-auth signup 필요

]
SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # CORS 관련 추가
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'finalPJT.urls'

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

WSGI_APPLICATION = 'finalPJT.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'asia/seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#custom user model 사용을 위해, 
AUTH_USER_MODEL = 'accounts.User'

# CORS 모든 요청에 대해 허용 
CORS_ALLOW_ALL_ORIGINS = True



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES' : [ 
        'rest_framework.authentication.TokenAuthentication', # 인증관련해서 토큰을 사용하여 하겠다.
    ],
    'DEFAULT_PERMISSION_CLASSES': [ 
        # 'rest_framework.permissions.AllowAny' # 기본 값을 누구나 허용하겠다.
        'rest_framework.permissions.IsAuthenticated', # 인증 된 사용자만 모든 작업이 가능 # 401 unauthorized
        
    ]
}