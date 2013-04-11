# -*- coding: utf-8 -*-
UNIDADES = (
    '',
    'UNO ',
    'DOS ',
    'TRES ',
    'CUATRO ',
    'CINCO ',
    'SEIS ',
    'SIETE ',
    'OCHO ',
    'NUEVE ',
    'DIEZ ',
    'ONCE ',
    'DOCE ',
    'TRECE ',
    'CATORCE ',
    'QUINCE ',
    'DIECISEIS ',
    'DIECISIETE ',
    'DIECIOCHO ',
    'DIECINUEVE ',
    'VEINTE '
)
DECENAS = (
    'VEINTI',
    'TREINTA ',
    'CUARENTA ',
    'CINCUENTA ',
    'SESENTA ',
    'SETENTA ',
    'OCHENTA ',
    'NOVENTA ',
    'CIEN '
)
CENTENAS = (
    'CIENTO ',
    'DOSCIENTOS ',
    'TRESCIENTOS ',
    'CUATROCIENTOS ',
    'QUINIENTOS ',
    'SEISCIENTOS ',
    'SETECIENTOS ',
    'OCHOCIENTOS ',
    'NOVECIENTOS '
)
 
def aLetra(number):
    """
    Converts a number into string representation
    """
    converted = ''
 
    if not (0 < number < 999999999):
 
        return 'No es posible convertir el numero a letras'
 
    number_str = str(number).zfill(9)
    millones = number_str[:3]
    miles = number_str[3:6]
    cientos = number_str[6:]
 
    if(millones):
        if(millones == '001'):
            converted += 'UN MILLON '
        elif(int(millones) > 0):
            converted += '%sMILLONES ' % __convertNumber(millones)
 
    if(miles):
        if(miles == '001'):
            converted += 'MIL '
        elif(int(miles) > 0):
            converted += '%sMIL ' % __convertNumber(miles)
 
    if(cientos):
        if(cientos == '001'):
            converted += 'UN '
        elif(int(cientos) > 0):
            converted += '%s ' % __convertNumber(cientos)
 
    return converted.title()
 
def __convertNumber(n):
    """
    Max length must be 3 digits
    """
    output = ''
 
    if(n == '100'):
        output = "CIEN "
    elif(n[0] != '0'):
        output = CENTENAS[int(n[0])-1]
 
    k = int(n[1:])
    if(k <= 20):
        output += UNIDADES[k]
    else:
        if((k > 30) & (n[2] != '0')):
            output += '%sY %s' % (DECENAS[int(n[1])-2], UNIDADES[int(n[2])])
        else:
            output += '%s%s' % (DECENAS[int(n[1])-2], UNIDADES[int(n[2])])
 
    return output

def ConvertirMes(mes, retorno=0):
    '''Debuelve el mes indicado como primer parametro, al tipo de retorno indicado en el segundo parametro.
    Ej. Para Enero el parametro mes pude ser Ene, Enero, January, Jan, 1 o -1... no importa las maysculas y minusculas
    esta funcion creara una tupla (1, Enero, January) y el valor a devolver de los tres, estara indicado en el parametro
    retorno 0 = 1, 1 = Enero, 2 = January
    Esta funcion es util para covertir el mes de texto a numero o mes en ingles a español y viceversa'''
    error=False
    try:
        mes = mes.lower() #pone todo el string mes en minusculas.
    except AttributeError: #error si el mes no es string(texto) 
        try:
            mes = int(mes) #se verifica que el mes sea un numero entero
        except TypeError: #error si el mes no es un numero
            error=True
    if error == False:
        verificado = False
        while True:
            if mes=="ene"or mes=="enero"or mes=="january"or mes=="jan"or mes==1 or mes==-1:
                mes = (1, "Enero", "January")
                break
            elif mes=="feb"or mes=="febrero"or mes=="february"or mes==2 or mes==-2:
                mes = (2, "Febrero", "February")
                break
            elif mes=="mar"or mes=="marzo"or mes=="march"or mes==3 or mes==-3:
                mes = (3, "Marzo", "March")
                break
            elif mes=="abr"or mes=="abril"or mes=="april"or mes=="apr"or mes==4 or mes==-4:
                mes = (4, "Abril", "April")
                break
            elif mes=="may"or mes=="mayo"or mes==5 or mes==-5:
                mes = (5, "Mayo", "May")
                break
            elif mes=="jun"or mes=="junio"or mes=="june"or mes==6 or mes==-6:
                mes = (6, "Junio", "June")
                break
            elif mes=="jul"or mes=="julio"or mes=="july"or mes==7 or mes==-7:
                mes = (7, "Julio", "July")
                break
            elif mes=="ago"or mes=="agosto"or mes=="august"or mes==8 or mes==-8:
                mes = (8, "Agosto", "August")
                break
            elif mes=="sep"or mes=="septiembre"or mes=="september"or mes==9 or mes==-9:
                mes = (9, "Septiembre", "September")
                break
            elif mes=="oct"or mes=="octubre"or mes=="october"or mes==10 or mes==-10:
                mes = (10, "Octubre", "October")
                break
            elif mes=="nov"or mes=="noviembre"or mes=="november"or mes==11 or mes==-11:
                mes = (11, "Noviembre", "November")
                break
            elif mes=="dic"or mes=="diciembre"or mes=="december"or mes=="dec"or mes==12 or mes==-12:
                mes = (12, "Diciembre", "December")
                break
            else:
                print("El parametro mes no es valido, se realizara una nueva verificacion con los tres primeros caracteres del parametro mes")
                try:
                    mes = mes[:3] #Si el mes es un String, se verificaran de el solo los 3 primero caracteres
                except TypeError:
                    print("El mes indicado como parametro no existe. ha indicado un numero fuera del rango, el rango es 1-12")
                    mes = (None, None, None) #si el mes es un numero fuera del rango 1-12. El retorno sera None
                    break
                if verificado == True:
                    mes = (None, None, None) #si el mes no cumple con las condiciones dadas. (2 veces verificado)
                    break
                else:
                    verificado = True
    else:
        print("El mes indicado como parametro no es valido")
        mes = (None, None, None) # si el mes es un caracter irreconocible.
    try:
        return mes[retorno]
    except: #si el parametro de retorno no es valido
        print("El segundo parametro no es valido, se devolvera el valor con el parametro retorno=0")
        return mes[0]
