from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def landing(request):
    html = loader.get_template("covid.html")
    return render(request, "panelUsuario.html")