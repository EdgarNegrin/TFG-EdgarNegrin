"""proyecto_liga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
    path('prediccion/',prediccion),
    path('equipos/',equipos),
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
