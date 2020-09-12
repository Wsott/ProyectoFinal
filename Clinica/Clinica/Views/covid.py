from django.http import HttpResponse
from django.template import loader

def landing(request):
    html = loader.get_template("covid.html")
    return HttpResponse(html.render())