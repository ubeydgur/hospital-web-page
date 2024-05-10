from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("index", views.index),
    path("patient", views.patient),
    path("doctor", views.doctor),
    path("admins", views.admins)
]