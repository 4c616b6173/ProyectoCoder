from django.shortcuts import render
# render es otra forma de cargar templates que veremos en próximas clases
# from django.shortcuts import render

from AppCoder.models import Estudiante, Curso
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import CursoFormulario




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


def cursoFormulario(request):

    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'], duracion=informacion['duracion'])

            curso.save()

            return render(request, "AppCoder/inicio.html")
        
    else:

        miFormulario = CursoFormulario()

    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})