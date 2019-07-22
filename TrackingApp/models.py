#!TrackingApp/models.py
"""Definicion de los modelos de la app"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.utils.timezone import now

class Usuario(models.Model):
    """Modelo Usuario"""
    min_str = 3
    max_str = 30
    celular_size = [10, 13]
    user_size = [0, 20]
    password_size = [5, 128]

    cedula = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=max_str,
                              validators=[MinLengthValidator(min_str)])
    apellido = models.CharField(max_length=max_str,
                                validators=[MinLengthValidator(min_str)])
    celular = models.CharField(max_length=celular_size[1],
                               validators=[MinLengthValidator(celular_size[0])])
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to="uploads/foto_perfil/", null=True)
    usuario_id = models.OneToOneField(User, on_delete=models.PROTECT,
                                      null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "%s, %s %s" % (self.cedula, self.apellido, self.nombre)

    class Meta:
        """Informacion adicional del modelo"""

        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Actividad(models.Model):
    """Modelo Actividad"""
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % (self.nombre)

    class Meta:
        """Informacion adicional del modelo"""

        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"

class Chaleco(models.Model):
    """Modelo Chaleco"""
    id = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % (self.nombre)

    class Meta:
        """Informacion adicional del modelo"""

        verbose_name = "Chaleco"
        verbose_name_plural = "Chaleco"


class RegistroActividad(models.Model):
    """Modelo RegistroActividad"""
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT,
                                null=False)
   	actividad = models.ForeignKey('Actividad', on_delete=models.PROTECT,
                                  null=True)
   	chaleco = models.ForeignKey('Chaleco', on_delete=models.PROTECT,
                                  null=True)
   	fecha = models.DateField(default=now)
    fecha_inicio = models.DateTimeField(null=True)
    fecha_fin = models.DateTimeField(null=True)
    total_horas = models.IntegerField(validators=[MinValueValidator(1)])
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % (self.nombre)

class RegistroActividad(models.Model):
    """Modelo RegistroActividad"""
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT,
                                null=False)
   	actividad = models.ForeignKey('Actividad', on_delete=models.PROTECT,
                                  null=False)
   	fecha = models.DateField(default=now)
    fecha_inicio = models.DateTimeField(null=True)
    fecha_fin = models.DateTimeField(null=True)
    total_horas = models.IntegerField(validators=[MinValueValidator(1)])
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % (self.nombre)

class RegistroChaleco(models.Model):
    """Modelo RegistroActividad"""
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT,
                                null=False)
   	chaleco = models.ForeignKey('Chaleco', on_delete=models.PROTECT,
                                  null=True)
   	fecha = models.DateField(default=now)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % (self.nombre)

class RegistroTracking(models.Model):
	    """Modelo RegistroTracking"""
    id = models.AutoField(primary_key=True)
    registro_actividad = models.ForeignKey('RegistroActividad', on_delete=models.PROTECT,
                                null=False)
   	actividad = models.ForeignKey('Actividad', on_delete=models.PROTECT,
                                  null=False)
   	fecha = models.DateTimeField(default=now)
   	latitud = models.DecimalField(max_digits=8, decimal_places=5)
   	longitud = models.DecimalField(max_digits=8, decimal_places=5)
   	satelites = models.IntegerField(validators=[MinValueValidator(1)])
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % (self.nombre)
