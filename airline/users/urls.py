from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,"index"),
    path("login", views.login_view, login = "login"),
    path("logout", views.logout_view, logout = "logout")
]
