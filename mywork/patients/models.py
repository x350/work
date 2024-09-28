from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models
class TypePatients(models.Model):
    typepatient = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.typepatient!r}"


class Doctor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name!r}"


class Otdel(models.Model):
    num = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(50)
        ]
    )
    name = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return f"{self.num!r} отделение"


class Patient(models.Model):
    class Meta:
        pass

    historyNum = models.IntegerField(max_length=100000)
    fio = models.CharField(max_length=100)
    # name = models.CharField(max_length=100)
    # secondname = models.CharField(max_length=100)
    typepatients = models.ForeignKey(TypePatients, on_delete=models.PROTECT)
    archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.typepatients} {self.fio!r})"
