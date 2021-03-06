"""
Django settings for our farmstand project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
import sys

from configurations import Configuration, values


class Common(Configuration):

    ADMINS = (
        ('Admin', 'info@example.com'),
    )

    AUTH_USER_MODEL = 'userprofile.User'

    MANAGERS = ADMINS

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, os.path.join(BASE_DIR, 'farmstand/apps'))

    USE_SOUTH = False

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    TEMPLATE_DEBUG = False

    DEFAULT_CURRENCY = 'USD'
    DEFAULT_WEIGHT = 'Ounces'

    CANONICAL_HOSTNAME = os.environ.get('CANONICAL_HOSTNAME', 'localhost:8000')
    PAYMENT_BASE_URL = 'http://%s/' % CANONICAL_HOSTNAME

    PAYMENT_MODEL = 'order.Payment'

    PAYMENT_VARIANTS = {
        'default': ('payments.dummy.DummyProvider', {})
    }

    PAYMENT_HOST = os.environ.get('PAYMENT_HOST', 'localhost:8000')

    SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
    SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

    CHECKOUT_PAYMENT_CHOICES = [
        ('default', 'Dummy provider')
    ]

    FACEBOOK_APP_ID = ""
    GOOGLE_CLIENT_ID = ""


    # Application definition

    INSTALLED_APPS = (
        'suit',
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.redirects",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.sitemaps",
        "django.contrib.staticfiles",

        "django_extensions",
        'floppyforms',
        'rest_framework',

        # Saleor apps
        'saleor.userprofile',
        'saleor.product',
        'saleor.cart',
        'saleor.checkout',
        'saleor.core',
        'saleor.order',
        'saleor.registration',
        'saleor.dashboard',

        # External apps
        'versatileimagefield',
        'django_prices',
        'emailit',
        'mptt',
        'payments',
        'selectable',
        'materializecssform'
    )

    TEMPLATE_CONTEXT_PROCESSORS = Configuration.TEMPLATE_CONTEXT_PROCESSORS + \
        ("django.core.context_processors.request",
         "django.core.context_processors.tz",
         "saleor.core.context_processors.canonical_hostname",
         "saleor.core.context_processors.default_currency",
         "saleor.core.context_processors.categories"
        )

    MIDDLEWARE_CLASSES = (
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'saleor.cart.middleware.CartMiddleware',
        'saleor.core.middleware.DiscountMiddleware',
        'saleor.core.middleware.GoogleAnalytics',

    )

    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    )

    ACCOUNT_AUTHENTICATION_METHOD = "email"
    ACCOUNT_USER_MODEL_USERNAME_FIELD = None
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_UNIQUE_EMAIL = True
    ACCOUNT_USERNAME_REQUIRED = False

    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        'saleor.registration.backends.EmailPasswordBackend',
        #'saleor.registration.backends.ExternalLoginBackend',
        'saleor.registration.backends.TrivialBackend',
        "allauth.account.auth_backends.AuthenticationBackend",)

    ROOT_URLCONF = 'farmstand.urls'

    WSGI_APPLICATION = 'farmstand.wsgi.application'

    DATABASES = values.DatabaseURLValue('sqlite:///{0}'.format(
        os.path.join(BASE_DIR, 'db.sqlite3'),
        environ=True))

    NEVERCACHE_KEY = values.Value('klladsf-wefkjlwef-wekjlwef--wefjlkjfslkxvl')

    #CACHES = values.CacheURLValue('memcached://127.0.0.1:11211')

    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'America/New_York'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    SITE_ID = 1

    ALLOWED_HOSTS = values.Value('*')

    SESSION_EXPIRE_AT_BROWSER_CLOSE = True

    PROJECT_DIRNAME = BASE_DIR.split(os.sep)[-1]

    CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_DIRNAME

    MEDIA_URL = "/media/"

    MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media')

    TEMPLATE_DIRS = (os.path.join(BASE_DIR, "farmstand/templates"),)

    STATIC_URL = '/static/'

    STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "farmstand/static"),
    )

    #DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    AWS_ACCESS_KEY_ID = values.Value()
    AWS_SECRET_ACCESS_KEY = values.Value()
    AWS_STORAGE_BUCKET_NAME = 'example.com'
    AWS_HEADERS = {'ExpiresDefault': 'access plus 30 days',
                   'Cache-Control': 'max-age=86400', }

    # Account activations automatically expire after this period
    ACCOUNT_ACTIVATION_DAYS = 14

    LOGIN_EXEMPT_URLS = ['', '/',
                         '/accounts/login/',
                         'login',
                         '/accounts/signup/']

    LOGIN_URL = '/accounts/login/'
    LOGIN_REDIRECT_URL = '/'
    LOGOUT_URL = '/accounts/logout/'

    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }


class Dev(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = TEMPLATE_DEBUG = True

    DATABASES = values.DatabaseURLValue('sqlite:///{0}'.format(
        os.path.join(Common.BASE_DIR, 'db.sqlite3'),
        environ=True))

    SECRET_KEY = 'notasecretatall'

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    INSTALLED_APPS = Common.INSTALLED_APPS + ('debug_toolbar',)


class Stage(Common):
    DEBUG = TEMPLATE_DEBUG = True

    SECRET_KEY = values.SecretValue()

    EMAIL_HOST = values.Value('localhost')
    EMAIL_HOST_USER = values.Value()
    EMAIL_HOST_PASSWORD = values.Value()
    EMAIL_PORT = values.Value()
    EMAIL_USE_TLS = values.BooleanValue(False)


class Prod(Common):
    """
    The in-production settings.
    """
    DEBUG = TEMPLATE_DEBUG = False

    SECRET_KEY = values.SecretValue()

    EMAIL_HOST = values.Value()
    EMAIL_HOST_USER = values.Value()
    EMAIL_HOST_PASSWORD = values.Value()
    EMAIL_PORT = values.Value()
    EMAIL_USE_TLS = values.BooleanValue(True)

    DSN_VALUE = values.Value()

    # If we're on production, connect to Sentry
    RAVEN_CONFIG = {
        'dsn': DSN_VALUE.setup('DSN_VALUE'),
    }

    INSTALLED_APPS = Common.INSTALLED_APPS + (
        'raven.contrib.django.raven_compat',)
