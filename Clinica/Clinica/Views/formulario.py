from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from Datos.models import Usuario, Persona

def landing(request):
    if request.POST:
        post = request.POST

        nuevaPersona = Persona()
        nuevaPersona.dni = post["DNI"]
        nuevaPersona.nombre = post["Nombre"]
        nuevaPersona.apellido = post["Apellido"]
        nuevaPersona.nacimiento = post["Nacimiento"]
        nuevaPersona.telefono = post["Telefono"]
        nuevaPersona.localidad = post["Localidad"]
        nuevaPersona.domicilio = post["Direccion"]

        nuevaPersona.save()

        nuevoUsuario = Usuario()
        nuevoUsuario.fk_persona_dni = nuevaPersona
        nuevoUsuario.user = post["Usuario"]
        nuevoUsuario.password = post["Password"]
        nuevoUsuario.email = post["Correo"]

        nuevoUsuario.save()

        return redirect("panel")
    else:
        return render(request, "formularioUsuario.html")