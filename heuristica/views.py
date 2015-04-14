# -*- encoding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from heuristica.models import Perfil
from django import forms
from django.core.validators import validate_slug, RegexValidator
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt, csrf_protect


#cosas chorras para las prácticas de SSBW se podran borrar algunas excepto las marcadas
from lxml import etree
import requests
from pymongo import MongoClient
# Create your views here.


def index (request):
    return render(request, 'login.htm')

# cosas de las practicas de SSBW que se podrán borrar
def google (request):
    tree = etree.parse ('http://maps.googleapis.com/maps/api/geocode/xml?address=daniel%20saucedo%20aranda%20granada')
    imagenes = etree.parse('http://ep00.epimg.net/rss/tecnologia/portada.xml')
    # Todos los enlaces
    urls=tree.xpath('//address_component')
    mandar = imagenes.xpath('//enclosure/@url')
    print(mandar)


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
        
        r = requests.get('http://servicios.elpais.com/rss/')
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

def inicio (request):
    context={ 'prueba': request.session['user']}
    request.session['menu']='facetas'
    return render(request, 'facetas.htm',context)

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
            return redirect('inicio')
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

        if 'guardado' not in request.session:#Compruebo si hay algo guardado para sacar la alerta de guardado
            context={ 'datos': seleccionado[0],'guardado':False,'pruebas':pruebas}
        
        else:
            context={ 'datos': seleccionado[0],'guardado': request.session['guardado'],'pruebas':pruebas}#si lo hay le asigno a guardado el valor de request.session[guardado] que tiene que ser true
            request.session['guardado'] = False
            del request.session['guardado']
    else:
        context={ 'datos': pruebas,'guardado':False,'pruebas':pruebas}
    return render(request, 'perfiles.htm',context)





def guardarPerfil(request):
    request.session['guardado'] = False
    
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
        request.session['guardado'] = True #Indico que hay algo nuevo guardado en la base de datos

    return redirect('perfiles')#Redirecciono a la funcion perfiles pasandole el valor de guardado con request.session[guardado]





#LLamo a la funcion al ser pulsado un perfil
def cargarPerfil(request):
    if request.method=='POST':
        for key in request.POST:
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




