from django.contrib import admin

# Register your models here.
from actividades.models import Actividad

admin.site.register(Actividad)

admin.site.site_header = "Actividades Admin"