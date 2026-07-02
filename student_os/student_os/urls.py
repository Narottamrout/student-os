from django.contrib import admin
from django.urls import path, include
from api_app.views import home

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/", include("api_app.urls")),
]