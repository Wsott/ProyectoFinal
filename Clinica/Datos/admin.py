from django.contrib import admin

from Datos.models import Usuario, Persona, Noticia, Turno, Mensaje

# Register your models here.


class PersonaAdmin(admin.ModelAdmin):
    list_display = ("dni", "nombre", "apellido", "nacimiento", "telefono", "localidad", "domicilio")


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("fk_persona_dni", "user", "email", "fechaCreacion")


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha", "titulo")


class MensajeAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha", "nombre", "dni", "email", "mensaje")


admin.site.register(Persona, PersonaAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Mensaje, MensajeAdmin)