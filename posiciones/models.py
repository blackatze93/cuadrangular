from django.db import models


class Equipo(models.Model):
    nombre = models.CharField(max_length=30)
    ganados = models.PositiveSmallIntegerField(default=0)
    perdidos = models.PositiveSmallIntegerField(default=0)
    empatados = models.PositiveSmallIntegerField(default=0)


class Partido(models.Model):
    local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='local')
    visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='visitante')
    goles_local = models.PositiveSmallIntegerField(default=0)
    goles_visitante = models.PositiveSmallIntegerField(default=0)