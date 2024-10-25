from rest_framework.routers import DefaultRouter

from dashboard_service.views import DashboardApiView


app_name = "dashboard_service"

router = DefaultRouter()
router.register("dashboard", DashboardApiView, basename="dashboard")

urlpatterns = router.urls

