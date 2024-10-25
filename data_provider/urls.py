from rest_framework.routers import DefaultRouter

from data_provider.views import EventApiView


app_name = "data_provider"

router = DefaultRouter()
router.register("events", EventApiView, basename="events")

urlpatterns = router.urls

