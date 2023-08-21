from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

#importo el modelo
from .models import Prueba

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class PruebaListView(ListView):
    template_name = 'home/lista.html'
    context_object_name = 'lista'
    queryset = ['0','1','2','3']

class ListarPruebas(ListView):
    template_name = 'home/lista_prueba.html'
    model = Prueba
    context_object_name = 'lista'
    