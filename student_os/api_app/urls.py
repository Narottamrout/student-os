# from django.urls import path
# from .views import hello

# urlpatterns = [
#     path("hello/", hello),
# ]
from django.urls import path
from .views import hello

urlpatterns = [
    path("hello/", hello),
]