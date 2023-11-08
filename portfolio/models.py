# Importa la clase models del módulo django.db, que se utiliza para definir modelos de base de datos en Django
from django.db import models

# Define un nuevo modelo llamado Project que hereda de models.Model, lo que significa que será un modelo de base de datos
class Project(models.Model):
    # Define un campo de texto llamado 'title' que puede contener hasta 100 caracteres. Se utiliza para el título del proyecto.
    title = models.CharField(max_length=100)

    # Define un campo de texto llamado 'description' que puede contener hasta 250 caracteres. Se utiliza para una descripción breve del proyecto.
    description = models.TextField()

    # Define un campo de imagen llamado 'image' que se utilizará para almacenar la imagen asociada al proyecto.
    # La opción 'upload_to' especifica la subcarpeta dentro de la carpeta de medios (media) donde se almacenarán las imágenes cargadas.
    image = models.ImageField(upload_to="portfolio/images/")
    
    tecno = models.CharField(max_length=250,default="Sin especificar")

    # Define un campo de URL llamado 'url' que puede estar en blanco (opcional). Se utiliza para almacenar una URL relacionada con el proyecto, como un enlace a la página del proyecto.
    url = models.URLField(blank=True)
    
    github = models.URLField(blank=True)