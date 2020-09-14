from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

def landing(request):
    return render(request, "formularioUsuario.html")