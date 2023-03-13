'''
Universidad de la Laguna
Proyecto: Footdata
Autor: Edgar Negrín Gonzalez
Email: alu0101210964@ull.edu.es
Fichero: dataManager.py: Este fichero contiene la
implementación de las funciones necesarias para modificar la base de datos
'''
import sqlite3

#
# Descripcion: Esta función se encarga de conectar con la base de datos
# Parametros: 
# Return: conexion(sqlite3.connect): Conexión con la base de datos, cursor(sqlite3.cursor): Cursor de la base de datos
#
def conectar():
  conexion = sqlite3.connect("db.sqlite3")
  cursor = conexion.cursor()
  return conexion, cursor

#
# Descripcion: Esta función se encarga de leer el fichero para insertarlo en la base de datos
# Parametros: fichero(str): Nombre del fichero
# Return: file(list): Lista con los datos del fichero
#
def abrirFichero(fichero):
  openFile = open(fichero, 'r', encoding='utf-8')
  file = []
  liga = []
  liga = openFile.readline().split(',') # liga, año, femenino/masculino
  liga[-1] = liga[-1].replace('\n','')
  lineas = openFile.readlines()
  for linea in lineas:
    file.append(linea.split(',')) # ["madrid", "4", "5", "6"] 
    file[-1] = file[-1] + liga

  openFile.close()
  return file

#
# Descripcion: Esta función se encarga de insertar los datos del fichero en la base de datos
# Parametros: conexion(sqlite3.connect): Conexión con la base de datos, cursor(sqlite3.cursor): Cursor de la base de datos, fichero(list): Lista con los datos del fichero
# Return: 
#
def insertarFicheroEquipo(conexion, cursor, fichero):
  sentencia = "INSERT INTO tracker_liga_equipo (id, nombre, edad_media, posesion, partidos_jugados, goles_favor, asistencias, tarjeta_amarilla, tarjeta_roja, goles_esperados, conducciones, pases_progresivos, goles_partido, asistencias_partido, goles_esperados_partido, liga, fecha, genero) VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
  cursor.executemany(sentencia, fichero)
  conexion.commit()
  conexion.close()

#
# Descripcion: Esta función se encarga de insertar los datos del fichero en la base de datos
# Parametros: conexion(sqlite3.connect): Conexión con la base de datos, cursor(sqlite3.cursor): Cursor de la base de datos, fichero(list): Lista con los datos del fichero
# Return: 
#
def insertarFicheroPartido(conexion, cursor, fichero):
  sentencia = "INSERT INTO tracker_liga_partido (id, equipo_local, goles_local_esperados, marcador, goles_visitante_esperados, equipo_visitante) VALUES (NULL,?,?,?,?,?)"
  cursor.executemany(sentencia, fichero)
  conexion.commit()
  conexion.close()

#
# Descripcion: Esta función se encarga de eliminar los datos en la base de datos
# Parametros: conexion(sqlite3.connect): Conexión con la base de datos, cursor(sqlite3.cursor): Cursor de la base de datos
# Return: 
#
def eliminarTabla(conexion, cursor):
  sentencia = "DELETE FROM tracker_liga_enfrentamientos"
  cursor.execute(sentencia)
  conexion.commit()
  conexion.close()

#
# Descripcion: Esta función se encarga de leer los datos en la base de datos
# Parametros: conexion(sqlite3.connect): Conexión con la base de datos, cursor(sqlite3.cursor): Cursor de la base de datos
# Return: 
#
def leer_Equipos(conexion, cursor):
  sentencia = "SELECT * FROM tracker_liga_equipo"
  cursor.execute(sentencia)
  equipos = cursor.fetchall()
  conexion.close()
  return equipos

#
# Descripcion: Esta función se encarga de leer los datos en la base de datos
# Parametros: conexion(sqlite3.connect): Conexión con la base de datos, cursor(sqlite3.cursor): Cursor de la base de datos
# Return: 
#
def leer_ligas(conexion, cursor):
  sentencia = "SELECT DISTINCT liga, genero, fecha FROM tracker_liga_equipo"
  cursor.execute(sentencia)
  equipos = cursor.fetchall()
  conexion.close()
  return equipos
