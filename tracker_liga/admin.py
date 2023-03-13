'''
Universidad de la Laguna
Proyecto: Footdata
Autor: Edgar Negrín Gonzalez
Email: alu0101210964@ull.edu.es
Fichero: admin.py: Este fichero contiene la
definicion de la configuracion del panel administrador
'''

from django.contrib import admin
from .models import Equipo, Partido

admin.site.register(Equipo)