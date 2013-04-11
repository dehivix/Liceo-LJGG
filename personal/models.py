# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from estudiantes.models import *
from plantel.models import *

# Create your models here.

class Cargos(models.Model):
    nombre = models.CharField(max_length=200)
    class Meta:
        db_table = u'cargo'
        verbose_name_plural = 'cargos'
    def __unicode__(self):
        return u'%s'%(self.nombre)


class Pagos(models.Model):
    nombre = models.CharField(max_length=200)
    class Meta:
        db_table = u'pago'
        verbose_name_plural = 'pagos'
    def __unicode__(self):
        return u'%s'%(self.nombre)


class Personal(models.Model):
    cargo=models.ForeignKey('Cargos',verbose_name='cargo que ejerce')
    cedula=models.CharField(max_length=8,unique=True,verbose_name=u'Número de Identificación')
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    pago=models.ForeignKey('Pagos',verbose_name='metodo de pago')
    class Meta:
        db_table = u'personal'
    def __unicode__(self):
        return u'%s %s %s'%(self.cedula,self.apellidos,self.nombres)
