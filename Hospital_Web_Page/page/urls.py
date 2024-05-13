from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("patient", views.patient, name="patient"),
    path("doctor", views.doctor, name="doctor"),
    path("admins", views.admins, name="admins"),
    path("create", views.patient_create, name="patient_create_account"),
    path("run_custom_query", views.run_custom_query, name='run_custom_query'),
    path('process', views.login_process, name='login_process'),
    path('create_user', views.create_user, name='create_user')
]