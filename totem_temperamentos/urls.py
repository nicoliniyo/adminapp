from django.urls import path
from . import views

urlpatterns = [

  path('', views.pregunta_list, name='pregunta_list'),
  path('create/', views.create_preguntas, name='pregunta_create'),

]