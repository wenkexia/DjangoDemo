

#超级管理员：admin root
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-2nhj(0u9!366y*@=!e5k8c=p3#9nd9q&b%o7vwsic#m4jf(dae"



ALLOWED_HOSTS = []


# Application definition
# 注册app
INSTALLED_APPS = [
    "mdeditor",
    'simpleui',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    'app1',
    'app3',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "djangoDemo.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "djangoDemo.wsgi.application"




# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if DEBUG:
    STATICFILES_DIRS = [BASE_DIR/'static']
else:
    STATIC_ROOT = BASE_DIR/'static'

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans' # 配置语言
TIME_ZONE = 'Asia/Shanghai'  #时区
USE_I18N = True
USE_TZ = True


# Database
# 数据库配置：https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DB_TYPE = "mysql"  # 数据库类型
if DB_TYPE == "mysql":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # MYSQL
            'NAME': 'djangodb',  # 数据库名
            "USER": "root",  # 用户名
            "PASSWORD": "root",  # 密码
            "HOST": "127.0.0.1",  # 主机地址
            "PORT": 3306,  # 端口号
            "OPTIONS": {
                "init_command": "set foreign_key_checks = 0;",  # 取消外键约束
            }
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }



# 配置日志
# 目的是为了在Debug模式下，我们能够看到执行ORM相关操作，底层的SQL语句是什么
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}




MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/media/'
X_FRAME_OPTIONS = 'SAMEORIGIN'