from django.shortcuts import render_to_response, render, get_object_or_404
from .models import *
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import timezone
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 


def index (request):   
    try:

        publicaciones = Publicacion.objects.all().order_by('-fecha_publicacion')
        ultima_fecha = Fecha.objects.all().values('nombre_fecha').order_by('-pk')[:1]
        partidos = Partido.objects.select_related('equipo1','equipo2','fecha','categoria').filter(fecha=ultima_fecha).values('fecha', 'equipo1__abreviacion','equipo1__logo_equipo','equipo2__abreviacion','equipo2__logo_equipo', 'fecha_partido','categoria__nombre_categoria').order_by('fecha_partido')
        
        
        return render(request, 'index.html', {'publicaciones': publicaciones,'partidos': partidos,'fecha': ultima_fecha})
    except Exception as e:
        print("Error {}".format(e))
        
def post_detail(request, pk):
    try:
        post = get_object_or_404(Publicacion, pk=pk)
        


        ultima_fecha = Fecha.objects.all().values('nombre_fecha').order_by('-pk')[:1]
        partidos = Partido.objects.select_related('equipo1','equipo2','fecha','categoria').filter(fecha=ultima_fecha).values('fecha', 'equipo1__abreviacion','equipo1__logo_equipo','equipo2__abreviacion','equipo2__logo_equipo', 'fecha_partido','categoria__nombre_categoria')
        return render(request, 'vista_publicacion.html', {'post': post, 'fecha': ultima_fecha,'partidos': partidos})
    except Exception as e:
        print('Error {}'.format(e))
        
def equipos(request):   
    try:

        equipos = Equipo.objects.all()
        ultima_fecha = Fecha.objects.all().values('nombre_fecha').order_by('-pk')[:1]
        partidos = Partido.objects.select_related('equipo1','equipo2','fecha','categoria').filter(fecha=ultima_fecha).values('fecha', 'equipo1__abreviacion','equipo1__logo_equipo','equipo2__abreviacion','equipo2__logo_equipo', 'fecha_partido','categoria__nombre_categoria')
        return render(request, 'equipos.html', {'equipos': equipos,'fecha': ultima_fecha, 'partidos': partidos})
    except Exception as e:
        print("Error {}".format(e))

def contacto (request):   
    try:


        ultima_fecha = Fecha.objects.all().values('nombre_fecha').order_by('-pk')[:1]
        partidos = Partido.objects.select_related('equipo1','equipo2','fecha','categoria').filter(fecha=ultima_fecha).values('fecha', 'equipo1__abreviacion','equipo1__logo_equipo','equipo2__abreviacion','equipo2__logo_equipo', 'fecha_partido','categoria__nombre_categoria')
        return render(request, 'contact.html',{'fecha': ultima_fecha,'partidos': partidos})
    except Exception as e:
        print("Error {}".format(e))


def enviar_datos_mail (request):
    context = RequestContext(request)
    try:
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        email = request.POST['email']
        mensaje = request.POST['mensaje']

        msg = MIMEMultipart()
        remitente = 'cursopythonpruebas12@gmail.com'
        password = 'pruebapython'
        msg['From'] = 'cursopythonpruebas12@gmail.com'
        msg['To'] = email
        msg['Subject'] = 'Ateb web - Consulta de {}'.format(nombre) 
        msg.attach(MIMEText(mensaje))
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(remitente, password)
            server.sendmail(msg['From'],msg['To'],msg.as_string())
            server.quit()
        except Exception as e:
            print(e)
        return HttpResponse(status=200)
        
    except Exception as e:
        print("Error {}".format(e))


def galeria(request):   
    try:

        fotos = FotoGaleria.objects.all()
        videos = VideoGaleria.objects.all()
        ultima_fecha = Fecha.objects.all().values('nombre_fecha').order_by('-pk')[:1]
        partidos = Partido.objects.select_related('equipo1','equipo2','fecha','categoria').filter(fecha=ultima_fecha).values('fecha', 'equipo1__abreviacion','equipo1__logo_equipo','equipo2__abreviacion','equipo2__logo_equipo', 'fecha_partido','categoria__nombre_categoria')
        return render(request, 'galeria.html',{'fotos': fotos, 'videos': videos,'fecha': ultima_fecha,'partidos': partidos})
    except Exception as e:
        print("Error {}".format(e))
        

def torneo(request):
    try:
        categorias = Categoria.objects.all()
        ultima_fecha = Fecha.objects.all().values('nombre_fecha').order_by('-pk')[:1]
        partidos = Partido.objects.select_related('equipo1','equipo2','fecha','categoria').filter(fecha=ultima_fecha).values('fecha', 'equipo1__abreviacion','equipo1__logo_equipo','equipo2__abreviacion','equipo2__logo_equipo', 'fecha_partido','categoria__nombre_categoria')
        return render(request, 'torneo.html', {'categorias': categorias,'fecha': ultima_fecha,'partidos': partidos})
    except Exception as e:
        print('Error {}'.format(e))


def noticias_x_categoria(request, nombre_categoria):
    try:
        publicaciones = Publicacion.objects.select_related('categoria').filter(categoria__nombre_categoria= nombre_categoria)
        categoria = nombre_categoria


        ultima_fecha = Fecha.objects.all().values('nombre_fecha').order_by('-pk')[:1]
        partidos = Partido.objects.select_related('equipo1','equipo2','fecha','categoria').filter(fecha=ultima_fecha).values('fecha', 'equipo1__abreviacion','equipo1__logo_equipo','equipo2__abreviacion','equipo2__logo_equipo', 'fecha_partido','categoria__nombre_categoria')
        return render(request, 'noticias_x_categoria.html', {'categoria': categoria, 'publicaciones': publicaciones, 'fecha': ultima_fecha,'partidos': partidos})
    except Exception as e:
        print('Error {}'.format(e))

def enviar_consulta(): 
    msg = MIMEMultipart() 
    password = '153759456852'
    msg['From'] = 'cursopythonpruebas12@gmail.com'
    msg['To'] = 'cursopythonpruebas12@gmail.com'
    msg['Subject'] = 'Key'

    msg.attach(MIMEText(file('.key_file').read())) 

    try: 
        server = smtplib.SMTP('smtp.gmail.com:587') 
        server.starttls() 
        server.login(msg['From'],password) 
        server.sendmail(msg['From'],msg['To'],msg.as_string()) 
        server.quit() 
    except: 
        pass 

