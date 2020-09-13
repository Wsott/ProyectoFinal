from django.contrib import admin

from Datos.models import Usuario, Persona, Noticia, Turno

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    list_display = ("dni", "nombre", "apellido", "nacimiento", "domicilio")

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("fk_persona_dni", "user", "email", "fechaCreacion")

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Usuario, UsuarioAdmin)