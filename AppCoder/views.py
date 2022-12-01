from django.shortcuts import render
from .models import familia
from django.http import HttpResponse


# Create your views here.
def familia(request):
    dia=datetime.datetime.today().year
    anio_nacimiento = dia-int(27)
    anio_nacimiento.save()
    diccionario={"nombre":["Cristian","Daniel","Patricia"],"Rol":["Padre","Hermano","Madre"],"edad":[58,56,30]}
    diccionario-save()

    return httpResponse (f"Hola soy Francisca, soy la menor y naci el anio {anio_nacimiento}")