'''
Universidad de la Laguna
Proyecto: Footdata
Autor: Edgar Negrín Gonzalez
Email: alu0101210964@ull.edu.es
Fichero: views.py: Este fichero contiene la
implementación de las vistas de la aplicación
'''

from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipo, Partido
from dataManager import insertarFicheroEquipo, eliminarTabla, conectar, abrirFichero, leer_ligas
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
import io
import csv
from machinelearning import *

#
# Descripcion: Esta función se encarga crear la vista home
# Parametros: request: Petición del usuario
# Return: Renderiza la vista home
#
def home(request):
    con, cursor = conectar()
    ligas = leer_ligas(con, cursor)
    equipos = Equipo.objects.all()
    return render(request, 'app/home.html', {'equipos': equipos, 'ligas': ligas})

#
# Descripcion: Esta función se encarga crear la vista partidos
# Parametros: request: Petición del usuario
# Return: Renderiza la vista partidos
#
def partidos(request):
    temporada = request.GET.get('temporada')
    partidos_filtrados = Partido.objects.filter(temporada=temporada)
    return render(request, 'app/partidos.html', {'partidos': partidos_filtrados, 'fecha': temporada})

#
# Descripcion: Esta función se encarga crear la vista equipos
# Parametros: request: Petición del usuario
# Return: Renderiza la vista equipos
#
def equipos(request):
    global Gtemporada 
    global Gliga
    global Ggenero
    global Gtemporada2 
    global Gliga2
    global Ggenero2
    Gtemporada = request.GET.get('temporada')
    Gliga = request.GET.get('liga')
    Ggenero = request.GET.get('genero')
    Gtemporada2 = request.GET.get('temporada2')
    Gliga2 = request.GET.get('liga2')
    Ggenero2 = request.GET.get('genero2')
    return render(request, 'app/equipos.html', {'equipos': Equipo.objects.all()})

#
# Descripcion: Esta función se encarga crear la vista insertar
# Parametros: request: Petición del usuario
# Return: Renderiza la vista insertar
#
def insertar(request):
    con, cursor = conectar()
    fichero = abrirFichero('Datos/ligas/datosSuperLeague2122.txt')
    insertarFicheroEquipo(con, cursor, fichero)
    return HttpResponse('Datos insertados')

#
# Descripcion: Esta función se encarga crear la vista insertar_partidos
# Parametros: request: Petición del usuario
# Return: Renderiza la vista insertar_partidos
#
def insertar_partidos(request):
    con, cursor = conectar()
    with open('Datos/prediccion/LaLiga_Matches_1995-2021.csv') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['Season'], i['Date'], i['HomeTeam'], i['AwayTeam'], i['FTHG'], i['FTAG'], i['FTR'], i['HTHG'], i['HTAG'], i['HTR']) for i in dr]
    cursor.executemany("INSERT INTO tracker_liga_partido (id, temporada, fecha, equipo_local, equipo_visitante, FTHG, FTAG, FTR, HTHG, HTAG, HTR) VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    con.commit()
    con.close()
    return HttpResponse('Datos insertados')

#
# Descripcion: Esta función se encarga crear la vista eliminar
# Parametros: request: Petición del usuario
# Return: Renderiza la vista eliminar
#
def eliminar(request):
    con, cursor = conectar()
    eliminarTabla(con, cursor)
    return HttpResponse('Datos eliminados')

#
# Descripcion: Esta función se encarga crear la vista prediccion
# Parametros: request: Petición del usuario
# Return: Renderiza la vista prediccion
#
def prediccion(request):
    equipo_local = request.GET.get('local')
    equipo_visitante = request.GET.get('visitante')
    fecha = request.GET.get('fecha')
    
    modelo, lb_make_outs, equipos_nombre, precicion = crear_modelo()
    dataframe = pd.DataFrame(
        {
            'HomeTeam': [equipo_local],
            'AwayTeam': [equipo_visitante],
            'Date': [fecha]
        }
    )
    prediccion = crear_prediccion(dataframe, modelo, lb_make_outs, equipos_nombre)
    if (prediccion[0][0] == 'H'):
        resultado = 'Victoria para ' + equipo_local
    else:
        if (prediccion[0][0] == 'D'):
            resultado = 'Empate'
        else:
            resultado = 'Victoria para ' + equipo_visitante
    
    return render(request, 'app/prediccion.html', {'resultado': resultado, 'precicion': precicion, 'equipos': equipos_nombre, 'equipo_local': equipo_local, 'equipo_visitante': equipo_visitante})

#
# Descripcion: Estas funciones se encargan de crear los gráficos de la vista equipos dependiendo de los filtros
# Parametros: request: Petición del usuario
# Return: (HttpResponse)Devuelve la vista de la grafica
#
def plot_edad1(request):
    return grafico_edad(Gtemporada, Gliga, Ggenero)

def plot_posesion1(request):
    return grafico_posesion(Gtemporada, Gliga, Ggenero)

def plot_goles1(request):
    return grafico_goles(Gtemporada, Gliga, Ggenero)

def plot_asistencias1(request):
    return grafico_asistencias(Gtemporada, Gliga, Ggenero)

def plot_goles_esperados1(request):
    return grafico_goles_esperados(Gtemporada, Gliga, Ggenero)

def plot_conducciones1(request):
    return grafico_conducciones(Gtemporada, Gliga, Ggenero)

def plot_pases_progresivos1(request):
    return grafico_pases_progresivos(Gtemporada, Gliga, Ggenero)

def plot_edad2(request):
    return grafico_edad(Gtemporada2, Gliga2, Ggenero2)

def plot_posesion2(request):
    return grafico_posesion(Gtemporada2, Gliga2, Ggenero2)

def plot_goles2(request):
    return grafico_goles(Gtemporada2, Gliga2, Ggenero2)

def plot_asistencias2(request):
    return grafico_asistencias(Gtemporada2, Gliga2, Ggenero2)

def plot_goles_esperados2(request):
    return grafico_goles_esperados(Gtemporada2, Gliga2, Ggenero2)

def plot_conducciones2(request):
    return grafico_conducciones(Gtemporada2, Gliga2, Ggenero2)

def plot_pases_progresivos2(request):
    return grafico_pases_progresivos(Gtemporada2, Gliga2, Ggenero2)

#
# Descripcion: Esta función se encarga crear el gráfico de predicción
# Parametros: request: Petición del usuario
# Return: response(HttpResponse): Devuelve la vista de la grafica
#
def plot_prediccion(request):
    num_partidos, num_local, num_empate, num_visitante = informacion_dataframe()
    
    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    
    axes = f.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.pie([num_local, num_visitante, num_empate], labels=['Local', 'Visitante', 'Empate'], autopct='%1.1f%%')
    f.autofmt_xdate(rotation=45)
    axes.set_title("Total de resultados del dataset con " + str(num_partidos) + " partidos")

    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Limpiamos la figura para liberar memoria
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    return response

#
# Descripcion: Esta función se encarga crear el gráfico de edad
# Parametros: fecha: Fecha de la liga, liga: Liga, genero: Genero
# Return: response(HttpResponse): Devuelve la vista de la grafica
#
def grafico_edad(fecha, liga, genero):
    #Datos a representar
    x = [equipo.nombre for equipo in Equipo.objects.filter(fecha=fecha,liga=liga,genero=genero)]
    y = [equipo.edad_media for equipo in Equipo.objects.filter(fecha=fecha,liga=liga,genero=genero)]

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    
    
    axes = f.add_axes([0.2, 0.2, 0.8, 0.8])
    axes.plot(x,y)
    f.autofmt_xdate(rotation=45)
    axes.set_xlabel("")
    axes.set_ylabel("Edad media")
    axes.set_title(fecha + " " + liga + " " + genero)

    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    return response

#
# Descripcion: Esta función se encarga crear el gráfico de posesion
# Parametros: fecha: Fecha de la liga, liga: Liga, genero: Genero
# Return: response(HttpResponse): Devuelve la vista de la grafica
#
def grafico_posesion(fecha, liga, genero):
    #Datos a representar
    x = [equipo.nombre for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]
    y = [equipo.posesion for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    
    axes = f.add_axes([0.2, 0.2, 0.8, 0.8])
    axes.bar(x,y)
    f.autofmt_xdate(rotation=45)
    axes.set_xlabel("")
    axes.set_ylabel("Posesion %")
    axes.set_title(fecha + " " + liga + " " + genero)

    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Limpiamos la figura para liberar memoria
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    return response

#
# Descripcion: Esta función se encarga crear el gráfico de goles
# Parametros: fecha: Fecha de la liga, liga: Liga, genero: Genero
# Return: response(HttpResponse): Devuelve la vista de la grafica
#
def grafico_goles(fecha, liga, genero):
    #Datos a representar
    x = [equipo.nombre for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]
    y = [equipo.goles_favor for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    
    axes = f.add_axes([0.2, 0.2, 0.8, 0.8])
    axes.bar(x,y)
    f.autofmt_xdate(rotation=45)
    axes.set_xlabel("")
    axes.set_ylabel("Goles a favor")
    axes.set_title(fecha + " " + liga + " " + genero)

    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Limpiamos la figura para liberar memoria
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    return response

#
# Descripcion: Esta función se encarga crear el gráfico de asistencias
# Parametros: fecha: Fecha de la liga, liga: Liga, genero: Genero
# Return: response(HttpResponse): Devuelve la vista de la grafica
#
def grafico_asistencias(fecha, liga, genero):
    #Datos a representar
    x = [equipo.nombre for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]
    y = [equipo.asistencias for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    
    axes = f.add_axes([0.2, 0.2, 0.8, 0.8])
    axes.scatter(x,y)
    f.autofmt_xdate(rotation=45)
    axes.set_xlabel("")
    axes.set_ylabel("Asistencias")
    axes.set_title(fecha + " " + liga + " " + genero)

    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Limpiamos la figura para liberar memoria
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    return response

#
# Descripcion: Esta función se encarga crear el gráfico de goles esperados
# Parametros: fecha: Fecha de la liga, liga: Liga, genero: Genero
# Return: response(HttpResponse): Devuelve la vista de la grafica
#
def grafico_goles_esperados(fecha, liga, genero):
    #Datos a representar
    x = [equipo.nombre for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]
    y = [equipo.goles_esperados for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    
    axes = f.add_axes([0.2, 0.2, 0.8, 0.8])
    axes.scatter(x,y)
    f.autofmt_xdate(rotation=45)
    axes.set_xlabel("")
    axes.set_ylabel("Goles esperados")
    axes.set_title(fecha + " " + liga + " " + genero)

    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Limpiamos la figura para liberar memoria
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    return response

#
# Descripcion: Esta función se encarga crear el gráfico de conducciones
# Parametros: fecha: Fecha de la liga, liga: Liga, genero: Genero
# Return: response(HttpResponse): Devuelve la vista de la grafica
#
def grafico_conducciones(fecha, liga, genero):
    #Datos a representar
    x = [equipo.nombre for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]
    y = [equipo.conducciones for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    
    axes = f.add_axes([0.2, 0.2, 0.8, 0.8])
    axes.scatter(x,y)
    f.autofmt_xdate(rotation=45)
    axes.set_xlabel("")
    axes.set_ylabel("Conducciones progresivas")
    axes.set_title(fecha + " " + liga + " " + genero)

    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Limpiamos la figura para liberar memoria
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    return response

#
# Descripcion: Esta función se encarga crear el gráfico de pases progresivos
# Parametros: fecha: Fecha de la liga, liga: Liga, genero: Genero
# Return: response(HttpResponse): Devuelve la vista de la grafica
#
def grafico_pases_progresivos(fecha, liga, genero):
    #Datos a representar
    x = [equipo.nombre for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]
    y = [equipo.pases_progresivos for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    
    axes = f.add_axes([0.2, 0.2, 0.8, 0.8])
    axes.scatter(x,y)
    f.autofmt_xdate(rotation=45)
    axes.set_xlabel("")
    axes.set_ylabel("Pases progresivos")
    axes.set_title(fecha + " " + liga + " " + genero)

    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Limpiamos la figura para liberar memoria
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    return response
