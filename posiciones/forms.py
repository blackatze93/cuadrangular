from django.forms import ModelForm
from .models import Equipo, Partido


class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre']


class PartidoForm(ModelForm):
    class Meta:
        model = Partido
        fields = ['local', 'visitante', 'goles_local', 'goles_visitante']