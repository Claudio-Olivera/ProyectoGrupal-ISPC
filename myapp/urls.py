#Creacion de urls.py para no tener que importar todo al main, pero ahora necesito hacer include en urls.py del principal.
#import de path
from django.urls import path
#import de la misma ubicacion el modulo views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('faq/', views.faq, name="faq"),
    path('sobreNosotros/', views.sobreNosotros, name="sobreNosotros"),
    path('cuidadores/', views.cuidadores, name="cuidadores"),
    path('contactanos/', views.contactanos, name="contactanos")
]