import requests
from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.forms import formset_factory
from rest_framework import viewsets
from .serializers import OrganizacionSerializer, PreguntaSerializer, PruebaSerializer, Prueba_resultadoSerializer

from .models import Organizacion, Pregunta, Prueba, Prueba_resultado, PreguntaForm, PreguntaFormSet


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
    print('CREATE PREGUNTAS')
    if request.method == 'POST':
        print('POST CALL')
        formset = PreguntaFormSet(request.POST)
        # form_items = [(key, value) for key, value in request.POST.items()]
        # print("Form Items:")
        # for item in form_items:
        #     print(item)

        count_a = 0
        count_b = 0
        count_c = 0
        count_d = 0

        # Iterate over form items to count occurrences
        for key, value in request.POST.items():
            if '_a_' in key:
                count_a += 1
            elif '_b_' in key:
                count_b += 1
            elif '_c_' in key:
                count_c += 1
            elif '_d_' in key:
                count_d += 1

        # Store the counts in a dictionary
        data = {
            'count_a': count_a,
            'count_b': count_b,
            'count_c': count_c,
            'count_d': count_d,
        }
        # Print the counts for debugging
        print(data)
        # Do something else after saving the formset
        if formset.is_valid():
            print('SAVE')
        else:
            # Print or log formset errors to see what went wrong
            print(formset.errors)
    else:
        formset = formset_factory(PreguntaForm, extra=40)

    return render(request, 'preguntas_create.html', {'formset': formset, 'error': formset.errors})