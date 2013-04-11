# -*- coding: utf8
import settings
from django.core.management import setup_environ
#from jangobot import settings
#Activando setiings de django
setup_environ(settings)
from estudiantes.models import *

import csv
archivo=csv.reader(open('MATRICULA.csv','rb'), delimiter='	',quotechar='"')
import pdb
pdb.set_trace()
for linea in archivo:
    try:
        cedula=linea[0].lstrip('+-0')    
        apellidos=linea[1] 
        nombres=linea[2]   
        edad=linea[3].strip('.') 
        sexo=linea[4]   
        telefono=linea[5]   
        representante_ape=linea[6]   
        representante_nom=linea[7]   
        representante=representante_ape+' '+representante_nom
        direccion=linea[8]   

        if sexo=='V':
            sexo='M'
        elif sexo=='H':
            sexo='F'



        EstudianteN, result=Estudiantes.objects.get_or_create(cedula=cedula, nombres=nombres, apellidos=apellidos, edad=edad, sexo=sexo, telefono=telefono, representante=representante, direccion=direccion)
    except:
        print EstudianteN
    else:
        pass


