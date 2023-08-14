from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import*
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,"aplicacion/base.html")

def Nosotros(request):
    return render(request,"aplicacion/nosotros.html")

def servicios(request):
    ctx= {"servicios":Servicios.objects.all()}
    return render(request,"aplicacion/servicios.html",ctx)

@login_required
def clientes(request):
    ctx= {"clientes":Clientes.objects.all()}
    return render(request,"aplicacion/clientes.html",ctx)

def acerca_de_mi(request):
    return render(request,"aplicacion/acerca_de_mi.html")

@login_required
def serviciosForm(request): #Form para el Modelo de servicios
    if request.method== "POST":
        servicios= Servicios(nombre=request.POST['nombre'], encargado=request.POST['encargado'] )
        servicios.save()
        return HttpResponse("Se datos fueron enviados correctamente")
    return render(request,"aplicacion/serviciosForm.html")

@login_required
def serviciosForm2(request): #Form_2 para el Modelo de servicios
    if request.method== "POST":
        miform_servicios=Ser_Form(request.POST)
        print(miform_servicios)
        if miform_servicios.is_valid():
            informacion_S= miform_servicios.cleaned_data
            servicios=Servicios(nombre=informacion_S['nombre'],encargado=informacion_S['encargado'],)
            servicios.save()
            return render(request,"aplicacion/Base.html")
    else:
        miform_servicios=Ser_Form()
    return render(request, "aplicacion/serviciosForm2.html", {"Form":miform_servicios})

@login_required    
def updateClientes(request, id_clientes):
    clientes=Clientes.objects.get(id=id_clientes)
    if request.method=="POST":
        miForm=Cli_Form(request.POST)
        if miForm.is_valid():
            clientes.nombre = miForm.cleaned_data.get('nombre'),
            clientes.servicio_contratado = miForm.cleaned_data.get('servicio_contratado')
            clientes.save()
            return redirect(reverse_lazy('clientes'))
    else:
        miForm = Cli_Form(initial={'nombre': clientes.nombre,
                                   'servicio_contratado': clientes.servicio_contratado})
    return render(request,"aplicacion/clientesForm.html",{'form':miForm})

@login_required
def deleteClientes(request, id_clientes):
    clientes=Clientes.objects.get(id=id_clientes)
    clientes.delete()
    return redirect(reverse_lazy('clientes'))

@login_required
def createClientes(request):
    
    if request.method=="POST":
        miform_clientes=Cli_Form(request.POST)
        print(miform_clientes)
        if miform_clientes.is_valid():
            p_nombre = miform_clientes.cleaned_data.get('nombre'),
            p_servicio_contratado = miform_clientes.cleaned_data.get('servicio_contratado')
            clientes=Clientes(nombre=p_nombre, 
                              servicio_contratado=p_servicio_contratado
                              )
            clientes.save()
            return redirect(reverse_lazy('clientes'))
    else:
        miform_clientes=Cli_Form()
    return render(request, "aplicacion/clientesForm.html", {"form":miform_clientes})



@login_required    
def updateServicios(request, id_servicios):
    servicios=Servicios.objects.get(id=id_servicios)
    if request.method=="POST":
        miForm=Ser_Form(request.POST)
        if miForm.is_valid():
            servicios.nombre = miForm.cleaned_data.get('nombre'),
            servicios.encargado = miForm.cleaned_data.get('encargado')
            servicios.save()
            return redirect(reverse_lazy('servicios'))
    else:
        miForm = Ser_Form(initial={'nombre': servicios.nombre,
                                   'encargado': servicios.encargado})
    return render(request,"aplicacion/serviciosForm2.html",{'form':miForm})

@login_required
def deleteServicios(request, id_servicios):
    servicios=Servicios.objects.get(id=id_servicios)
    servicios.delete()
    return redirect(reverse_lazy('servicios'))

@login_required
def createServicios(request):
    
    if request.method=="POST":
        miform_servicios=Ser_Form(request.POST)
        print(miform_servicios)
        if miform_servicios.is_valid():
            p_nombre = miform_servicios.cleaned_data.get('nombre'),
            p_encargado = miform_servicios.cleaned_data.get('encargado')
            servicios=Servicios(nombre=p_nombre, 
                              encargado=p_encargado)
            servicios.save()
            return redirect(reverse_lazy('servicios'))
    else:
        miform_servicios=Ser_Form()
    return render(request, "aplicacion/ServiciosForm2.html", {"form":miform_servicios})


def loginRequest(request):
    if request.method =="POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user=authenticate(request, username=usuario, 
                              password=clave)
        if user is not None:
            login(request, user)
            try: 
                avatar=Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar='/media/avatares/default.png'
            finally: 
                request.session['avatar']=avatar
                return render(request, "aplicacion/base.html", {"mensaje": f"Bienvenido {usuario}"})
        else:
            miform = AuthenticationForm()
        return render(request,"aplicacion/login.html", {"form": miform,"mensaje": "Datos incorrectos"})
    else:
        miform = AuthenticationForm()
        return render(request,"aplicacion/login.html", {"form": miform})
    
def register(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get("username")
            form.save()
            return render(request,"aplicacion/base.html", {"mensaje": "usuario creado"})
    else:
        form = UserCreationForm()

    return render(request, "aplicacion/register.html", {"form": form})

@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method =="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"aplicacion/base.html", {'mensaje':f"Usuario {usuario.username} actualizado correctamente"})
        else:
            return render(request,"aplicacion/editarPerfil.html", {'form':form})
    else:
        form=UserEditForm(instance=usuario)
    return render(request,"aplicacion/editarPerfil.html", {'form':form, 'usuario': usuario})

@login_required
def agregarAvatar(request):
    
    if request.method =="POST":
        form=AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            #borro avatar viejo
            u=User.objects.get(username=request.user)
            avatarViejo=Avatar.objects.filter(user=u)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()

             #creo avatar nuevo
            avatar=Avatar(user=u,imagen=form.cleaned_data['imagen'])
            avatar.save()

            #almaceno en session la url del avatar para mostrarla en base
            imagen=Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar']=imagen
           
            return render(request,"aplicacion/base.html")
       
    else:
        form=AvatarFormulario()
    return render(request,"aplicacion/agregarAvatar.html", {'form':form})

def oficinas(request):
    ctx= {"oficinas":Oficinas.objects.all()}
    return render(request,"aplicacion/oficinas.html",ctx)

@login_required    
def updateOficinas(request, id_oficinas):
    oficinas=Oficinas.objects.get(id=id_oficinas)
    if request.method=="POST":
        miForm=Ofi_Form(request.POST)
        if miForm.is_valid():
            oficinas.nombre = miForm.cleaned_data.get('nombre'),
            oficinas.direccion = miForm.cleaned_data.get('direccion')
            oficinas.save()
            return redirect(reverse_lazy('oficinas'))
    else:
        miForm = Ofi_Form(initial={'nombre': oficinas.nombre,
                                   'direccion': oficinas.direccion})
    return render(request,"aplicacion/oficinasForm.html",{'form':miForm})

@login_required
def deleteOficinas(request, id_oficinas):
    oficinas=Oficinas.objects.get(id=id_oficinas)
    oficinas.delete()
    return redirect(reverse_lazy('oficinas'))

@login_required
def createOficinas(request):
    
    if request.method=="POST":
        miform_oficinas=Ofi_Form(request.POST)
        print(miform_oficinas)
        if miform_oficinas.is_valid():
            p_nombre = miform_oficinas.cleaned_data.get('nombre'),
            p_direccion = miform_oficinas.cleaned_data.get('direccion')
            oficinas=Oficinas(nombre=p_nombre, 
                              direccion=p_direccion
                              )
            oficinas.save()
            return redirect(reverse_lazy('oficinas'))
    else:
        miform_clientes=Ofi_Form()
    return render(request, "aplicacion/oficinasForm.html", {"form":miform_oficinas})

def eventos(request):
    ctx= {"eventos":Eventos.objects.all()}
    return render(request,"aplicacion/eventos.html",ctx)

@login_required    
def updateEventos(request, id_eventos):
    eventos=Eventos.objects.get(id=id_eventos)
    if request.method=="POST":
        miForm=Eve_Form(request.POST)
        if miForm.is_valid():
            eventos.nombre = miForm.cleaned_data.get('nombre'),
            eventos.tipo = miForm.cleaned_data.get('tipo')
            eventos.save()
            return redirect(reverse_lazy('eventos'))
    else:
        miForm = Eve_Form(initial={'nombre': eventos.nombre,
                                   'tipo': eventos.tipo})
    return render(request,"aplicacion/eventosForm.html",{'form':miForm})

@login_required
def deleteEventos(request, id_eventos):
    eventos=Eventos.objects.get(id=eventos)
    eventos.delete()
    return redirect(reverse_lazy('eventos'))

@login_required
def createEventos(request):
    
    if request.method=="POST":
        miform_eventos=Eve_Form(request.POST)
        print(miform_eventos)
        if miform_eventos.is_valid():
            p_nombre = miform_eventos.cleaned_data.get('nombre'),
            p_tipo = miform_eventos.cleaned_data.get('tipo')
            eventos=Eventos(nombre=p_nombre, 
                              tipo=p_tipo
                              )
            eventos.save()
            return redirect(reverse_lazy('eventos'))
    else:
        miform_eventos=Eve_Form()
    return render(request, "aplicacion/eventosForm.html", {"form":miform_eventos})

def buscarServicio(request):
    return render(request,"aplicacion/buscarServicio.html")

def buscar2(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        encargado= Servicios.objects.filter(nombre__icontains=nombre)
        return render(request, "aplicacion/resultadosServicios.html", {"nombre":nombre, "encargado":encargado})
    return HttpResponse("No se encuentra ese servicio")











