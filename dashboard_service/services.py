import csv
import requests


def read_csv(path):
    data = []

    with open(path, mode="r") as file:
        csvFile = csv.reader(file)

        for lines in csvFile:
            print(lines)
            line_data = {
                "booking_id": "",
                "hotel_id": "",
                "room_id": "",
                "rpg_status": "",
                "night_of_stay": "",
                "timestamp": "",
            }
            data.append(line_data)

    return data


def save_to_data_provider(data):
    url = ""

    result = requests.post(url, data)

    return result

