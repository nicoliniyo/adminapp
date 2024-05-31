from django.db import models
from django import forms
from django.utils import timezone

class Persona(models.Model):
    id = models.BigAutoField(primary_key=True)
    casada = models.CharField(max_length=255, blank=True)
    extension = models.CharField(max_length=255)
    # fechanac = models.CharField(max_length=255)
    fechanac = models.DateTimeField(default=timezone.now)
    genero = models.CharField(max_length=255)
    materno = models.CharField(max_length=255)
    nomcompleto = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    nrodocumento = models.CharField(max_length=255)
    nrodocumentochars = models.CharField(max_length=255)
    nrodocumentoint = models.CharField(max_length=255)
    paterno = models.CharField(max_length=255)
    tipodocumento = models.CharField(max_length=255)


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('casada', 'extension', 'fechanac', 'genero', 'materno', 'nomcompleto', 'nombres', 'nrodocumento', 'nrodocumentochars', 'nrodocumentoint', 'paterno', 'tipodocumento')
