from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listar_proyectos(request):
    proyecto=Proyecto.all()
    
    return render(request, 'listar_proyectos.html', {"listar_proyectos" : proyecto })