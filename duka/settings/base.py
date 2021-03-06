import os
from decouple import config
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

ADMINS = (
  ('Prof. Isaac', 'deisaack@gmail.com'),
)
ALLOWED_HOSTS= ['duka.herokuapp.com']
AUTH_USER_MODEL = 'authtools.User'
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

AWS_STATIC_LOCATION = 'static'

AWS_PUBLIC_MEDIA_LOCATION = 'media/public'

AWS_PRIVATE_MEDIA_LOCATION = 'media/private'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRISPY_TEMPLATE_PACK = 'bootstrap3'


# GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyD2XP6khyd123inKasJ2NxfWodaqYO_HqY'
GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyCKKERHiiwDU37DQ719Uj93bXVlSGRMn9U'
# GEOPOSITION_GOOGLE_MAPS_API_KEY = config('GEOPOSITION_GOOGLE_MAPS_API_KEY')
GOOGLE_RECAPTCHA_SECRET_KEY = config('GOOGLE_RECAPTCHA_SECRET_KEY')
INSTALLED_APPS = [
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'duka.accounts',
    'duka.profiles',
    'duka.favorites',
    'duka.files',

    'rest_framework',
    'crispy_forms',
    'authtools',
    'braces',
    'easy_thumbnails',
    'geoposition',
    'storages',
]
LANGUAGE_CODE = 'en-us'
LIVE_DIR = os.path.join(BASE_DIR, "live")
LOGIN_REDIRECT_URL = reverse_lazy("home")
LOGIN_URL = reverse_lazy("accounts:login")
MANAGERS = ADMINS
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(LIVE_DIR, 'live/media')
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}
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
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 6
}
ROOT_URLCONF = 'duka.urls'
SECRET_KEY = config('SECRET_KEY')
SITE_ID = 1
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATIC_ROOT = os.path.join(LIVE_DIR, "static")
THUMBNAIL_EXTENSION = 'png'
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
TIME_ZONE = 'Africa/Nairobi'
USE_L10N = True
USE_I18N = True
USE_TZ = True
WSGI_APPLICATION = 'duka.wsgi.application'

