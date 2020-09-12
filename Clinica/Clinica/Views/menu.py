from django.http import HttpResponse
from django.template import loader


def landing(request):
    html = loader.get_template("menu.html")
    return HttpResponse(html.render())