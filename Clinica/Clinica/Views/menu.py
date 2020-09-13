from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from Datos.models import Usuario, Noticia, Mensaje


def landing(request):
    """
    Se traen las noticias de la base de datos
    """
    lista = Noticia.objects.all()[:5]
    contexto = {"articulos": lista}

    """
    Si la peticion de la pagina es un POST se puede realizar una operacion especial o renderizar la pagina
    original.
    """
    if request.POST:
        post = request.POST

        """
        En base a un discriminador se determina que operacion se realiza, el discriminador es un campo oculto
        en el HTML del template menu.html
        """
        if post["discriminador"] == "login":
            try:
                elemento = Usuario.objects.get(user=post["user"])

                if (elemento == None):
                    print("X")
                else:
                    print("O")
            except ObjectDoesNotExist:
                print("BOOM")
                error = f"No existe un usuario llamado {post['user']}"
                contexto["msg"] = error
                #msg = {"msg": error}
                return render(request, "menu.html", contexto)
            else:
                return render(request, "menu.html", contexto)
        elif post["discriminador"] == "mensaje":
            nuevoMensaje = Mensaje()

            nuevoMensaje.nombre = post["Nombre"]
            nuevoMensaje.dni = post["DNI"]
            nuevoMensaje.email = post["Email"]
            nuevoMensaje.mensaje = post["Mensaje"]
            nuevoMensaje.save()

            return render(request, "menu.html", contexto)
    else:
        #html = loader.get_template("menu.html")
        return render(request, "menu.html", contexto)