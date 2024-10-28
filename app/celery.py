import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'save-data-provider-events-task': {
        'task': 'dashboard_service.tasks.save_data_provider_events',
        'schedule': crontab(hour=9, minute=0)
    },
    'get-data-provider-events-task': {
        'task': 'dashboard_service.tasks.get_data_provider_events',
        'schedule': crontab(hour=23, minute=55)
    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

