from django.shortcuts import redirect, render
from .forms import CustomUserForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .models import Hardware
from .forms import HardwareForm



# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def noticias(request):
    return render(request, 'core/noticias.html')

def quienessomos(request):
    return render(request, 'core/quienessomos.html')

def logout(request):
    return render(request, 'registration/logout.html')


def registro(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')

    return render(request, 'registration/registro.html',data)

def api(request):
    return render(request, 'core/api.html')

def rtx2080(request):
    return render(request, 'core/rtx2080.html')

def rx5700(request):
    return render(request, 'core/rx5700.html')

def hyperxexo(request):
    return render(request, 'core/hyperxexo.html')

def proce(request):
    return render(request, 'core/procesadores.html')

def grafica(request):
    return render(request, 'core/grafica.html')

def ram(request):
    return render(request, 'core/ram.html')

def listado_hardware(request):

    hardwares = Hardware.objects.all()
    data = {
        'hardwares':hardwares
    }
    return render(request, 'core/listado_hardwares.html', data)
    


def nuevo_hardware(request):
    data = {
        'form':HardwareForm()
    }
    if request.method == 'POST':
        formulario = HardwareForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
        data['form'] = formulario 
    
    return render(request, 'core/nuevo_hardware.html', data)


def modificar_hardware(request, id):
    hardware = Hardware.objects.get(id=id)
    data = {
        'form':HardwareForm(instance=hardware)
    }
    if request.method == 'POST':
        formulario = HardwareForm(data=request.POST, instance=hardware)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = formulario
    if request.user.is_authenticated==True:
        return render(request, 'core/modificar_hardware.html',data)
    else:
        return redirect('login')


def eliminar_hardware(request, id):
    hardware = Hardware.objects.get(id=id)
    hardware.delete()
    return redirect('listado_hardwares')


