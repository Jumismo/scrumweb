# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 12:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyScrum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('asunto', models.CharField(max_length=100)),
                ('horaInicio', models.TimeField()),
                ('duracion', models.IntegerField()),
                ('conclusiones', models.TextField(default='Conclusiones de la reunion')),
            ],
        ),
        migrations.CreateModel(
            name='HistoriasUsuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('prioridad', models.CharField(choices=[('0', 'Baja'), ('1', 'Media'), ('2', 'Alta')], max_length=1)),
                ('estimacion', models.IntegerField()),
                ('criterios_validacion', models.TextField()),
                ('descripcion', models.TextField(default='Describa el caso de uso')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Retrospectiva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('asunto', models.CharField(max_length=100)),
                ('fechaInicio', models.DateField()),
                ('duracion_maxima', models.IntegerField()),
                ('acciones_mejora', models.TextField(default='Acciones de mejora')),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('dedicacionMax', models.IntegerField(default=0)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrum.Proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='SprintReview',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('horaInicio', models.TimeField()),
                ('duracion', models.IntegerField()),
                ('propuesta', models.TextField(default='Propuesta')),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrum.Sprint')),
            ],
        ),
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('0', 'No Iniciada'), ('1', 'En Proceso'), ('2', 'Completada')], max_length=1)),
                ('dedicacion', models.IntegerField(default=0)),
                ('historia_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrum.HistoriasUsuario')),
                ('sprint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scrum.Sprint')),
            ],
        ),
        migrations.CreateModel(
            name='TareasDailyScrum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tareas_realizadas', models.TextField()),
                ('tareas_futuras', models.TextField()),
                ('obstaculos', models.TextField()),
                ('dailyScrum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrum.DailyScrum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TareasSpringReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tareas_realizadas', models.TextField(default='Tareas realizadas')),
                ('tareas_no_realizadas', models.TextField(blank=True)),
                ('propuesta_fecha_fin', models.DateField()),
                ('springReview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrum.SprintReview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='dailyscrum',
            name='sprint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrum.Sprint'),
        ),
    ]
