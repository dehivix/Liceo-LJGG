# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from plantel.models import *

# Create your models here.
class Estudiantes(models.Model):
    cedula=models.CharField(max_length=8,unique=True,verbose_name=u'Número de Identificación')
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=(('M','Masculino'),('F','Femenino')),default=0,verbose_name=u'sexo')
    edad = models.IntegerField(default=0,verbose_name=u'edad', null=True)
    telefono = models.CharField(max_length=50,blank=True,)
    representante = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    class Meta:
        db_table = u'estudiantes'
        verbose_name_plural = "estudiantes"
    def __unicode__(self):
        return u'%s %s %s'%(self.cedula,self.apellidos,self.nombres)


class Inscripcion(models.Model):
    estudiante = models.ForeignKey('Estudiantes',help_text=u'Escriba la cédula, nombre o apellido del estudiante')
    horario = models.ForeignKey(Horario,help_text=u'Escriba el nombre de la materia a inscribir')
    periodo= models.ForeignKey(Periodo)
    activo = models.BooleanField()
    class Meta:
        db_table = u'inscripcion'
        verbose_name_plural = "inscripciones"
        verbose_name = 'inscripción'
        unique_together = ('estudiante','horario','periodo','activo')
        permissions=(('ver_todas_inscripciones','Ver todas las inscripciones'),)
    def __unicode__(self):
        return u'%s %s %s - %s' % (self.estudiante.cedula,self.estudiante.nombres,self.estudiante.apellidos,self.horario)


class Notas(models.Model):
    inscripcion = models.ForeignKey('Inscripcion',verbose_name=u'inscripción', help_text=u'Introduzca la cédula de la persona inscrita')
    nota = models.IntegerField()
    class Meta:
        db_table = u'notas'
        verbose_name_plural = "notas"
        unique_together = ('inscripcion',)
    def __unicode__(self):
        return u"%s  -  %s" %(self.inscripcion.horario.asignatura.nombre, self.inscripcion.estudiante)


class NEXA(models.Model):
    estudiante = models.ForeignKey('Estudiantes',help_text=u'Escriba la cédula, nombre o apellido del estudiante')
    horario = models.ForeignKey(Horario,help_text=u'Escriba el nombre de la materia a inscribir')
    nota_primer = models.IntegerField(blank=True, null=True)
    nota_segundo = models.IntegerField(blank=True, null=True)
    nota_tercero = models.IntegerField(blank=True, null=True)
    nota_definitiva = models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = u'nexa'
        verbose_name_plural = "nexas"
        unique_together = ('estudiante','horario')
    def __unicode__(self):
        return u"%s  -  %s" %(self.horario.asignatura.nombre, self.estudiante)



