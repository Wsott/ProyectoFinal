from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from django.core.exceptions import ObjectDoesNotExist

from Datos.models import Usuario, Persona, Turno

def landing(request):
    if (request.session.get('actual') is None):
        return redirect('menu')
    else:
        nombre = request.session.get('actual')
        elemento = Usuario.objects.get(user=nombre)
        persona = elemento.fk_persona_dni

        turno = None
        try:
            turno = Turno.objects.filter(fk_persona_dni=persona)
        except ObjectDoesNotExist:
            turno = None

        contexto = {"turno": turno}

        return render(request, "panelUsuario.html", contexto)

def logOut(request):
    if (request.session.get('actual') is None):
        return redirect('menu')
    else:
        request.session.flush()
        return redirect('menu')
