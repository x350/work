from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def patientsadd_list(requset: HttpRequest):
    context = {
    }
    return render(requset, 'patients/patients_list.html', context=context)