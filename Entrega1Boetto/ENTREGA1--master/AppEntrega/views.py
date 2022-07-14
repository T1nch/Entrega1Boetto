from pipes import Template
from django.http import HttpResponse
from django.shortcuts import render
from AppEntrega.models import Clientes, Productos, Proveedores
from django.template import Context, Template
from AppEntrega.forms import ClientesForms, ProductosForms, ProveedoresForms


def inicio(request):
        return render (request, "AppEntrega/inicio.html")

def clientes(request):
        return render (request, "AppEntrega/clientes.html")

def proveedores(request):
        return render (request, "AppEntrega/proveedores.html")

def productos(request):
        return render (request, "AppEntrega/productos.html")

def ClientesFormulario(request):

        if request.method=="POST":
                form= ClientesForms(request.POST)
                if form.is_valid():
                        info= form.cleaned_data
                        nombre= info["nombre"]
                        direccion= info["direccion"]
                        dni= info["dni"]
                        clientes= Clientes(nombre=nombre, direccion=direccion, dni=dni)
                        clientes.save()
                        return render (request, "AppEntrega/inicio.html")
        else:
                form= ClientesForms()
        return render(request, "AppEntrega/clientesFormulario.html", {"formulario":form})

def ProveedoresFormulario(request):

        if request.method=="POST":
                form= ProveedoresForms(request.POST)
                if form.is_valid():
                        info= form.cleaned_data
                        nombre= info["nombre"]
                        direccion= info["direccion"]
                        cantidad_de_productos= info["cantidad_de_productos"]
                        proveedores= Proveedores(nombre=nombre, direccion=direccion, cantidad_de_productos= cantidad_de_productos)
                        proveedores.save()
                        return render (request, "AppEntrega/inicio.html")
        else:
                form= ProveedoresForms()
        return render(request, "AppEntrega/proveFormulario.html", {"formulario":form})


def ProductosFormulario(request):
        
        if request.method=="POST":
                form= ProductosForms(request.POST)
                print(form)
                if form.is_valid():
                        info= form.cleaned_data
                        print(info)
                        marca= info["marca"]
                        precio= info["precio"]
                        cantidad= info["cantidad"]
                        productos= Productos(marca=marca, precio=precio, cantidad=cantidad)
                        productos.save()
                        return render (request, "AppEntrega/inicio.html")
        else:
                form= ProductosForms()

        return render(request, "AppEntrega/productosFormulario.html", {"formulario":form})


def busquedaClientes(request):


        return render(request, "AppEntrega/busquedaClientes.html")


def buscar(request):

        if request.GET["dni"]:

                dni= request.GET["dni"]
                clientes=Clientes.objects.filter(dni=dni)
        

                return render(request, "AppEntrega/resultadosBusqueda.html", {"clientes":clientes})

        else:
                return render(request, "AppEntrega/busquedaClientes.html", {"error":"no se ingreso ningún dni"})

        return HttpResponse(respuesta)