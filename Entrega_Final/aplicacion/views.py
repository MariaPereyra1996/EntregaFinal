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
                              servicio_contratado=p_encargado)
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




