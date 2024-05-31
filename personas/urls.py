from django.urls import path
from . import views

urlpatterns = [

  path('', views.persona_list, name='persona_list'),
  path('create/', views.persona_create, name='persona_create'),
  path('<pk>/update/', views.persona_update, name='persona_update'),
  path('<pk>/delete/', views.persona_delete, name='persona_delete'),

]