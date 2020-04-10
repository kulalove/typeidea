from .base import *#NOGA 告诉规范此处无需检测
DEBUG=True#可在开发环境中，****绝不可在线上环境中用

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}