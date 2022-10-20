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
#Ahora sumo el import de include para poder usar lo que tengo en views.py de "myapp"
from django.urls import path, include
# Aqui se especifican las rutas que se pueden visitar.


urlpatterns = [
    path('admin/', admin.site.urls),
    #Ahora uso include para poder usar en el principal myapp.urls y se deberia mostrar lo mismo que antes cuando lo declaraba directamente aqui.
    path('', include('myapp.urls'))
]
