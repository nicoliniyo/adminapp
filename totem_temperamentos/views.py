import requests
from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.forms import formset_factory
from rest_framework import viewsets
from .constants import TEMPERATURA_PROMPT, build_prompt
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
        # print('POST CALL')
        form_items = [(key, value) for key, value in request.POST.items()]
        # print("Form Items:")
        # for item in form_items:
        #     print(item)

        formset = PreguntaFormSet(request.POST)
        data = eval_preguntas(request)
        # Print the counts for debugging
        print(data)
        prompt_data = build_prompt(" Sanguíneo:" + str(data['a']) + " Colérico" + str(data['b']) + " Melancólico" + str(data['c']) + " Flemático" + str(data['d']))

        ai_response = aiopen.views.send_request(prompt_data)
        html_ai_response = (ai_response);
        print('CONVERTed html: {0}'.format(html_ai_response))
        return render(request, 'preguntas_result.html',
                      {'data': data, 'ai_response': html_ai_response, })

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


def convert_text_to_html(text):
    """Converts plain text to HTML, adding break lines after certain characters.

    Args:
        text (str): The plain text to convert.

    Returns:
        str: The converted HTML text.
    """

    html = ""
    for char in text:
        if char in ':"':
            html += char + "<br/>"
        elif char == ".":
            html += char + "<br/>"
        else:
            html += char
    return html