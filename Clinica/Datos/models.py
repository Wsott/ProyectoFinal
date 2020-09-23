from django.db import models

# Create your models here.
class Persona(models.Model):
    dni = models.IntegerField(primary_key=True, editable=True)
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    nacimiento = models.DateField()
    telefono = models.CharField(max_length=16)
    localidad = models.CharField(max_length=64)
    domicilio = models.CharField(max_length=256)

    def __str__(self):
        return str(self.dni)

class Salud(models.Model):
    fk_persona_dni = models.OneToOneField(Persona,
                                          on_delete=models.CASCADE,
                                          primary_key=True)
    grupoSanguineo = models.CharField(max_length=4, null=True)
    fuma = models.CharField(max_length=16)
    bebe = models.CharField(max_length=16)
    alergias = models.CharField(max_length=512)
    medicamentos = models.CharField(max_length=512)
    enfcronica = models.CharField(max_length=512)
    antquirurgicos = models.CharField(max_length=512)

class Usuario(models.Model):
    fk_persona_dni = models.OneToOneField(Persona,
                                          on_delete=models.CASCADE,
                                          primary_key=True) #models.IntegerField(primary_key=True, editable=False)
    user = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=128, unique=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

class Noticia(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    fecha = models.DateField()
    imagen = models.CharField(max_length=256)
    titulo = models.CharField(max_length=256)
    cuerpo = models.TextField()

class Mensaje(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    fecha = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=256)
    dni = models.IntegerField()
    email = models.EmailField(max_length=128)
    mensaje = models.TextField()

class Medico(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    nacimiento = models.DateField()
    especialidad = models.CharField(max_length=64)

    def __str__(self):
        return str(self.id)

class Turno(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    fk_persona_dni = models.ForeignKey(Persona,
                                          on_delete=models.CASCADE,
                                          null=True)
    especialista = models.CharField(max_length=128)
    pago = models.CharField(max_length=32)
    nombrePago = models.CharField(max_length=64)
    fecha = models.DateField(null=True)
