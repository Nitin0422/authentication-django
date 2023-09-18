from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path("", views.HomePage, name="home"),
    path("register/", views.Register, name="register")
]