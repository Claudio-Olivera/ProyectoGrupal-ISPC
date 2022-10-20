from django.shortcuts import render
# Create your views here.
# Aca definimos que vas a querer mostrar o enviar al cliente , es decir renderiza los archivos html.

#"Hacer un hello world": importo HttpResponse
from django.http import HttpResponse
def hello(request):
    return HttpResponse ("<h1>Hello World</h1>")



