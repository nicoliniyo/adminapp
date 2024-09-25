from django.db import models
from users_profiles.models import UsersProfile
from django.forms import formset_factory
from django import forms

class Organizacion(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    nit = models.IntegerField(null=True, blank=True)  # Assuming nit can be null

    def __str__(self):
        return self.nombre

class Pregunta(models.Model):
    tipo = models.CharField(max_length=255)
    nro_pregunta = models.IntegerField()
    columna = models.CharField(max_length=1)
    pregunta = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nro_pregunta} - {self.pregunta}"

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ('tipo', 'nro_pregunta', 'columna', 'pregunta')


# PreguntaFormSet = formset_factory(PreguntaForm, extra=40)
PreguntaFormSet = forms.modelformset_factory(Pregunta, fields='__all__')


class Prueba(models.Model):
    profile = models.ForeignKey(UsersProfile, on_delete=models.CASCADE)
    fecha_prueba = models.DateField()
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    valor = models.IntegerField()
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Prueba de {self.profile} en {self.fecha_prueba}"


class Prueba_resultado(models.Model):
    prueba_nro = models.IntegerField()
    prioridad = models.CharField(max_length=50)  # Puedes ajustar el tamaño según tus necesidades
    resultado = models.TextField()
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Resultado de la prueba {self.prueba_nro} para {self.organizacion}"