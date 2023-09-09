from django.urls import path
from iot.views import index


urlpatterns = [
    path("index/", index, name='index'),
]
