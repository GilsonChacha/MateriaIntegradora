# -*- coding: utf-8 -*-
"""Importación de modelos para que aparezcan en la sección de admin"""
from django.contrib import admin
from . import models

admin.site.register(models.Usuario)
admin.site.register(models.Actividad)
admin.site.register(models.Chaleco)
admin.site.register(models.RegistroActividad)
admin.site.register(models.RegistroChaleco)
admin.site.register(models.RegistroTracking)