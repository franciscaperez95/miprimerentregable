from django.http import HttpResponse
from django.template import Template,Context
import datetime



def familia(request):
    dia=datetime.datetime.today().year
    anio_nacimiento = dia-int(27)
    
    diccionario={"nombre":["Cristian","Daniel","Patricia"],"Rol":["Padre","Hermano","Madre"],"edad":[58,56,30]}

    archivo=open("C:/Users/Francisca Perez/Desktop/cursopython/Proyecto1/Plantillas/template1.html")

    template=Template(archivo.read())
    archivo.close()
    contexto=Context(diccionario)

    documento=template.render(contexto)
    return HttpResponse(documento)