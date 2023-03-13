'''
Universidad de la Laguna
Proyecto: Footdata
Autor: Edgar Negrín Gonzalez
Email: alu0101210964@ull.edu.es
Fichero: urls.py: Este fichero contiene las
definiciones de las rutas URL de la aplicación y las asignaciones de vistas
'''
from django.contrib import admin
from django.urls import path
from tracker_liga.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('insertar',insertar),
    path('insertar_partidos',insertar_partidos),
    path('eliminar',eliminar),
    path('partidos',partidos),
    path('prediccion',prediccion),
    path('equipos',equipos),
    path('plot_edad1',plot_edad1),
    path('plot_edad2',plot_edad2),
    path('plot_posesion1',plot_posesion1),
    path('plot_posesion2',plot_posesion2),
    path('plot_goles1',plot_goles1),
    path('plot_goles2',plot_goles2),
    path('plot_asistencias1',plot_asistencias1),
    path('plot_asistencias2',plot_asistencias2),
    path('plot_goles_esperados1',plot_goles_esperados1),
    path('plot_goles_esperados2',plot_goles_esperados2),
    path('plot_conducciones1',plot_conducciones1),
    path('plot_conducciones2',plot_conducciones2),
    path('plot_pases_progresivos1',plot_pases_progresivos1),	
    path('plot_pases_progresivos2',plot_pases_progresivos2),
    path('plot_prediccion',plot_prediccion)
]
