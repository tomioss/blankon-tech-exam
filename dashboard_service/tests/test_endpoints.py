from datetime import date

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

from rest_framework import status
from rest_framework.test import APITestCase

from dashboard_service.models import BookingEvent


def create_booking_event(room_id, booking_id=1, night_of_stay=date.today()):
    return BookingEvent.objects.create(
        booking_id=booking_id,
        hotel_id="1",
        room_id=room_id,
        rpg_status=1,
        night_of_stay=night_of_stay,
        timestamp=timezone.now()
    )


def create_user(username, password):
    user = User.objects.create_user(username)
    user.set_password(password)
    user.save()


class DashboardApiViewTest(APITestCase):
    url = reverse("dashboard_service:dashboard-list")

    def _login_user(self):
        username = "username"
        password = "password"
        create_user(username, password)
        self.assertTrue(self.client.login(username=username, password=password))

    def setUp(self):
        create_booking_event("1")

        self._login_user()

    def test_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["booking_id"], 1)
        self.assertEqual(data["results"][0]["hotel_id"], 1)
        self.assertEqual(data["results"][0]["room_id"], "1")

    def test_list_param(self):
        today = date.today()
        params = {
            "month": today.month,
            "day": today.day,
            "year": today.year
        }

        response = self.client.get(self.url, params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["booking_id"], 1)
        self.assertEqual(data["results"][0]["hotel_id"], 1)
        self.assertEqual(data["results"][0]["room_id"], "1")

    def test_list_param_none(self):
        params = {
            "month": 1,
            "day": 1,
            "year": 2024
        }

        response = self.client.get(self.url, params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["count"], 0)

