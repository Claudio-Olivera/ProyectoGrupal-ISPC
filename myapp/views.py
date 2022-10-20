from django.shortcuts import render
# Create your views here.
# Aca definimos que vas a querer mostrar o enviar al cliente , es decir renderiza los archivos html.

#"Hacer un hello world": importo HttpResponse
from django.http import HttpResponse
def hello(request):
    return HttpResponse ("<h1>Hello World</h1>")
#Ahora necesito dirigirme a CuidaPets(que es el principal) e indicar en el archivo urls.py en la seccion urlpatterns la funcion "hello" que acabo de crear 


