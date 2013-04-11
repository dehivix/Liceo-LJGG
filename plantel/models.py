# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from estudiantes.models import *
from personal.models import *

class Anos(models.Model):
    nombre = models.CharField(max_length=20)
    class Meta:
        db_table = u'Ano'
        verbose_name_plural = 'Anos'
    def __unicode__(self):
        return u'%s'%(self.nombre)

class Secciones(models.Model):
    nombre = models.CharField(max_length=20)
    class Meta:
        db_table = u'secciones'
        verbose_name_plural = 'secciones'
    def __unicode__(self):
        return u'%s'%(self.nombre)

class Asignatura(models.Model):
    nombre = models.CharField(max_length=30)
    class Meta:
        db_table = u'asignaturas'
        verbose_name_plural = 'asignaturas'
    def __unicode__(self):
        return u'%s'%(self.nombre)

class Horario(models.Model):
    ano=models.ForeignKey('Anos',verbose_name='Año en curso')
    asignatura=models.ForeignKey('Asignatura',help_text='Escriba el nombre de la materia')
    seccion=models.ForeignKey('Secciones',help_text=u'Escriba el nombre de la sección',verbose_name=u'sección')
    profesor=models.ForeignKey(Personal,help_text='Escriba el nombre del profesor')
    class Meta:
        db_table=u'horario'
        unique_together=('ano','asignatura','seccion','profesor')
    def __unicode__(self):
        return "%s  %s" % (self.asignatura.nombre, self.seccion.nombre)


class Periodo(models.Model):
    nombre_id=models.CharField(max_length=30,unique=True)
    fecha_inicio = models.DateField(verbose_name=u'fecha de inicio')
    fecha_culminacion = models.DateField(verbose_name=u'fecha de culminación')
    class Meta:
        db_table = u'periodo'
    def __unicode__(self):
        return u"%s  %s  %s" %(self.nombre_id, self.fecha_inicio, self.fecha_culminacion)



