from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieproj.settings')
app = Celery(
    "movieproj", broker='redis://redis:6379/', backend='redis://redis:6379/'
)
app.autodiscover_tasks()