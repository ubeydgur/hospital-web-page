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
    path('login_patient', views.login_patient, name='login_patient'),
    path('login_admin', views.login_admin, name='login_admin'),
    path('login_doctor', views.login_doctor, name='login_doctor'),
    path('admin_index', views.admin_index, name='admin_index'),
    path('table_patient', views.table_patient, name='table_patient'),
    path('table_doctor', views.table_doctor, name='table_doctor'),
    path('table_appointment', views.table_appointment, name='table_appointment'),
    path('table_report', views.table_report, name='table_report'),
    path('create_patient', views.create_patient, name='create_patient'),
    path('create_patient_admin', views.create_patient_admin, name='create_patient_admin'),
    path('delete_patient', views.delete_patient, name='delete_patient'),
    path('create_report_admin', views.create_report_admin, name='create_report_admin'),
    path('delete_report', views.delete_report, name='delete_report'),
    path('create_doctor_admin', views.create_doctor_admin, name='create_doctor_admin'),
    path('delete_doctor', views.delete_doctor, name='delete_doctor'),
    path('create_appointment_admin', views.create_appointment_admin, name='create_appointment_admin'),
    path('delete_appointment', views.delete_appointment, name='delete_appointment')
]