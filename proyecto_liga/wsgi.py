'''
Universidad de la Laguna
Proyecto: Footdata
Autor: Edgar Negrín Gonzalez
Email: alu0101210964@ull.edu.es
Fichero: wsgi.py: Este fichero contiene la
implementación de la interfaz de servidor de puerta de enlace interfaz web
'''

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_liga.settings')

application = get_wsgi_application()
