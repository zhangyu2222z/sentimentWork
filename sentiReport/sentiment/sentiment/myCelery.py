import os
from celery import Celery,platforms
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','sentiment.settings')
app = Celery('sentiment')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
platforms.C_FORCE_ROOT = True