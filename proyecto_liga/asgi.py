'''
Universidad de la Laguna
Proyecto: Footdata
Autor: Edgar Negrín Gonzalez
Email: alu0101210964@ull.edu.es
Fichero: asgi.py: Este fichero contiene la
implementación de la interfaz de aplicaciones de puerta de enlace asíncrona
'''

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_liga.settings')

application = get_asgi_application()
