from django.contrib import admin

# Register your models here.
from totem_temperamentos.models import Organizacion, Pregunta, Prueba, Prueba_resultado
# , Prueba, Pregunta, Prueba_resultado)

admin.site.register(Organizacion)
admin.site.register(Prueba)
admin.site.register(Pregunta)
admin.site.register(Prueba_resultado)
admin.site.site_header = "Totem Temperamentos"
