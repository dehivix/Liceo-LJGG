# -*- coding: utf-8 -*-
''' Modo script'''
from django.core.management import setup_environ
import settings
setup_environ(settings)
'''== Modo script =='''

"""
    - evaluar que el inscrito tenga solo secciones RA(1)
    - evaluar si hay un horario para las materias con la seccion solicitada
    - crear un horario con la materia y el periodo en la seccion correspondiente del inscrito
        
"""
inscrito=0
seccion=0
from estudiantes.models import Expediente,Inscripcion,Inscritos
from pensums.models import Horario,Seccion
def validar(inscrito):
    return not Expediente.objects.exclude(inscripcion__horario__seccion__id=1).filter(inscripcion__inscrito__id=inscrito).exists()
def corregirSecciones(inscrito,seccion):
    if validar(inscrito):
#Obtiene el último periodo inscrito (con calificaciones)
        periodo=Expediente.objects.filter(inscripcion__inscrito__id=inscrito).order_by('-inscripcion__horario__periodo_detalle')[0].inscripcion.horario.periodo_detalle
#Selecciona los detalles de la sección
        seccion=Seccion.objects.filter(nombre=seccion)[0]
#Selecciona los expedientes del último periodo cursado
        print seccion,inscrito
        ultimasInscripciones=Expediente.objects.filter(inscripcion__inscrito__id=inscrito,inscripcion__horario__periodo_detalle=periodo)
        for expediente in ultimasInscripciones:
#Buscar un horario similiar al periodo cursado pero con la sección a asignar
            horario=Horario.objects.filter(materia=expediente.inscripcion.horario.materia,seccion=seccion,periodo_detalle=expediente.inscripcion.horario.periodo_detalle)
            if not horario.exists():
#Si no existe el horario, se crea
                horario=Horario(materia=expediente.inscripcion.horario.materia,seccion=seccion,periodo_detalle=expediente.inscripcion.horario.periodo_detalle,profesor=expediente.inscripcion.horario.profesor)
                horario.save()
            else:
                horario=horario[0]
#Reemplazar el horario inscrito (con sección RA) por el nuevo horario
            expediente.inscripcion.horario=horario
            expediente.inscripcion.save()



    else:
        print "%s no tiene secciones RA"%inscrito
        return False

def procesarCsv(archivo):
    for row in archivo:
        inscrito=0
        if row[1]<>'':
            inscrito=Inscritos.objects.filter(estudiante__persona__num_identificacion=row[1])
            if inscrito.count()>1:
                print "%s Tiene mas de una carrera: "%row[1]
                for insc in inscrito:
                    print "\tinscrito id: %s  %s "%(insc.id,insc.carrera_sedes)
                inscrito=0
            else:
                inscrito=inscrito[0].id
        elif row[0]<>'':
                inscrito=row[0]
        seccion=row[2]
        if inscrito<>0:
            corregirSecciones(inscrito,seccion)
def main(argv):
    global inscrito,seccion
    import getopt
    try:
        optlist,args=getopt.getopt(argv,'i:s:c:a:',['inscrito=','seccion=','cedula=','csv='])
    except getopt.GetoptError, err:
        print str(err)
        sys.exit()
    else:
        archivo=''
        for arg,val in optlist:
            if arg in  ('-i','--inscrito'):
                inscrito=val
            elif arg in ('-c','--cedula'):
                inscrito=Inscritos.objects.filter(estudiante__persona__num_identificacion=val)
                if inscrito.count()>1:
                    print "Tiene mas de una carrera:"
                    for insc in inscrito:
                        print "\tinscrito id: %s  %s "%(insc.id,insc.carrera_sedes)
                    sys.exit()
                else:
                    inscrito=inscrito[0].id
            elif arg in ('-s','--seccion'):
                seccion=val
            elif arg in ('-a','--csv'):
                import csv
                archivo=csv.reader(open(val,'rb'))
        if archivo<>'':
                procesarCsv(archivo)
         
    if seccion<>0 and inscrito<>0:
        corregirSecciones(inscrito,seccion)
    elif archivo=='':
        print "las opciones [-i, -c] y -s son obligatorio"
        sys.exit()


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])



