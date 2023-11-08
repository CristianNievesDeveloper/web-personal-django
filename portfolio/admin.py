# Importa la clase 'admin' del módulo 'django.contrib', que se utiliza para configurar la interfaz de administración de Django.
from django.contrib import admin

# Importa el modelo 'Project' desde el archivo models.py de la misma aplicación.
from .models import Project

# Registra el modelo 'Project' en el panel de administración de Django para que puedas gestionar y editar instancias de este modelo a través de la interfaz de administración.
admin.site.register(Project)