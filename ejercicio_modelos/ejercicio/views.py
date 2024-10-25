from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    return render(request, 'index.html')

def listar_proyectos(request):  
    proyectos =Proyecto.objects.select_related('creador').prefetch_related('colaboradores')
    proyectos=proyectos.all() 
    
    
    return render(request, 'listar_proyectos.html', {"listar_proyectos" : proyectos})

def tareas_desce(request,proyecto_id):
    tareas=Tarea.objects.select_related('proyecto')
    tareas = tareas.filter(proyecto=proyecto_id).order_by("-fecha_creacion").all()
    return render(request, 'tarea_desce.html', {"tareas_desce:": tareas}), 
#nos falta hacer el template de aqui 
    