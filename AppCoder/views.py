from django.shortcuts import render
# render es otra forma de cargar templates que veremos en próximas clases
# from django.shortcuts import render

from AppCoder.models import Estudiante
from django.http import HttpResponse
from django.template import loader



def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def about(request):
    return  render(request, 'AppCoder/about.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')