from django.urls import path
from .models import *
from . import views

app_name ="application"
urlpatterns = [
    path("", views.index, name="index"),
]
