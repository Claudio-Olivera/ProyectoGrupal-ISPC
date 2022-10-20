from django.shortcuts import render
# Create your views here.
# Aca definimos que vas a querer mostrar o enviar al cliente , es decir renderiza los archivos html.
def index(request):
    return render (request, 'index.html')
def faq(request):
    return render (request, 'faq.html')
def sobreNosotros(request):
    return render (request, 'sobreNosotros.html')
def cuidadores(request):
    return render (request, 'cuidadores.html')
def contactanos(request):
    return render (request, 'contactanos.html')


