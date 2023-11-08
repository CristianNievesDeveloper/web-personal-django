"""
URL configuration for django_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# Importa la clase 'admin' del módulo 'django.contrib' para habilitar la interfaz de administración de Django.
from django.contrib import admin
# Importa la función 'path' del módulo 'django.urls' para definir las rutas de URL en tu aplicación.
from django.urls import path
# Importa las funciones 'static' y 'settings' para manejar archivos estáticos y multimedia en tu aplicación.
from django.conf.urls.static import static
from django.conf import settings

# Importa las vistas desde la aplicación 'portfolio'.
from portfolio import views
from enviaemail.views import contact


# Define las URL de tu aplicación.
urlpatterns = [
    # Define la URL para acceder a la interfaz de administración de Django.
    path('admin/', admin.site.urls),
    # Define una URL vacía como la página de inicio de tu aplicación, utilizando la vista 'home' de la aplicación 'portfolio'.
    path('', views.home, name='home'),
    path('projects/', views.projects_view, name='projects_view'),
    path('contact/', contact, name='contact'),  # Agrega esta línea
    
]

# Agrega la configuración para servir archivos multimedia (archivos cargados) durante el desarrollo.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

