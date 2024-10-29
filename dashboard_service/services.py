import csv
import requests

from django.conf import settings

from dashboard_service.models import BookingEvent


def read_csv(path, params=None):
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

            if params:
                if "hotel_id" in params and params["hotel_id"] == lines["hotel_id"]:
                    data.append(line_data)
                if "room_reservation_id" in params and params["room_reservation_id"] == lines["room_reservation_id"]:
                    data.append(line_data)
            else:
                data.append(line_data)

    return data


def save_to_data_provider(data):
    url = settings.DATA_PROVIDER_URL

    result = requests.post(url, auth=(settings.API_USER, settings.API_PASS), data=data)

    return result


def send_bookings(params=None):
    path = settings.DATA_CSV

    data = read_csv(path, params)

    for line_data in data:
        result = save_to_data_provider(line_data)

        if result.status_code != 201:
            break


def retrieve_data_provider(start_time, end_time, page):
    url = settings.DATA_PROVIDER_URL
    params = {
        "updated_gte": start_time,
        "updated_lte": end_time,
        "page": page,
    }

    result = requests.get(url, auth=(settings.API_USER, settings.API_PASS), params=params)

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



def get_data_provider_and_save_events(start_time, end_time):
    page = 1

    while True:
        result = retrieve_data_provider(start_time, end_time, page)

        if result.status_code != 200:
            break

        data = result.json()

        if "results" in data:
            save_booking_events(data["results"])

        page += 1

