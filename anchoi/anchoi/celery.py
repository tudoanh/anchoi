from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from celery.signals import after_task_publish, task_success, task_failure

from events.utils import send_msg

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anchoi.settings')

app = Celery('anchoi', backend='redis://localhost:6379/0')
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.timezone = 'Asia/Saigon'

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

HANOI_CENTER = (21.028811, 105.848977)
SAIGON_CENTER = (10.782812, 106.695886)


app.conf.beat_schedule = {
    'hourly-scan': {
        'task': 'events.tasks.hourly_scan',
        'schedule': crontab(minute=0, hour='*/1'),
    },
    'daily-scan': {
        'task': 'events.tasks.daily_scan',
        'schedule': crontab(minute=0, hour=2)
    },
    'hanoi-weekly-scan': {
        'task': 'events.tasks.weekly_scan',
        'schedule': crontab(minute=0, hour=2, day_of_week=1),
        'kwargs': {
            'lat': HANOI_CENTER[0],
            'lon': HANOI_CENTER[1],
            'distance': 8000
        }
    },
    'saigon-weekly-scan': {
        'task': 'events.tasks.weekly_scan',
        'schedule': crontab(minute=0, hour=2, day_of_week=2),
        'kwargs': {
            'lat': SAIGON_CENTER[0],
            'lon': SAIGON_CENTER[1],
            'distance': 10000
        }
    }
}


@after_task_publish.connect
def start_task(sender=None, headers=None, body=None, **kwargs):
    if sender == 'events.tasks.hourly_scan':
        send_msg('Start hourly scan.')
    elif sender == 'events.tasks.daily_scan':
        send_msg('Start daily scan.')
    elif sender == 'events.tasks.weekly_scan':
        send_msg('Start weekly scan.')


@task_success.connect
def send_result(sender, result, **kwargs):
    if sender == 'events.tasks.hourly_scan':
        send_msg('Hourly scan done.')
    elif sender == 'events.tasks.daily_scan':
        send_msg('Daily scan done.')
    elif sender == 'events.tasks.weekly_scan':
        send_msg('Weekly scan done.')


@task_failure.connect
def task_failed(sender=None, headers=None, body=None, **kwargs):
    send_msg(sender)
    send_msg(headers)
    send_msg(body)
