import csv
import requests

from django.conf import settings


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

