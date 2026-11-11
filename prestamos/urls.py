from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "encargado/",
        views.PanelEncargadoView.as_view(),
        name="panel_encargado",
    ),
    path("", views.inicio, name="inicio"),
]
