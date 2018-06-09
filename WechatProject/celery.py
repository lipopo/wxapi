from __future__ import unicode_literals, absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WecharProject.settings')

app = Celery('WechatProject')
app.config_from_object('django.conf:settings', namespace="CELERY")

app.autodiscover_tasks()
@app.task(bind=True)
def debug_app(self):
    return None