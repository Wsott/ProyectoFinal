from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from Datos.models import Usuario


def landing(request):
    if request.POST:
        post = request.POST
        try:
            elemento = Usuario.objects.get(user=post["user"])

            if (elemento == None):
                print("X")
            else:
                print("O")
        except ObjectDoesNotExist:
            print("BOOM")
            error = f"No existe un usuario llamado {post['user']}"
            msg = {"msg": error}
            return render(request, "menu.html", msg)
        else:
            return render(request, "menu.html")


    else:
        html = loader.get_template("menu.html")
        return render(request, "menu.html")