from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipo, Partido, Enfrentamientos
from insertarDB import insertarFicheroEquipo, insertarFicheroPartido, insertarFicheroEnfrentamiento, eliminarTabla, conectar, abrirFichero
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
import io
from IA import *

# Create your views here.
def home(request):
    equipos = Equipo.objects.all()
    return render(request, 'app/home.html')

def partidos(request):
    return render(request, 'app/partidos.html', {'partidos': Enfrentamientos.objects.all()})

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

def insertar(request):
    con, cursor = conectar()
    fichero = abrirFichero('Datos/ligas/datosSuperLeague2122.txt')
    insertarFicheroEquipo(con, cursor, fichero)
    return HttpResponse('Datos insertados')

def eliminar(request):
    con, cursor = conectar()
    eliminarTabla(con, cursor)
    return HttpResponse('Datos eliminados')

def prediccion(request):
    datos([(partido.equipo, partido.adversario, partido.goles_favor, partido.goles_contra, partido.resultado) for partido in Enfrentamientos.objects.all()])
    return render(request, 'app/prediccion.html')

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


# Creacion de imagenes de los graficos

def grafico_edad(fecha, liga, genero):
    #Datos a representar
    x = [equipo.nombre for equipo in Equipo.objects.filter(fecha=fecha,liga=liga,genero=genero)]
    y = [equipo.edad_media for equipo in Equipo.objects.filter(fecha=fecha,liga=liga,genero=genero)]

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    
    
    axes = f.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.scatter(x,y)
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

    # Limpiamos la figura para liberar memoria
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    return response

def grafico_posesion(fecha, liga, genero):
    #Datos a representar
    x = [equipo.nombre for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]
    y = [equipo.posesion for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    
    axes = f.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.scatter(x,y)
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

def grafico_goles(fecha, liga, genero):
    #Datos a representar
    x = [equipo.nombre for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]
    y = [equipo.goles_favor for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    
    axes = f.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.scatter(x,y)
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

def grafico_asistencias(fecha, liga, genero):
    #Datos a representar
    x = [equipo.nombre for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]
    y = [equipo.asistencias for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    
    axes = f.add_axes([0.1, 0.1, 0.8, 0.8])
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

def grafico_goles_esperados(fecha, liga, genero):
    #Datos a representar
    x = [equipo.nombre for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]
    y = [equipo.goles_esperados for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    
    axes = f.add_axes([0.1, 0.1, 0.8, 0.8])
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

def grafico_conducciones(fecha, liga, genero):
    #Datos a representar
    x = [equipo.nombre for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]
    y = [equipo.conducciones for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    
    axes = f.add_axes([0.1, 0.1, 0.8, 0.8])
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

def grafico_pases_progresivos(fecha, liga, genero):
    #Datos a representar
    x = [equipo.nombre for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]
    y = [equipo.pases_progresivos for equipo in Equipo.objects.filter(fecha=fecha, liga=liga,genero=genero)]

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    
    axes = f.add_axes([0.1, 0.1, 0.8, 0.8])
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
