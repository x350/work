from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Patient


# Create your views here.

class PatientCreateView(CreateView):
    model = Patient
    template_name = 'patients/patient_add.html'

    fields = "historyNum", "fio", "typepatients"
    # form_class = GroupForm #для создания формы выбирается что-то одно
    # либо GroupForm либо fields
    success_url = reverse_lazy("patients:patients_list")
    # необходимо создать новый шаблон


class PatientDetailView(DetailView):
    template_name = 'patients/patient_details.html'
    model = Patient
    context_object_name = 'patient'

class PatientsListView(ListView):
    template_name = 'patients/patients_list.html'
    # model = Product
    context_object_name = 'patients'
    queryset = Patient.objects.filter(archived=False)

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy("patients:patients_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)
