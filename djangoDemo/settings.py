# 超级管理员：admin root
# root root
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-2nhj(0u9!366y*@=!e5k8c=p3#9nd9q&b%o7vwsic#m4jf(dae"

# #字母验证码
# CAPTCHA_IMAGE_SIZE = (80, 45)   # 设置 captcha 图片大小
# CAPTCHA_LENGTH = 4   # 字符个数
# CAPTCHA_TIMEOUT = 1   # 超时(minutes)


# #加减乘除验证码
# CAPTCHA_OUTPUT_FORMAT = '%(image)s %(text_field)s %(hidden_field)s '
# CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_null',
#      'captcha.helpers.noise_arcs', # 线
#      'captcha.helpers.noise_dots', # 点
# )
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
# CAPTCHA_TIMEOUT = 1


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
    'users',
    'captcha',
    'rest_framework',
    'drf_yasg',
    'students.apps.StudentsConfig',
    'snippets.apps.SnippetsConfig',

]

# DRF全局配置
REST_FRAMEWORK = {
    # 配置全局分页
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,  # 每页数目
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',  # 时间格式
    'DEFAULT_RENDER_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],

}

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
        "DIRS": [f"{BASE_DIR}/templates", f"{BASE_DIR}/users/templates"],
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
    STATICFILES_DIRS = [BASE_DIR / 'static']
else:
    STATIC_ROOT = BASE_DIR / 'static'

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  # 配置语言
TIME_ZONE = 'Asia/Shanghai'  # 时区
USE_I18N = True
USE_TZ = True

# Database
# 数据库配置：https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DB_TYPE = "sqlite3"  # 数据库类型
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
