from django.shortcuts import render, redirect
from .models import Galeria
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from .forms import GaleriaForm

def home(request):
    return render(request, 'artistas/home.html')

def nosotros(request):
    return render(request, 'artistas/nosotros.html')

def contacto(request):
    return render(request, 'artistas/contacto.html')

def galeria(request):
    galeria = Galeria.objects.all()
    context = {"galeria": galeria}
    return render(request, 'artistas/galeria.html', context)

@login_required
def gestiongal(request):
    galeria = Galeria.objects.all()
    context = {"galeria": galeria}
    return render(request, 'artistas/gestion/gestiongal.html', context)

def nuevogal(request):
    formulario = GaleriaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('gestiongal')
    return render(request, "artistas/gestion/nuevogaleria.html", {"formulario": formulario})

def editargal(request, codigo):
    galeria = Galeria.objects.get(codigo=codigo)
    formulario = GaleriaForm(request.POST or None, request.FILES or None, instance=galeria)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('gestiongal')
    return render(request, "artistas/gestion/editargaleria.html", {"formulario": formulario})

def borrargaleria(request, codigo):
    galeria = Galeria.objects.get(codigo=codigo)
    galeria.delete()
    messages.success(request, '¡Galeria Eliminado!')
    return redirect('gestiongal')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            request.session['username'] = username

    return render(request, "artistas/login.html")

def salir(request):
    logout(request)
    return redirect('/')
