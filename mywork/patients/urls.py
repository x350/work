from django.urls import path

from .views import PatientDetailView, PatientsListView, PatientCreateView, PatientDeleteView

app_name = "patients"



urlpatterns = [
    path("patients_list/", PatientsListView.as_view(), name="patients_list"),
    path("patient_add/", PatientCreateView.as_view(), name="patient_add"),
    path("patient_detail/<int:pk>", PatientDetailView.as_view(), name="patient_detail"),
    path("<int:pk>/confirm-archived/", PatientDeleteView.as_view(), name='patient_delete'),
]