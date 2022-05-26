from django.shortcuts import render, HttpResponse, redirect
import requests

# Create your views here.
from tienda.carro import Carro
from api.models import Producto

def index(request):
    return render(request, 'index.html')

def productos(request):
    url = 'http://127.0.0.1:8000/api/productos/'
    respuesta = requests.get(url, auth=('admin', 'music_pro_admin_331'))
    datos = respuesta.json()
    music_pro = {'productos' : datos}
    return render(request, 'productos.html', music_pro)

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto)
    return redirect("carro")

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto)
    return redirect("carro")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar(producto)
    return redirect("carro")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar()
    return redirect("carro")

def api_dolar(request):
    url = 'https://mindicador.cl/api/dolar/'
    response = requests.get(url)
    datos_api = response.json()
    dolar_hoy = datos_api['serie'][0]['valor']
    dolar = {'valor_dolar' : dolar_hoy}
    return render(request, 'carro.html', dolar)
