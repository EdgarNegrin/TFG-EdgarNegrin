'''
Universidad de la Laguna
Proyecto: Footdata
Autor: Edgar Negrín Gonzalez
Email: alu0101210964@ull.edu.es
Fichero: models.py: Este fichero contiene los
modelos de la base de datos
'''
from django.db import models

#
# Descripcion: Modelo de la tabla Equipo
#
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
    
#
# Descripcion: Modelo de la tabla Partido
#
class Partido(models.Model):
    temporada = models.CharField(max_length=50, default='null')
    fecha = models.CharField(max_length=50, default='null')
    equipo_local = models.CharField(max_length=50, default='null')
    equipo_visitante = models.CharField(max_length=50, default='null')
    FTHG = models.CharField(max_length=50, default='null')
    FTAG = models.CharField(max_length=50, default='null')
    FTR = models.CharField(max_length=50, default='null')
    HTHG = models.CharField(max_length=50, default='null')
    HTAG = models.CharField(max_length=50, default='null')
    HTR = models.CharField(max_length=50, default='null')
    
    def __str__(self):
        return self.equipo_local + ' vs ' + self.equipo_visitante
    