from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    partidos_jugados = models.IntegerField(default=0) # Cambiarlo porque esta mal escrito
    edad_media = models.FloatField(default=0.0)
    posesion = models.FloatField(default=0.0)
    goles_favor = models.IntegerField(default=0)
    asistencias = models.IntegerField(default=0)
    tarjeta_amarilla = models.IntegerField(default=0)
    tarjeta_roja = models.IntegerField(default=0)
    goles_esperados = models.FloatField(default=0.0)
    conducciones = models.IntegerField(default=0)
    pases_progresivos = models.IntegerField(default=0)
    goles_partido = models.FloatField(default=0.0)
    asistencias_partido = models.FloatField(default=0.0)
    goles_esperados_partido = models.FloatField(default=0.0)
    liga = models.CharField(max_length=50, default='null')
    fecha = models.CharField(max_length=50, default='null')
    genero = models.CharField(max_length=50, default='null')

    def __str__(self):
        return self.nombre
    

class Partido(models.Model):
    equipo_local = models.CharField(max_length=50, default='null')
    goles_local_esperados = models.FloatField(default=0.0)
    marcador = models.CharField(max_length=50, default='null')
    goles_visitante_esperados = models.FloatField(default=0.0)
    equipo_visitante = models.CharField(max_length=50, default='null')
    
    def __str__(self):
        return self.equipo_local + ' vs ' + self.equipo_visitante
    
class Enfrentamientos(models.Model):
    resultado = models.CharField(max_length=50, default='null')
    goles_favor = models.CharField(max_length=50, default='null')
    goles_contra = models.CharField(max_length=50, default='null')
    adversario = models.CharField(max_length=50, default='null')
    goles_esperados_favor = models.CharField(max_length=50, default='null')
    goles_esperados_contra = models.CharField(max_length=50, default='null')
    posesion = models.CharField(max_length=50, default='null')
    fecha = models.CharField(max_length=50, default='null')
    liga = models.CharField(max_length=50, default='null')
    genero = models.CharField(max_length=50, default='null')
    equipo = models.CharField(max_length=50, default='null')