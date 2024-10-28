from celery import shared_task

from dashboard_service.services import get_data_provider_and_save_events
from dashboard_service.utils import get_date_time_today


@shared_task
def hello_task():
    return "Hello!"


@shared_task
def get_data_provider_events():
    start_time, end_time = get_date_time_today()
    get_data_provider_and_save_events(start_time, end_time)

