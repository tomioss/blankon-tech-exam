import csv
import requests

from django.conf import settings

from dashboard_service.models import BookingEvent


def read_csv(path):
    data = []

    with open(path, mode="r") as file:
        csvFile = csv.DictReader(file)

        for lines in csvFile:
            line_data = {
                "booking_id": lines["id"],
                "hotel_id": lines["hotel_id"],
                "room_id": lines["room_reservation_id"],
                "rpg_status": lines["status"],
                "night_of_stay": lines["night_of_stay"],
                "timestamp": lines["event_timestamp"],
            }
            data.append(line_data)

    return data


def save_to_data_provider(data):
    url = settings.DATA_PROVIDER_URL

    result = requests.post(url, data)

    return result


def send_bookings():
    path = settings.DATA_CSV

    data = read_csv(path)

    for line_data in data:
        save_to_data_provider(line_data)


def retrieve_data_provider(start_time, end_time, page):
    url = settings.DATA_PROVIDER_URL
    params = {
        "hotel_id": 2607,
        "updated_gte": start_time,
        "updated_lte": end_time,
        "page": page
    }

    result = requests.get(url, params=params)

    return result


def save_booking_events(json_data):
    booking_events = []

    for data in json_data:
        booking_events.append(BookingEvent(
            booking_id=data["booking_id"],
            hotel_id=data["hotel_id"],
            timestamp=data["timestamp"],
            rpg_status=data["rpg_status"],
            room_id=data["room_id"],
            night_of_stay=data["night_of_stay"],
        ))

    return BookingEvent.objects.bulk_create(booking_events)

