from .views import *
from django.urls import path


urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("login", Login.as_view(), name="login"),
    ]