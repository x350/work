from django.urls import path

from .views import patients_list

app_name = "patients"

urlpatterns = [
    path("patients_list/", patients_list, name="patients_list"),
]