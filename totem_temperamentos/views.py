import requests
from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.forms import formset_factory
from rest_framework import viewsets
from .serializers import OrganizacionSerializer, PreguntaSerializer, PruebaSerializer, Prueba_resultadoSerializer

from .models import Organizacion, Pregunta, Prueba, Prueba_resultado, PreguntaForm

class OrganizacionViewSet(viewsets.ModelViewSet):
    queryset = Organizacion.objects.all()
    serializer_class = OrganizacionSerializer

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

class PruebaViewSet(viewsets.ModelViewSet):
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerializer

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        prueba = get_object_or_404(queryset, pk=pk)
        serializer = PruebaSerializer(prueba)
        return Response(serializer.data)

class PruebaResultadoViewSet(viewsets.ModelViewSet):
    queryset = Prueba_resultado.objects.all()
    serializer_class = Prueba_resultadoSerializer


def pregunta_list(request):
    preguntas = Pregunta.objects.all()
    return render(request, 'preguntas_list.html', {})


def create_preguntas(request):
    if request.method == 'POST':
        formset = PreguntaFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            # Do something else
    else:
        formset = formset_factory(PreguntaForm, extra=40)
    return render(request, 'preguntas_create.html', {'formset': formset})