from datetime import datetime

from django.test import TestCase

from dashboard_service.utils import get_booking_data, get_date_time_today


class DateTimeUtilsTest(TestCase):
    def test_get_date_time_today(self):
        start, end = get_date_time_today()

        self.assertTrue(isinstance(start, datetime))
        self.assertTrue(isinstance(end, datetime))


class BookingDataTest(TestCase):
    def test_get_booking_data(self):
        result = get_booking_data()

        self.assertEquals(len(result), 8)

