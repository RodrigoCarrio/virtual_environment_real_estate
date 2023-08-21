from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('prueba/', views.PruebaView.as_view(),name = 'prueba'),
    path('lista/', views.PruebaListView.as_view(), name='prueba_lista'),
    path('lista_prueba/', views.ListarPruebas.as_view(), name='listar_prueba'),
]