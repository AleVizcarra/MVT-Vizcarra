from django.shortcuts import render
from .models import Familiar
from datetime import date
from django.http import HttpResponse
from django.template import loader
# Create your views here.

# Vista para crear un familiar, para ello se debe importar el modelo


def crear_familiar(request):
    # Creamos 5 familiares
    familiar1 = Familiar(
        nombre='Gladis',
        apellido='Peña',
        edad=54,
        fecha_nacimiento=date(1968, 8, 14),
    )

    familiar2 = Familiar(
        nombre='Eduardo',
        apellido='Bernal',
        edad=28,
        fecha_nacimiento=date(1994, 5, 16),
    )

    familiar3 = Familiar(
        nombre='Martín',
        apellido='Espinoza',
        edad=22,
        fecha_nacimiento=date(1999, 9, 30),
    )

    familiar4 = Familiar(
        nombre='Juan Manuel',
        apellido='Sarabia',
        edad=32,
        fecha_nacimiento=date(1990, 3, 29),
    )

    familiar5 = Familiar(
        nombre='Alma',
        apellido='Peña',
        edad=60,
        fecha_nacimiento=date(1963, 6, 1),
    )

    familiares = [familiar1, familiar2, familiar3, familiar4, familiar5]

    for familiar in familiares:
        familiar.save()

    dicc_familiares = {'familiares': familiares}
    plantilla = loader.get_template('familiares.html')
    documento = plantilla.render(dicc_familiares)

    return HttpResponse(documento)
