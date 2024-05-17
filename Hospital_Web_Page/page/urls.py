from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("patient", views.patient, name="patient"),
    path("doctor", views.doctor, name="doctor"),
    path("admins", views.admins, name="admins"),
    path("create", views.patient_create, name="patient_create_account"),
    path("run-custom-query", views.run_custom_query, name='run_custom_query'),
    path('login-patient', views.login_patient, name='login_patient'),
    path('login-admin', views.login_admin, name='login_admin'),
    path('login-doctor', views.login_doctor, name='login_doctor'),
    path('admin-index', views.admin_index, name='admin_index'),
    path('table-patient', views.table_patient, name='table_patient'),
    path('table-doctor', views.table_doctor, name='table_doctor'),
    path('table-appointment', views.table_appointment, name='table_appointment'),
    path('table-report', views.table_report, name='table_report'),
    path('create-patient', views.create_patient, name='create_patient'),
    path('create-patient-admin', views.create_patient_admin, name='create_patient_admin'),
    path('delete-patient', views.delete_patient, name='delete_patient'),
    path('create-report-admin', views.create_report_admin, name='create_report_admin'),
    path('delete-report', views.delete_report, name='delete_report'),
    path('create-doctor-admin', views.create_doctor_admin, name='create_doctor_admin'),
    path('delete-doctor', views.delete_doctor, name='delete_doctor'),
    path('create-appointment-admin', views.create_appointment_admin, name='create_appointment_admin'),
    path('delete-appointment', views.delete_appointment, name='delete_appointment')
]