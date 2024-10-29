from datetime import date

from django.urls import reverse
from django.utils import timezone

from rest_framework import status
from rest_framework.test import APITestCase

from data_provider.models import Event


def create_booking_event(room_id, booking_id=1, night_of_stay=date.today()):
    return Event.objects.create(
        booking_id=booking_id,
        hotel_id="1",
        room_id=room_id,
        rpg_status=1,
        night_of_stay=night_of_stay,
        timestamp=timezone.now()
    )


class DataProviderEventApiViewTest(APITestCase):
    url = reverse("data_provider:events-list")

    def setUp(self):
        event = create_booking_event("1")
        self.detail_url = reverse("data_provider:events-detail", args=[event.id])

    def test_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["results"][0]["booking_id"], 1)
        self.assertEqual(data["results"][0]["hotel_id"], 1)
        self.assertEqual(data["results"][0]["room_id"], "1")

    def test_list_param(self):
        params = {
            "hotel_id": "1",
            "rpg_status": "1"
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
            "hotel_id": "0",
            "rpg_status": "0",
            "room_id": "0"
        }

        response = self.client.get(self.url, params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["count"], 0)

    def test_detail(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["booking_id"], 1)
        self.assertEqual(data["hotel_id"], 1)
        self.assertEqual(data["room_id"], "1")

