# encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


PRIORIDAD = (
    ('0', 'Baja'),
    ('1', 'Media'),
    ('2', 'Alta'),
)

ESTADO = (
          ('0', 'No Iniciada'),
          ('1', 'En Proceso'),
          ('2', 'Completada'),
          )

# Create your models here.
class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, null=False)
    fechaInicio = models.DateField(null=False)
    fechaFin = models.DateField(null=False)
    def __unicode__(self): 
        return self.nombre
    
class Sprint(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    fechaInicio = models.DateField(null=False)
    fechaFin = models.DateField(null=False)
    dedicacionMax = models.IntegerField(default=0, null=False)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=False)
    def __unicode__(self): 
        return self.nombre

class HistoriasUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, null=False)  
    prioridad = models.CharField(max_length=1, choices=PRIORIDAD, null=False) 
    estimacion = models.IntegerField(null=False);
    criterios_validacion = models.TextField()
    descripcion = models.TextField(default="Describa el caso de uso", null=False)
    def __unicode__(self):
        return self.nombre

class Tareas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    estado = models.CharField(max_length=1, choices=ESTADO, null=False)
    dedicacion = models.IntegerField(default=0, null=False)
    historia_usuario = models.ForeignKey(HistoriasUsuario, on_delete=models.CASCADE, null=False)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, null=True)
    def __unicode__(self):
        return self.nombre

class DailyScrum(models.Model):
    id = models.AutoField(primary_key=True)
    asunto = models.CharField(max_length=100, null=False)
    horaInicio = models.TimeField(null=False)
    duracion = models.IntegerField(null=False)
    conclusiones = models.TextField(default="Conclusiones de la reunion", null=False)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, null=False)
    def __unicode__(self):
        return self.asunto
    
class SprintReview(models.Model):
    id = models.AutoField(primary_key=True)
    horaInicio = models.TimeField(null=False)
    duracion = models.IntegerField(null=False)
    propuesta = models.TextField(default="Propuesta", null=False)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    
class Retrospectiva(models.Model):
    id = models.AutoField(primary_key=True)
    asunto = models.CharField(max_length=100, null=False)
    fechaInicio = models.DateField(null=False);
    duracion_maxima = models.IntegerField(null=False)
    acciones_mejora = models.TextField(default="Acciones de mejora", null=False)
    def __unicode__(self):
        return self.asunto
    
class TareasSpringReview(models.Model):
    springReview = models.ForeignKey(SprintReview, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    tareas_realizadas = models.TextField(default="Tareas realizadas", null=False)
    tareas_no_realizadas = models.TextField(null=False, blank=True)
    propuesta_fecha_fin = models.DateField()
    
class TareasDailyScrum(models.Model):
    dailyScrum = models.ForeignKey(DailyScrum, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    tareas_realizadas = models.TextField(null=False)
    tareas_futuras = models.TextField(null=False)
    obstaculos = models.TextField()
    


    
    
    
    
    

