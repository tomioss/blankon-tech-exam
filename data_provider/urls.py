
from django.urls import path
from data_provider.views import EventApiView


app_name = "data_provider"

urlpatterns = [
    path("events/", EventApiView.as_view(), name="events"),
]

