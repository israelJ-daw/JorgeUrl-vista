# Generated by Django 5.1.2 on 2024-10-25 12:24

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=2500)),
                ('duracion', models.FloatField()),
                ('fecha_inicio', models.DateField(default=django.utils.timezone.now)),
                ('fecha_fin', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('fecha_registro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('prioridad', models.IntegerField()),
                ('estado', models.CharField(choices=[('PE', 'Pendiente'), ('PR', 'Progreso'), ('Co', 'Completada')], max_length=2)),
                ('completada', models.BooleanField()),
                ('fecha_creacion', models.DateField(default=django.utils.timezone.now)),
                ('hora_vencimiento', models.TimeField(default=django.utils.timezone.now)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyecto_tareas', to='ejercicio.proyecto')),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creador_tarea', to='ejercicio.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('tarea', models.ManyToManyField(related_name='etiquetas_tareas', to='ejercicio.tarea')),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionTarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones', models.TextField(max_length=2500)),
                ('fecha_asignacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejercicio.tarea')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejercicio.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='tarea',
            name='usuarios_asignados',
            field=models.ManyToManyField(related_name='colaboradores_tarea', through='ejercicio.AsignacionTarea', to='ejercicio.usuario'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='colaboradores',
            field=models.ManyToManyField(related_name='colaboradores_proyecto', to='ejercicio.usuario'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creador_proyecto', to='ejercicio.usuario'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField(max_length=2500)),
                ('fecha_comentario', models.DateTimeField(default=django.utils.timezone.now)),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios_tarea', to='ejercicio.tarea')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios_creador', to='ejercicio.usuario')),
            ],
        ),
    ]
