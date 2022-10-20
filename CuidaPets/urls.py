"""CuidaPets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Aqui se especifican las rutas que se pueden visitar.

#"Crear hello world" ahora importo la funcion hello desde myapp a la principal es decir a CuidaPets
from myapp.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    #"Crear Hello wold" ahora indico que cuando se visite la ruta principal, se ejecute la funcion hello que importé.
    path('', hello)
    #"Crear Hello world" Ahora corro el server para ver los cambios (python manage runserver) deberia mostrar "hello world"
]
