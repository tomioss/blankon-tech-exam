from rest_framework.routers import DefaultRouter

from dashboard_service.views import DashboardApiView, SendBookingApiView, ViewBookingApiView


app_name = "dashboard_service"

router = DefaultRouter()
router.register("dashboard", DashboardApiView, basename="dashboard")
router.register("send_booking", SendBookingApiView, basename="send_booking")
router.register("view_booking", ViewBookingApiView, basename="view_booking")

urlpatterns = router.urls

