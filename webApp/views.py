from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
# Importo settings para poder usar una variable del archivo settings.py
from django.conf import settings

def saludo(request):
    return HttpResponse('Bienvenido!')

def segunda_vista(request):
    return HttpResponse('<br><br>/a entendimos esto, es muy simple :)')

def diaDeHoy(request):
    dia = datetime.now()
    documentoDeTexto = f'Hoy es el dia: <br> {dia}'
    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentoDeTexto = f'Mi nombre es: <br><br> {nombre}' 
    return HttpResponse(documentoDeTexto)

def probandoTemplates(self):

    name = 'Matias'

    lastname = 'Viaggio'

    diahoy = datetime.now() 

    miLista = ['nota1', 'nota2', 'nota3']

    diccionario = {'nombre':name, 'apellido':lastname, 'fechaActual':diahoy, 'nota':miLista}

    
    # miHtml = open('C:/Users/matia/Documents/.python/project1/webApp/plantillas1/pTemplates.html')
    # plantilla = Template(miHtml.read())
    # miHtml.close()
    plantilla = loader.get_template('pTemplates.html')
    # miContexto = Context(diccionario)
    # documento = plantilla.render(miContexto)
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

