from django.urls import path
from iot.views import index, tutorial_card, login_view, cadastro
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("index/", index, name="index"),
    path("tutorial/<int:card_id>/", tutorial_card, name="tutorial-card"),
    path("login/", login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("cadastro/", cadastro, name="cadastro"),
]
