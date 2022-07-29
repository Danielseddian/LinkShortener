from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views as v

app_name = "shortener"

router = DefaultRouter()
router.register("short_link", v.CreateShortLinkViewSet, basename="short_link")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("<str:short>", v.redirector, name="short_link_redirector")
]