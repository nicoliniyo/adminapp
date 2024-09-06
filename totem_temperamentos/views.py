import requests
from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.forms import formset_factory
from rest_framework import viewsets
from .constants import TEMPERATURA_PROMPT
from .serializers import OrganizacionSerializer, PreguntaSerializer, PruebaSerializer, Prueba_resultadoSerializer

from .models import Organizacion, Pregunta, Prueba, Prueba_resultado, PreguntaForm, PreguntaFormSet

import aiopen



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


def eval_preguntas(request):
    print("request.POST:", request.POST)
    print("request.POST.items():", request.POST.items())
    results = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

    for key, value in request.POST.items():
        if 'fortaleza_' in key or 'debilidad_' in key:
            print(key, value)
            if 'a' in value:
                results['a'] += 1
            elif 'b' in value:
                results['b'] += 1
            elif 'c' in value:
                results['c'] += 1
            elif 'd' in value:
                results['d'] += 1

    return results

def create_preguntas(request):
    print('CREATE PREGUNTAS')
    if request.method == 'POST':
        print('POST CALL')
        form_items = [(key, value) for key, value in request.POST.items()]
        print("Form Items:")
        for item in form_items:
            print(item)

        formset = PreguntaFormSet(request.POST)
        data = eval_preguntas(request)
        # Print the counts for debugging
        print(data)
        prompt_data = TEMPERATURA_PROMPT + " Sanguíneo:" + str(data['a']) + " Colérico" + str(data['b']) + " Melancólico" + str(data['c']) + " Flemático" + str(data['d'])
        ai_response = aiopen.views.send_request(prompt_data)


        return render(request, 'preguntas_result.html', {
            'san': (data['a']),
            'col' : (data['b']),
            'mel' : (data['c']),
            'fle' : (data['d']),
            'ai_response': ai_response, })
        # Do something else after saving the formset
        if formset.is_valid():

            print('SAVE')
        else:
            # Print or log formset errors to see what went wrong
            print(formset.errors)
    else:
        formset = formset_factory(PreguntaForm, extra=40)

    return render(request, 'preguntas_create.html', {'formset': formset, })


def create_preguntas_t(request):
    print('CREATE PREGUNTAS')
    if request.method == 'POST':
        print('POST CALL')
        formset = PreguntaFormSet(request.POST)
        # form_items = [(key, value) for key, value in request.POST.items()]
        form_items = [(key, value) for key, value in request.POST.items()]
        print("Form Items:")
        for item in form_items:
            print(item)

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
        prompt_data = TEMPERATURA_PROMPT + " Sanguíneo:" + str(data['count_a']) + " Sanguíneo:" + str(data['count_a'])  + " Colérico" + str(data['count_b']) + " Melancólico" + str(data['count_c']) + " Flemático" + str(data['count_d'])
        ai_response = aiopen.views.send_request(prompt_data)
        return render(request, 'preguntas_result.html', {'data': data, 'ai_response': ai_response, })
        # Do something else after saving the formset
        if formset.is_valid():

            print('SAVE')
        else:
            # Print or log formset errors to see what went wrong
            print(formset.errors)

    else:
        formset = formset_factory(PreguntaForm, extra=40)

    return render(request, 'preguntas_create.html', {'formset': formset, })
