from rest_framework import serializers
from .models import (Organizacion, Pregunta, Prueba, Prueba_resultado)
#, , Prueba, Prueba_resultado)

class OrganizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = '__all__'

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'

class Prueba_resultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prueba_resultado
        fields = '__all__'


class PruebaSerializer(serializers.ModelSerializer):
    resultados = serializers.SerializerMethodField()

    class Meta:
        model = Prueba
        fields = '__all__'

    def get_resultados(self, obj):
        resultados = Prueba_resultado.objects.filter(prueba_nro=obj.id)
        serializer = Prueba_resultadoSerializer(resultados, many=True)
        return serializer.data

