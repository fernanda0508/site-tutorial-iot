from django.urls import path
from iot.views import index


urlpatterns = [
    path("index/", index, name='index'),
    # path('cards/', CardListView.as_view(), name='card-list'),
]
