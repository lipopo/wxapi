from __future__ import unicode_literals, absolute_import
import os
from celery import Celery
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WechatProject.settings')

app = Celery('WechatProject')
app.config_from_object('django.conf:settings', namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'refreshAccessToken': {
        'task': 'WechatAPI.tasks.refreshAccessToken',
        'schedule': timedelta(seconds=4000),
        # 'schedule': crontab(seconds='7000'),
        # 'args': (16, 16)
    },
}
@app.task(bind=True)
def debug_app(self):
    return None