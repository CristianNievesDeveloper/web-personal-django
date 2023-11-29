# Importa la función 'render' del módulo 'django.shortcuts' para renderizar las plantillas HTML.
from django.shortcuts import render

# from django.views.decorators.csrf import csrf_protect


# Importa el modelo 'Project' desde el archivo models.py de la misma aplicación.
from .models import Project


# Define una vista llamada 'home' que tomará una solicitud ('request') como argumento.
def home(request):
    # Recupera todos los objetos 'Project' de la base de datos.
    projects = Project.objects.all()

    # Renderiza la plantilla 'home.html' y pasa los proyectos recuperados como contexto a la plantilla.
    return render(request, 'home.html', {'projects': projects})


def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'projects.html',{'projects': projects})


def handling_404(request, exception):
    return render(request,'404.html',{})


def custom_500(request):
    return render(request, '500.html', status=500)

def hello_word(request):
    raise Exception('error 500')