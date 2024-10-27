from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("ejercicio/listar", views.listar_proyectos, name="listar_proyectos"),
    path("tareas/desce/<int:proyecto_id>/", views.tareas_desce, name="tareas_desce"),
    path("usuarios/asce", views.usuarios_asce, name="usuarios_asce"),
    path("tarea/texto", views.tarea_texto, name="tarea_texto"),
    path("tareas/año", views.tareas_año, name="tareas_año"),
    path("comentarios/", views.comentarios_view, name="comentarios_view"),
    path("todos/comentarios/<str:palabra>/<int:año>/", views.todos_comentarios_tareas, name="todos_comentarios_tareas"),
    path("todas/etiquetas" , views.todas_etiquetas, name="todas_etiquetas"),
    path('filtro0/', views.usuarios_no_asignados, name='usuarios_no_asignados'),
]
