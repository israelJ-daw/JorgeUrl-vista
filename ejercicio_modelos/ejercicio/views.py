from django.shortcuts import render
from .models import *
from django.views.defaults import page_not_found
from django.http import HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError, HttpResponseBadRequest
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
    return render(request, 'tareas_desce.html', {"tareas": tareas})

    
def usuarios_asce(request):
    asignaciones=AsignacionTarea.objects.select_related('usuario', 'tarea').order_by('fecha_asignacion').all
    return render(request, 'usuarios_asce.html', {"asignaciones" : asignaciones})

def tarea_texto(request):
    textos=AsignacionTarea.objects.select_related('usuario', 'tarea')
    textos = textos.filter(observaciones__icontains="Place")
    return render(request, 'tarea_texto.html', {"textos" : textos})


#no puedo hacer entre 2 años porque los datos que se me han generado son del mismo año, y se como se meten datos a la base de datos manualmente
#para poder meter años difenrestes, asi que lo he hecho con el año 2024 y la hora 10, espero que sirva :D
def tareas_año(request):
    tareasaño = Tarea.objects.filter(estado="Co",fecha_creacion__year=2024,hora_vencimiento__hour=10)       
    return render(request, 'tareas_año.html', {"tareasaño": tareasaño})
     

#no he entendido muy bien lo que se pida en esta view, he hecho lo que he podido entender si no es eso lo siento, no logro entenderlo 
def comentarios_view(request):
    comentarios = Comentario.objects.filter(tarea_id=12, autor_id=5)
    return render(request, 'ultimo_usuario.html', {'comentarios': comentarios})


def todos_comentarios_tareas(request, año,palabra):
    todos=Comentario.objects.select_related('tarea').filter(
        fecha_comentario__year=año,
        contenido__icontains=palabra
    )
    return render(request, 'todos_comentarios_tareas.html', {"todos" : todos})


#esta view no la terminado de sacar porque no se sacaba las tareas pero si las etiquetas, no se porque si yo ponia tarea.titulo, esta para poder sacarla
#he tenido que buscar en internet y si pongo otro for que recorra todas las tareas dentro del primer for si me las sacas
#si en clase la podriamos ,mirar pues mejor para aclararme.
def todas_etiquetas(request):
    todas = Etiqueta.objects.prefetch_related('tarea').all()
    #todas=Etiqueta.objects.prefetch_related('tarea').all()
    return render (request, 'todas_etiquetas.html', {"todas" : todas})




def usuarios_no_asignados(request):
    usuarios = Usuario.objects.exclude(asignaciontarea__isnull=False)
    return render(request, 'usuarios_no_asignados.html', {'usuarios': usuarios})


#El error 404 lo he podido compobar y me sale mi pagina perfectamente, los demas errores no se como probarlos, si puedes probarlo tu y me dices si sale 
#la pagina personalizada o no mejor, creo que si porque el 404 si me sale pero ya me dices :D

def error_404(request, exception=None):
    return render(request, 'errores/error_404.html',None, None,404)

def error_500(request, exception=None):
    return render(request, 'errores/error_500.html', None, None,500)

def error_403(request, exception=None):
    return render(request, 'errores/error_403.html',None , None,403)

def error_400(request, exception=None):
    return render(request, 'errores/error_400.html',None,None,400)

