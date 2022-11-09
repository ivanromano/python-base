from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=250)

class Tarea(models.Model):
    tittle = models.CharField(max_length=200)
    descripcion = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
