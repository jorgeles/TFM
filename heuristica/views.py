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


def inicio (request):
    context={ 'prueba': request.session['fav_color']}
    return render(request, 'facetas.htm',context)



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


def logear(request):
    username = request.POST['user']
    password = request.POST['password']
    
    user = authenticate (username=username, password=password)
    
    if user is not None:
        if user.is_active:
            login(request, user)
            request.session['fav_color'] = 'blue'
            return redirect('inicio')
            # Redirect to a success page.
        show_remove_link = False
        return render(request, 'login.htm', {'show_remove_link': show_remove_link})
    show_remove_link = True
    return render(request, 'login.htm', {'show_remove_link': show_remove_link})

def perfiles (request):
    p=Perfil.objects.get(nombre='Jorge')
    if 'guardado' not in request.session:
        context={ 'datos': p,'guardado':False}
    else:
        context={ 'datos': p,'guardado': request.session['guardado']}
        request.session['guardado'] = False
    
    return render(request, 'perfiles.htm',context)

def guardarPerfil(request):
    request.session['guardado'] = False
    
    if request.method == 'POST':
        
        disruptor = request.POST['disruptor']
        filantropo = request.POST['filantropo']
        socializador = request.POST['socializador']
        jugador = request.POST['jugador']
        logrador = request.POST['logrador']
        espiritu = request.POST['espiritu']
        
        p=Perfil.objects.get(nombre='Jorge')
        p.disruptor=disruptor
        p.filantropo=filantropo
        p.socializador=socializador
        p.jugador=jugador
        p.logrador=logrador
        p.espiritu=espiritu
        
        p.save()
        request.session['guardado'] = True

    return redirect('perfiles')




