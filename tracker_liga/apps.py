'''
Universidad de la Laguna
Proyecto: Footdata
Autor: Edgar Negrín Gonzalez
Email: alu0101210964@ull.edu.es
Fichero: apps.py: Este fichero contiene la
configuración y presonalización de la aplicación
'''
from django.apps import AppConfig


class TrackerLigaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tracker_liga'
