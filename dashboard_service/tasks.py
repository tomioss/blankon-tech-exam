
from dashboard_service.services import retrieve_data_provider, save_booking_events


def get_data_provider_events():
    start_time = "2022-01-01"
    end_time = "2022-01-31"
    page = 1

    while True:
        result = retrieve_data_provider(start_time, end_time, page)
        data = result.json()

        if "detail" in data and data["detail"] == "Invalid page.":
            break

        if "results" in data:
            save_booking_events(data["results"])

        page += 1

