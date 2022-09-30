from django.shortcuts import render
from django.http import HttpResponse
from .models import RegistroUsuario
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'bodega/index.html')


@csrf_exempt
def crearUsuario(request):
    if request.method == 'GET':
        registros = RegistroUsuario.objects.all()
        return render(request, 'bodega/crearUsuario.html', {'registros': registros})
    elif request.method == 'POST':
        registro = RegistroUsuario()
        registro.rol = request.POST['rol']
        registro.nombre = request.POST['nombre']
        registro.contrasena = request.POST['contrasena']
        registro.contrasenaVe = request.POST['contrasenaVe']
        return HttpResponse('ok')

@csrf_exempt
def editar(request):
    if request.method == 'POST':
        try:
            rol= request.POST['rol']
            nombre = request.POST['nombre']
            contrasena = request.POST['contrasena']
            contrasenaVe = request.POST['contrasenaVe']
            RegistroUsuario.objects.filter(rol=rol).update(
                rol=rol, nombre=nombre, contraseña=contraseña, contrasenaVe=contrasenaVe)
            return HttpResponse('ok')
        except:
            return HttpResponse('error')

@csrf_exempt
def eliminar(request):
    if request.method == 'POST':
        try:
            sku = request.POST['sku']
            RegistroProducto.objects.filter(sku=sku).delete()
            return HttpResponse('ok')
        except:
            return HttpResponse('error')
        

def login(request):
    return render(request, 'bodega/login.html')

def loginAd(request):
    return render(request, 'bodega/loginAd.html')

def registroB(request):
    return render(request, 'bodega/registrob.html')

def pagAdmin(request):
    return render(request, 'bodega/pagAdmin.html')
    
def pagFun(request):
    return render(request, 'bodega/pagFun.html')


def somos(request):
    return render(request, 'bodega/somos.html')


def contacto(request):
    return render(request, 'bodega/contacto.html')

def crtUsuario(request):
    return render(request, 'bodega/crearUsuario.html')

def crtUnInternas(request):
    return render(request, 'bodega/crearUnInternas.html')

def crtRoles(request):
    return render(request, 'bodega/crearRoles.html')

def crtFlujos(request):
    return render(request, 'bodega/crearFlujo.html')

def crtTarea(request):
    return render(request, 'bodega/crearTarea.html')

def asgResp(request):
    return render(request, 'bodega/asignarResponsable.html')