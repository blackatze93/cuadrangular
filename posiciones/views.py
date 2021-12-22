from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .forms import EquipoForm, PartidoForm
from .models import Equipo, Partido


def cargar_equipo(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EquipoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('cargar_resultados'))

        # if a GET (or any other method) we'll create a blank form
    else:
        form = EquipoForm()

    return render(request, 'equipo.html', {'form': form})


def cargar_resultados(request):
    equipos = Equipo.objects.values_list('nombre', flat=True).order_by('nombre')
    partidos = generar_partidos(equipos)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = request.POST
        locales = form.getlist('local')
        visitantes = form.getlist('visitante')
        goles_local = form.getlist('goles_local')
        goles_visitante = form.getlist('goles_visitante')

        # Establecer todos los partidos ganados, empatados y perdidos a cero
        for i in range(0, len(locales)):
            local = Equipo.objects.get(nombre=locales[i])
            visitante = Equipo.objects.get(nombre=visitantes[i])

            local.empatados = 0
            visitante.empatados = 0

            local.ganados = 0
            visitante.ganados = 0

            local.perdidos = 0
            visitante.perdidos = 0

            local.save()
            visitante.save()

        for i in range(0, len(locales)):
            local = Equipo.objects.get(nombre=locales[i])
            visitante = Equipo.objects.get(nombre=visitantes[i])
            partido = Partido(local=local,
                              visitante=visitante,
                              goles_local=goles_local[i],
                              goles_visitante=goles_visitante[i])

            if goles_local[i] > goles_visitante[i]:
                local.ganados += 1
                visitante.perdidos += 1
            elif goles_local[i] < goles_visitante[i]:
                local.perdidos += 1
                visitante.ganados += 1
            else:
                local.empatados += 1
                visitante.empatados += 1

            partido.save()
            local.save()
            visitante.save()

        return HttpResponseRedirect(reverse('tabla'))

    return render(request, 'partidos.html', {'partidos': partidos})


def tabla(request):
    equipos = Equipo.objects.all().order_by('-ganados', '-empatados', '-perdidos')
    print(equipos)
    return render(request, 'tabla.html', {'equipos': equipos})


def generar_partidos(equipos):
    # equipos = ['A','B','C','D']
    partidos = []
    for k in equipos:
        for j in equipos:
            if j == k:
                continue

            z = [k, j]
            z.sort()

            try:
                partidos.index(z)
            except:
                partidos.append(z)

    return partidos
