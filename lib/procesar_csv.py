# -*- coding: utf-8 -*-
from estudiantes.models import *
from sedes.models import *
from pensums.models import *
from django.db.models import Q
''' Buscar el PeriodoDetalle ''' 

def getPeriodo (periodo,carrera_sedeId,crear=False,lapso=False):
    if crear and lapso:
        periodO=Periodo.objects.filter(periodo=periodo)
        if periodO.exists():
            periodO=periodO[0]
        else:
            periodO,=Periodo.objects.get_or_create(periodo__periodo=periodo)
        carreraSede=CarrerasSedes.objects.get(id=carrera_sedeId)
        periodoId=PeriodoDetalles.objects.filter(periodo=periodO,carreras_sedes=carreraSede)
        if periodoId.exists():
            periodoId=periodoId[0]
        else:
            lapso=Lapso.objects.get(id=lapso)
            periodoId,crea=PeriodoDetalles.objects.get_or_create(periodo=periodO,carreras_sedes=carreraSede,lapso=lapso)

            print "Periodo %s creado"%periodo
    else:
        from django.core import exceptions
        try:
            periodoId=PeriodoDetalles.objects.get(periodo__periodo=periodo,carreras_sedes__id=carrera_sedeId)
        except exceptions.MultipleObjectsReturned:
            periodoId=PeriodoDetalles.objects.filter(periodo__periodo=periodo,carreras_sedes__id=carrera_sedeId)

    return periodoId
''' Obtiene el horario y lo crea si no existe la opcion create es True'''
def getHorario(periodo_detalleId,seccionId,materiaId,create=False):
    horarioId=0    
    try:
        horarioId=Horario.objects.get(materia=materiaId,periodo_detalle=periodo_detalleId,seccion=seccionId)
    except:
        if create:
            horario=Horario(materia=materiaId,periodo_detalle=periodo_detalleId,seccion=seccionId,profesor_id=1)
            horario.save()
            print "Creado horario materia:%s carrera:%s seccion:%s"%(materiaId,periodo_detalleId.carreras_sedes,seccionId)
            horarioId=horario
    
    return horarioId

''' Busca la inscripcion, si existe se asigna el estatus. 
    Sino existe se ingresa '''
def setInscripcion (horario,inscrito,lapso_id,estatus):
    try:
        inscripcion=Inscripcion.objects.get(horario=horario,inscrito=inscrito)
    except:
        lapso=Lapso.objects.get(id=lapso_id)
        inscripcion=Inscripcion(horario=horario,inscrito=inscrito,lapso=lapso,activo=estatus)
        inscripcion.save()
    else:
        inscripcion=Inscripcion.objects.filter(horario=horario,inscrito=inscrito).update(activo=estatus)
    return inscripcion
''' Retorna la inscripcion si existe, sino, la crea dependiendo de la opcion crear'''
def getInscripcion (horario,inscrito,crear=False,estatus=False,lapso_id=None):
    from django.core import exceptions
    try:
        inscripcion=Inscripcion.objects.get(horario=horario,inscrito=inscrito)
    except exceptions.MultipleObjectsReturned:
        inscripcion=Inscripcion.objects.filter(horario=horario,inscrito=inscrito)
        if inscripcion.count()>2:
            print "Mas de 2 inscripciones repetidas"
        else:
           if  Expediente.objects.get(inscripcion=inscripcion[0]).nota == Expediente.objects.get(inscripcion=inscripcion[1]).nota:
                Expediente.objects.filter(inscripcion=inscripcion[0]).delete()
                inscripcion[0].delete()
                inscripcion=inscripcion[1]

    except:
        try:
            inscripcion=Inscripcion.objects.get(horario__materia=horario.materia,horario__periodo_detalle=horario.periodo_detalle,inscrito=inscrito)
        except:
            if crear:
                print "Creando inscripcion %s %s"%(inscrito,horario)
                lapso=Lapso.objects.get(id=lapso_id)
                inscripcion=Inscripcion(horario=horario,inscrito=inscrito,lapso=lapso,activo=estatus)
                inscripcion.save()
            else:
                inscripcion=0
    return inscripcion

''' Cargar expediente '''
def setExpedinete(inscripcion,nota):
    expediente=Expediente(inscripcion=inscripcion,nota=nota)
    expediente.save()
    return expediente

def getExpediente(inscripcion,nota=0,crear=False):
    from django.core import exceptions 
    expediente=0
    try:
        expediente=Expediente.objects.get(inscripcion=inscripcion)
    except exceptions.MultipleObjectsReturned:
        try:
            expediente=Expediente.objects.get(inscripcion=inscripcion,nota=nota)
        except exceptions.ObjectDoesNotExist:
            if (int(nota)<10):
                nota='0%s'%nota
            try:
                expediente=Expediente.objects.get(inscripcion=inscripcion,nota=nota)
            except exceptions.ObjectDoesNotExist:
                expediente=Expediente.objects.get(inscripcion=inscripcion,)


        except exceptions.MultipleObjectsReturned:
            expediente=Expediente.objects.filter(inscripcion=inscripcion,nota=nota)
            expediente=expediente[0]



    except exceptions.ObjectDoesNotExist:
        if crear:
            expediente=Expediente(inscripcion=inscripcion,nota=nota).save()

    return expediente

''' Crear la sección si no existe '''

def getSeccion (nombreSeccion,crear=False):
    seccionId=0
    try:
        seccionId=Seccion.objects.get(nombre=nombreSeccion)
    except:
        if crear:
            print "Creando Seccion"
            seccion=Seccion(nombre=nombreSeccion)
            seccion.save()
            seccionId=seccion
    return seccionId

''' Obtener la materia según el código, a partir del pensum del estudiante '''

def getMateria(pensum,codigo):
    try:
        
        materia=Materia.objects.filter(materia_id__pensum__id=pensum,codigo=codigo)[0]
    except:
        print "Error materia %s %s"%(pensum,codigo)
        import pdb
        pdb.set_trace()
        pdb.set_trace()
    return materia


''' Obtener carrera según el código '''

def getCarrera(codigo):
    '''Si el código es 503 el Id es 3'''
    carreraId=0
    codigo.strip('\'')
    if codigo=='501':
        carreraId=42
    elif codigo=='503':
        carreraId=21
    elif codigo=='601':
        carreraId=16
    else:
        try:
            carreraId=CarrerasSedes.objects.get(carreras__codigo_interno=codigo,sedes__ubicacion__nombre='SAN JUAN').id
        except:
            import pdb
            pdb.set_trace()
    return carreraId
