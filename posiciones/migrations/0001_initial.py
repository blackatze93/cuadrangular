# Generated by Django 3.2 on 2021-12-22 20:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('ganados', models.PositiveSmallIntegerField(default=0)),
                ('perdidos', models.PositiveSmallIntegerField(default=0)),
                ('empatados', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goles_local', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('goles_visitante', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='local', to='posiciones.equipo')),
                ('visitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitante', to='posiciones.equipo')),
            ],
        ),
    ]