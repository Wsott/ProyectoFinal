from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

def landing(request):
    if (request.session.get('actual') is None):
        return redirect('menu')
    else:
        html = loader.get_template("covid.html")
        #return redirect("menu")
        print(request.session.get('actual'))
        return render(request, "panelUsuario.html")

def logOut(request):
    if (request.session.get('actual') is None):
        return redirect('menu')
    else:
        request.session.flush()
        return redirect('menu')
