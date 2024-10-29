from datetime import datetime
from unittest import mock

from django.test import TestCase

from dashboard_service.services import retrieve_data_provider, save_booking_events, save_to_data_provider
from dashboard_service.utils import get_booking_data, get_date_time_today


class CallDataProviderApiTest(TestCase):

    def setUp(self):
        self.data = {
            "booking_id": 1,
            "hotel_id": 2607,
            "timestamp": datetime.now(),
            "rpg_status": 1,
            "room_id": "1",
            "night_of_stay": "2024-10-26"
        }

    @mock.patch("dashboard_service.services.requests.post")
    def test_save_to_data_provider(self, mock_post):
        mock_post.return_value = self.data

        result = save_to_data_provider(self.data)

        self.assertEquals(result, self.data)

    @mock.patch("dashboard_service.services.requests.get")
    def test_retrieve_data_provider(self, mock_get):
        mock_get.return_value = self.data
        start_time, end_time = get_date_time_today()

        results = retrieve_data_provider(start_time, end_time, 1)

        self.assertEquals(results, self.data)


class BulkCreateBookingEvents(TestCase):
    def test_save_booking_events(self):
        data = get_booking_data()

        result = save_booking_events(data)

        self.assertEquals(len(result), 8)

