# -*- encoding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from heuristica.models import Perfil
from heuristica.models import Juegos
from heuristica.models import Heuristica
from heuristica.models import MiTest
from heuristica.models import Asignados
from heuristica.models import Resultados
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.core.validators import validate_slug, RegexValidator
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
from django.core import serializers
import json


#cosas chorras para las prácticas de SSBW se podran borrar algunas excepto las marcadas
from lxml import etree
import requests
from pymongo import MongoClient
# Create your views here.




# cosas de las practicas de SSBW que se podrán borrar
def google (request):
    tree = etree.parse ('http://maps.googleapis.com/maps/api/geocode/xml?address=daniel%20saucedo%20aranda%20granada')
    imagenes = etree.parse('http://ep00.epimg.net/rss/tecnologia/portada.xml')
    # Todos los enlaces
    urls=tree.xpath('//address_component')
    mandar = imagenes.xpath('//enclosure/@url')


    for i in urls:
        test = i.xpath('type/text()')
        for t in test:
            if t == 'locality':
                localidad=i.xpath('long_name/text()')
            elif t == 'administrative_area_level_3':
                area=i.xpath('long_name/text()')
            elif t == 'administrative_area_level_2':
                provincia=i.xpath('long_name/text()')
            elif t == 'administrative_area_level_1':
                comunidad=i.xpath('long_name/text()')
            elif t == 'country':
                pais=i.xpath('long_name/text()')


    context={'localidad':localidad,'area':area,'provincia':provincia,'comunidad':comunidad,'pais':pais,'imagenes':mandar}
    return render(request, 'google.html',context)

def mongo (request):
    
    if request.method == 'POST':
        client = MongoClient()
        db = client.db_noticias
        posts = db.posts
        resultados = []
        categoria = request.POST['categoria']
        for resultado in posts.find({"categorias" : categoria}):
            resultados.append(resultado)
        context={'resultados':resultados}
        return render(request,'mongo.html',context)
    
    else:
        
        client = MongoClient()
        page = requests.get('http://ep00.epimg.net/rss/elpais/portada.xml')
        client.db_noticias.posts.remove()
    
        root = etree.fromstring(page.text.encode('utf-8'))

        items = root.xpath('//item')
        news = []
    

    
        for item in items:
            categorias = []
            texto=''
            cat = item.xpath('category')
        
            for i in item:
                if i.tag == '{http://purl.org/rss/1.0/modules/content/}encoded':
                    texto=i.text.encode('utf-8')
        
            for c in cat:
                categorias.append(c.text.encode('utf-8'))
    

            noticia = {
                "titulo": item.xpath('title')[0].text.encode('utf-8'),
                    "link": item.xpath('link')[0].text.encode('utf-8'),
                    "categorias": categorias,
                        "noticia":texto,

            }
                

            news.append(noticia)
            
        db = client.db_noticias
        posts = db.posts
        posts.insert(news)
        return render(request,'mongo.html')

def prueba (request):
    client = MongoClient()
    page = requests.get('http://ep00.epimg.net/rss/elpais/portada.xml')
    client.db_noticias.posts.remove()

    root = etree.fromstring(page.text.encode('utf-8'))
        
    items = root.xpath('//item')
    news = []
    j=0
        
    for item in items:
        j=j+1
        categorias = []
        texto=''
        cat = item.xpath('category')
            
        for i in item:
            if i.tag == '{http://purl.org/rss/1.0/modules/content/}encoded':
                texto=i.text.encode('utf-8')
        
        for c in cat:
            categorias.append(c.text.encode('utf-8'))
    
    
        noticia = {
            "titulo": item.xpath('title')[0].text.encode('utf-8'),
                "link": item.xpath('link')[0].text.encode('utf-8'),
                    "categorias": categorias,
                        "noticia":texto,
        
        }
    
    
        news.append(noticia)

    db = client.db_noticias
    posts = db.posts
    posts.insert(news)
    return JsonResponse({'datos':j})


#Hasta aqui las cosas de SSBW a partir de aqui no se puede borrar nada

def index (request):
    request.session.clear()
    return render(request, 'login.htm')


########################################################################
#Funciones de la página de registro

# Con validadores de campo
class registrationForm(forms.Form):
    name = forms.CharField (label = '',
                            max_length = 10,
                            required   = True,
                            error_messages={'required': 'Your Name is Required'},
                            widget=forms.TextInput(attrs={'placeholder': 'Introduzca Su Nombre','class': 'formulario'}),
                            validators = [
                                          validate_slug,
                                          ]
                            )
                                
    name_again = forms.CharField (label='',
                                  max_length = 10,
                                  widget=forms.TextInput(attrs={'placeholder': 'Su Nombre de Nuevo','class': 'formulario'}),
                                  error_messages={'required': 'Your Name is Required'},
                                  )
    password = forms.CharField (label='',
                                    max_length = 10,
                                    widget=forms.PasswordInput(attrs={'placeholder': 'Su Password',
                                                           'class': 'formulario',}
                                                           ),
                                    error_messages={'required': 'Your Password is Required'},
                                  )
    password_again = forms.CharField (label='',
                                      max_length = 10,
                                      widget=forms.PasswordInput(attrs={'placeholder': 'Su Password de Nuevo',
                                                               'class': 'formulario',}
                                                               ),
                                      error_messages={'required': 'Your Password is Required'},
                                      )
                                  

                                  
# Tipo email de HTML5, el navegador lo valida automaticamente
    email = forms.EmailField(label='',
                             widget=forms.TextInput(attrs={'placeholder': 'Su Correo Electronico','class': 'formulario'}),
                             error_messages={'required': 'Your Email is Required'},
                             )
    email_again = forms.EmailField(label='',
                                   widget=forms.TextInput(attrs={'placeholder': 'Repita Correo Electronico','class': 'formulario'}),
                                   error_messages={'required': 'Your Email is Required'},
                                   )

# Cross - field validation
# https://docs.djangoproject.com/en/1.7/ref/forms/validation/#using-validation-in-practice
# Override the clean method

def clean (self):
    cleaned_data = super(registrationForm, self).clean()
    n  = cleaned_data.get("name")
    na = cleaned_data.get("name_again")
    if n != na:
        raise forms.ValidationError ('los nombres no coinciden')


def registro (request):
    # Recibo el formulario
    if request.method == 'POST':
        # bound data to form
        form = registrationForm (request.POST)
        
        if form.is_valid ():
            try:
                user = User.objects.create_user(form.cleaned_data['name'], form.cleaned_data['email'],form.cleaned_data['password'])
                user = Usuario.objects.create
            except Exception as error:
                print error

            context =  {
                'fulanito':form.cleaned_data['name'],
                'form':form,
            }
            return render (request, 'login.htm', context)
        
        
        else:
            context =  {
                'fulanito': 'error',
                'form':form,
            }
            return render (request, 'registro.htm', context)

# Entrando la primera vez desde GET
    else:
        fulanito = 'default'
        
        form = registrationForm ()
        
        context = {
            'fulanito':fulanito,
            'form':form,
        }
        return render (request, 'registro.htm',context)

########################################################################
#Fucniones de la pagina de Facetas

def facetas (request):
    heuristicas=[]
    if 'jugabilidad' in request.session:
        heuristicas=Heuristica.objects.filter(propietario=request.session['user'],jugabilidad=request.session['jugabilidad'])
    else:
        heuristicas=Heuristica.objects.filter(propietario=request.session['user'],jugabilidad=1)
        request.session['jugabilidad']='1'

    context={'datos':heuristicas}
    request.session['menu']='facetas'
    return render(request, 'facetas.htm',context)

def guardar_Heuristica(request):
    if request.method == 'POST':#Si se pasan cosas por post quiere decir que ha habido cambios y por tanto los guardo en la base de datos
        id = request.POST['id']
        cuestion = request.POST['cuestion']
        comentarios = request.POST['comentarios']
        comentarioVisible = request.POST['checked']
        selectedElms = request.POST.getlist('selectedElmsIds[]')
        selectedElms = json.dumps(selectedElms)
        selectedAtr = request.POST.getlist('atributos[]')
        selectedAtr = json.dumps(selectedAtr)
        print selectedAtr
        range = request.POST['range']
        if id:
            p=Heuristica.objects.get(id=id)
            p.id=id
            p.nombre=cuestion
            p.comentario=comentarios
            p.comentarioVisible=comentarioVisible
            p.rango= range
            p.elementos = selectedElms
            p.atributos = selectedAtr
            p.jugabilidad = request.session['jugabilidad']
            p.save()
            return JsonResponse({'nuevo':'false'})
        else:
            p=Heuristica.objects.create(nombre=cuestion,propietario=request.session['user'],comentario=comentarios,elementos=selectedElms,rango=range,atributos=selectedAtr,jugabilidad=request.session['jugabilidad'])
            return JsonResponse({'nuevo':'true','id':p.id})

def cargar_dato(request):
    if request.method == 'POST':
        id = request.POST['id']
        heuristicas=Heuristica.objects.filter(propietario=request.session['user'],id=id)
        envio = serializers.serialize('json', heuristicas)
        return JsonResponse({"datos":envio})

def eliminar_dato(request):
    if request.method == 'POST':
        ids = []
        ids = request.POST.getlist('ids[]')
        for id in ids:
            print id
            seleccionado=Heuristica.objects.filter(id=id)
            seleccionado.delete()
        return JsonResponse({})

def cargarJugabilidad(request):
    if request.method == 'POST':
        jugabilidad = request.POST['jugabilidad']
        request.session['jugabilidad']=jugabilidad
        return redirect('facetas')
    return redirect('facetas')


        


########################################################################
#Funciones de la pagina MisTest

def mistest (request):
    request.session['menu']='mistest'
    mistests= MiTest.objects.filter(propietario=request.session['user'])
    heuristicas=[]
    if mistests:
        if 'mitest' in request.session:
            test=MiTest.objects.filter(propietario=request.session['user'],id=request.session['mitest'])
            if 'configuracion_jugabilidad' in request.session:
                heuristicas=Heuristica.objects.filter(propietario=request.session['user'],jugabilidad=request.session['jugabilidad'])
            else:
                heuristicas=Heuristica.objects.filter(propietario=request.session['user'],jugabilidad=1)
            context={ 'mitest': test[0],'tests':mistests,'heuristicas':heuristicas}
        else:
            request.session['mitest']=mistests[0].id
            if 'configuracion_jugabilidad' in request.session:
                heuristicas=Heuristica.objects.filter(propietario=request.session['user'],jugabilidad=request.session['jugabilidad'])
            else:
                heuristicas=Heuristica.objects.filter(propietario=request.session['user'],jugabilidad=1)

            context={ 'mitest': mistests[0],'tests':mistests,'heuristicas':heuristicas}
        return render(request, 'mistest.html',context)

    return render(request, 'mistest.html')

def eliminarTest(request):
    if request.method=='POST':
        MiTest.objects.filter(propietario=request.session['user'],id=request.session['mitest']).delete()
        mistests= MiTest.objects.filter(propietario=request.session['user'])
        if mistests:
            request.session['mitest']=mistests[0].id
    return redirect('mistest')

def cargarTest(request):
    if request.method=='POST':
            value = request.POST['testpulsado']
            request.session['mitest']=value
            return redirect('mistest')
    
    return redirect('mistest')

def nuevoTest(request):
    if request.method=='POST':
        misids = []
        asignados = []
        ids = Heuristica.objects.filter(propietario=request.session['user'])
        for id in ids:
            help = Heuristica.objects.filter(id=id.id)
            misids.append(serializers.serialize('json', help))
        misids=json.dumps(misids)
        p=MiTest.objects.create(nombre='Nuevo Test',propietario=request.session['user'],seleccionados=misids,asignados=asignados)
        request.session['mitest']=p.id
        return redirect('mistest')
    
    return redirect('mistest')

def cargarTablas(request):
    if request.method=='POST':
        heuristicas = []
        if request.POST['id']=='Intrinseca':
            heuristicas = Heuristica.objects.filter(propietario=request.session['user'],jugabilidad=1)
            heuristicas = serializers.serialize('json', heuristicas)
        elif request.POST['id']=='Mecanica':
            heuristicas = Heuristica.objects.filter(propietario=request.session['user'],jugabilidad=2)
            heuristicas = serializers.serialize('json', heuristicas)
        elif request.POST['id']=='Interactiva':
            heuristicas = Heuristica.objects.filter(propietario=request.session['user'],jugabilidad=3)
            heuristicas = serializers.serialize('json', heuristicas)
        elif request.POST['id']=='Artistica':
            heuristicas = Heuristica.objects.filter(propietario=request.session['user'],jugabilidad=4)
            heuristicas = serializers.serialize('json', heuristicas)
        elif request.POST['id']=='Intrapersonal':
            heuristicas = Heuristica.objects.filter(propietario=request.session['user'],jugabilidad=5)
            heuristicas = serializers.serialize('json', heuristicas)
        elif request.POST['id']=='Interpersonal':
            heuristicas = Heuristica.objects.filter(propietario=request.session['user'],jugabilidad=6)
            heuristicas = serializers.serialize('json', heuristicas)
        else:
            heuristicas = Heuristica.objects.filter(propietario=request.session['user'])
            heuristicas = serializers.serialize('json', heuristicas)
        return JsonResponse({'heuristica':heuristicas})


    return JsonResponse({})

def guardarTest(request):
    if request.method=='POST':
        id = request.session['mitest']
        seleccionados = request.POST.getlist('seleccionados[]')
        envioseleccionados = []
        for seleccion in seleccionados:
            help = Heuristica.objects.filter(id=seleccion)
            print help
            envioseleccionados.append(serializers.serialize('json', help))
        
        seleccionados = json.dumps(envioseleccionados)
        asignados = request.POST.getlist('asignados[]')
        asignados = json.dumps(asignados)
        p=MiTest.objects.get(id=id)
        p.seleccionados=seleccionados
        p.asignados = asignados
        p.nombre=request.POST['nombre']
        p.titulo=request.POST['titulo']
        p.save()
    
    return JsonResponse({})

def guardarEnviar(request):
    if request.method=='POST':
        id = request.session['mitest']
        seleccionados = request.POST.getlist('seleccionados[]')
        envioseleccionados = []
        for seleccion in seleccionados:
            help = Heuristica.objects.filter(id=seleccion)
            envioseleccionados.append(serializers.serialize('json', help))
    
        seleccionados = json.dumps(envioseleccionados)
        asignados = request.POST.getlist('asignados[]')
        aux = asignados
        asignados = json.dumps(asignados)
        test=MiTest.objects.get(id=id)
        nombre=request.POST['nombre']
        titulo=request.POST['titulo']
        test.seleccionados=seleccionados
        test.asignados = asignados
        test.nombre=request.POST['nombre']
        test.titulo=request.POST['titulo']
        Asignados.objects.filter(idTest=id).delete()
        for asignado in aux:
            Resultados.objects.filter(idTest=id,propietario=asignado).delete()
            p=Asignados.objects.create(nombre=nombre,creador=request.session['user'],seleccionados=seleccionados, propietario=asignado, titulo=titulo,idTest=id)
        
        test.save()
    
    return JsonResponse({})

def guardarComentarios(request):
    if request.method=='POST':
        comentarios=request.POST['comentarios']
        id = request.session['mitest']
        test=MiTest.objects.get(id=id)
        test.comentarios=comentarios
        test.save()

    return JsonResponse({})


def guardarEnviarIndividual(request):
    if request.method=='POST':
        id = request.session['mitest']
        seleccionados = request.POST.getlist('seleccionados[]')
        envioseleccionados = []
        for seleccion in seleccionados:
            help = Heuristica.objects.filter(id=seleccion)
            envioseleccionados.append(serializers.serialize('json', help))
        
        seleccionados = json.dumps(envioseleccionados)
        asignados = request.POST.getlist('asignados[]')
        envio = request.POST.getlist('envio[]')
        aux = envio
        asignados = json.dumps(asignados)
        test=MiTest.objects.get(id=id)
        nombre=request.POST['nombre']
        titulo=request.POST['titulo']
        test.seleccionados=seleccionados
        test.asignados = asignados
        test.nombre=request.POST['nombre']
        test.titulo=request.POST['titulo']
        for asignado in aux:
            Resultados.objects.filter(idTest=id,propietario=asignado).delete()
            u=Asignados.objects.filter(idTest=id,propietario=asignado)
            if u.count() > 0:
                Asignados.objects.filter(idTest=id,propietario=asignado).delete()
                p=Asignados.objects.create(nombre=nombre,creador=request.session['user'],seleccionados=seleccionados, propietario=asignado, titulo=titulo,idTest=id)
            else:
                p=Asignados.objects.create(nombre=nombre,creador=request.session['user'],seleccionados=seleccionados, propietario=asignado, titulo=titulo,idTest=id)
        
        test.save()
    
    return JsonResponse({})


def cargarUsuarios(request):
    if request.method=='POST':
        usuarios= User.objects.filter(username__istartswith=request.POST['user'])
        #usuarios = serializers.serialize('json', usuarios)
        list = []
        print usuarios
        for usuario in usuarios:
            list.append(usuario.username)
        return JsonResponse({'usuarios':list})

def UsuarioExiste(request):
    if request.method=='POST':
        try:
            usuarios= User.objects.get(username=request.POST['user'])
            return JsonResponse({'existe':True})
        except ObjectDoesNotExist:
            return JsonResponse({'existe':False})
    return JsonResponse({'existe':False})

def cargarValoracion(request):
    if request.method=='POST':
        resultados= Resultados.objects.filter(idTest=request.session['mitest'])
        if resultados:
            resultados = serializers.serialize('json',resultados)
            return JsonResponse({'existe':True,'resultados':resultados})
        else:
            return JsonResponse({'existe':False})

    return JsonResponse({'existe':False})
        


########################################################################
#Funciones de la pagina Asignados

def asignados (request):
    request.session['menu']='asignados'
    asignados= Asignados.objects.filter(propietario=request.session['user'])
    if asignados:
        if 'asignado' in request.session:
            asignado=Asignados.objects.filter(propietario=request.session['user'], id=request.session['asignado'])
            if asignado:
                context={ 'asignados':asignados,'asignado':asignado[0]}
            else:
                context={ 'asignados':asignados,'asignado':asignados[0]}
                request.session['asignado']=asignados[0].id
        else:
            context={ 'asignados':asignados,'asignado':asignados[0]}
            request.session['asignado']=asignados[0].id
        return render(request, 'asignados.html',context)

    return render(request, 'asignados.html')

def cargarAsignado(request):
    if request.method=='POST':
        value = request.POST['asignadopulsado']
        request.session['asignado']=value

    return redirect('asignados')

def eliminarAsignado(request):
    if request.method=='POST':
        Asignados.objects.filter(id=request.session['asignado']).delete()
        asignados= Asignados.objects.filter(propietario=request.session['user'])
        if asignados:
            request.session['asignado']=asignados[0].id

    return redirect('asignados')

def cargarPreguntas(request):
    if 'asignado' in request.session:
        asignado=Asignados.objects.filter(propietario=request.session['user'], id=request.session['asignado'])
        auxiliar = serializers.serialize('json', asignado)
        return JsonResponse({'envio':auxiliar,'nada':False})
    return JsonResponse({'nada':True})

def guardarResultado(request):
    if request.method=='POST':
        asignado=Asignados.objects.get(propietario=request.session['user'], id=request.session['asignado'])
        respuestas = request.POST['resultados']
        asignado.respuestas = respuestas
        asignado.save()
        return JsonResponse({})

def enviarResultado(request):
    if request.method=='POST':
        asignado=Asignados.objects.get(propietario=request.session['user'], id=request.session['asignado'])
        respuestas = request.POST['resultados']
        Resultados.objects.filter(idTest=asignado.idTest,propietario=request.session['user']).delete()
        Resultados.objects.create(propietario=request.session['user'],idTest=asignado.idTest,respuestas=respuestas,seleccionados=asignado.seleccionados)
        asignado.delete()
    return JsonResponse({})

########################################################################
#Fucniones de la pagina de Login

def logear(request):
    username = request.POST['user']
    password = request.POST['password']
    
    user = authenticate (username=username, password=password)
    
    if user is not None:
        if user.is_active:
            login(request, user)
            request.session['user'] = username
            return redirect('mistest')
            # Redirect to a success page.
        show_remove_link = False
        return render(request, 'login.htm', {'show_remove_link': show_remove_link})
    show_remove_link = True
    return render(request, 'login.htm', {'show_remove_link': show_remove_link})

###########################################################################
#Funciones de la página de Perfiles

#Función para llevarte a la pagina de definicion de perfiles
def perfiles (request):
    pruebas=[]
    pruebas= Perfil.objects.filter(propietario=request.session['user'])#Le indico que saque todos los perfiles cuyo propietario sea el usuario logueado
    seleccionado=pruebas
    request.session['menu']='perfiles'
    #request.session.clear()
    if pruebas:
        if 'pulsado' in request.session:#detecto si hay un perfil seleccionado y saco sus datos de la BD y se los mando al html
            seleccionado=Perfil.objects.filter(id=request.session['pulsado'])
        
        else:
            request.session['pulsado']=seleccionado[0].id
        context={ 'datos': seleccionado[0],'pruebas':pruebas}#si lo hay le asigno a guardado el valor de request.session[guardado] que tiene que ser true

    else:
        context={ 'datos': pruebas,'pruebas':pruebas}
    return render(request, 'perfiles.htm',context)





def guardarPerfil(request):
    #request.session['guardado'] = False
    if request.method == 'POST':#Si se pasan cosas por post quiere decir que ha habido cambios y por tanto los guardo en la base de datos
        
        #obtengo los datos del html
        disruptor = request.POST['disruptor']
        filantropo = request.POST['filantropo']
        socializador = request.POST['socializador']
        jugador = request.POST['jugador']
        logrador = request.POST['logrador']
        espiritu = request.POST['espiritu']
        id=request.POST['id']
        nombre=request.POST['nombre']
        
        #introduzco los datos en la BD
        p=Perfil.objects.get(id=id)
        p.disruptor=disruptor
        p.filantropo=filantropo
        p.socializador=socializador
        p.nombre=nombre
        p.jugador=jugador
        p.logrador=logrador
        p.espiritu=espiritu
        
        p.save()
        #request.session['guardado'] = True #Indico que hay algo nuevo guardado en la base de datos

        #return redirect('perfiles')#Redirecciono a la funcion perfiles pasandole el valor de guardado con request.session[guardado]
        return JsonResponse({})





#LLamo a la funcion al ser pulsado un perfil
def cargarPerfil(request):
    if request.method=='POST':
            value = request.POST['valor']
            request.session['pulsado']=value #le meto en la session el id del perfil y se lo paso a la funcion perfiles
            return redirect('perfiles')
    
    return redirect('perfiles')




#LLamo a la funcion al crear un nuevo perfil
def nuevoPerfil(request):
    if request.method=='POST':
        p=Perfil.objects.create(nombre='Nuevo Perfil',propietario=request.session['user'])
        request.session['pulsado']=p.id
        return redirect('perfiles')

#Elimina el Perfil activo
def eliminarPerfil(request):
    if request.method=='POST':
        seleccionado=Perfil.objects.filter(id=request.session['pulsado'])
        seleccionado.delete()
        del request.session['pulsado']#Elimino pulsado de la session
    return redirect('perfiles')

###########################################################################################################
#Funciones de la pagina de tipos de juegos

def juegos(request):
    pruebas=[]
    pruebas= Juegos.objects.filter(propietario=request.session['user'])#Le indico que saque todos los perfiles cuyo propietario sea el usuario logueado
    seleccionado=pruebas
    request.session['menu']='juegos'
    #request.session.clear()
    if pruebas:
        if 'pulsadojuego' in request.session:#detecto si hay un perfil seleccionado y saco sus datos de la BD y se los mando al html
            seleccionado=Juegos.objects.filter(id=request.session['pulsadojuego'])
        else:
            request.session['pulsadojuego']=seleccionado[0].id
        context={ 'datos': seleccionado[0],'pruebas':pruebas}#si lo hay le asigno a guardado el valor de request.session[guardado] que tiene que ser true
    
    else:
        context={ 'datos': pruebas,'pruebas':pruebas}


    return render(request,'juegos.htm',context)

#LLamo a la funcion al crear un nuevo perfil
def nuevoJuego(request):
    if request.method=='POST':
        p=Juegos.objects.create(nombre='Nuevo Juego',propietario=request.session['user'])
        request.session['pulsadojuego']=p.id
        return redirect('juegos')

#LLamo a la funcion al ser pulsado un perfil
def cargarJuego(request):
    if request.method=='POST':
        for key in request.POST:
            value = request.POST['valor']
            request.session['pulsadojuego']=value #le meto en la session el id del perfil y se lo paso a la funcion perfiles
            return redirect('juegos')
    
    return redirect('juegos')

#Elimina el Perfil activo
def eliminarJuego(request):
    if request.method=='POST':
        seleccionado=Juegos.objects.filter(id=request.session['pulsadojuego'])
        seleccionado.delete()
        del request.session['pulsadojuego']#Elimino pulsado de la session
    return redirect('juegos')

def guardarJuego(request):
    #request.session['guardado'] = False
    if request.method == 'POST':#Si se pasan cosas por post quiere decir que ha habido cambios y por tanto los guardo en la base de datos
        
        #obtengo los datos del html
        aventuras = request.POST['aventuras']
        accion = request.POST['accion']
        fp = request.POST['fp']
        simulacion = request.POST['simulacion']
        plataformas = request.POST['plataformas']
        estrategia = request.POST['estrategia']
        deporte = request.POST['deporte']
        motor = request.POST['motor']
        rol = request.POST['rol']
        print "Hola"
        sandbox = request.POST['sandbox']
        party = request.POST['party']
        educativo = request.POST['educativo']
        musical = request.POST['musical']
        nombre = request.POST['nombre']
        id=request.POST['id']
        
        #introduzco los datos en la BD
        p=Juegos.objects.get(id=id)
        p.aventuras=aventuras
        p.accion=accion
        p.fps=fp
        p.simulacion=simulacion
        p.plataformas=plataformas
        p.estrategia=estrategia
        p.deporte=deporte
        p.motor=motor
        p.rol=rol
        p.sandbox=sandbox
        p.party=party
        p.educativo=educativo
        p.musical=musical
        p.nombre=nombre

        
        p.save()
        #request.session['guardado'] = True #Indico que hay algo nuevo guardado en la base de datos
        
        #return redirect('perfiles')#Redirecciono a la funcion perfiles pasandole el valor de guardado con request.session[guardado]
        return JsonResponse({'datos':'juju'})





