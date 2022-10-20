from django.apps import AppConfig

#Lo mismo que settings.py pero para este project "myapp"

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
