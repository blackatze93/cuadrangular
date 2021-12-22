from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Equipo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ganados = models.PositiveSmallIntegerField(default=0)
    perdidos = models.PositiveSmallIntegerField(default=0)
    empatados = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.nombre}'


class Partido(models.Model):
    local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='local')
    visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='visitante')
    goles_local = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)])
    goles_visitante = models.PositiveSmallIntegerField(default=0,

                                                       validators=[MinValueValidator(0), MaxValueValidator(99)])

    def __str__(self):
        return f'{self.local} VS {self.visitante}'
