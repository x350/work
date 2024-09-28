from django.contrib import admin

from .models import Patient, TypePatients


# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = "pk", "historyNum", "fio", "typepatients", "archived"

    list_display_links = 'pk', "fio",


@admin.register(TypePatients)
class PatientAdmin(admin.ModelAdmin):
    list_display = "pk", "typepatient",
    list_display_links = "pk", "typepatient",
