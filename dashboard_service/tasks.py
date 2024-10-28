from celery import shared_task

from dashboard_service.services import get_data_provider_and_save_events, save_to_data_provider
from dashboard_service.utils import get_booking_data, get_date_time_today


@shared_task
def hello_task():
    return "Hello!"


@shared_task
def save_data_provider_events():
    data = get_booking_data()

    for line_data in data:
        result = save_to_data_provider(line_data)

        if result.status_code != 201:
            break


@shared_task
def get_data_provider_events():
    start_time, end_time = get_date_time_today()
    get_data_provider_and_save_events(start_time, end_time)

