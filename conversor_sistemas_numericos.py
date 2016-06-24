#Programa: Conversor de sistemas numericos
'''
El programa realiza la conversion entre los siguientes sistemas numericos:
*Sistema decimal
*Sistema binario
*Sistema hexadecimal
'''
num_hexadecimal = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def convertir_Decimal_Binario(numero_decimal):
    '''
    La funcion recibe argumentos enteros de base diez y regresa una cadena
    de caracteres conteniendo el numero en base 2
    '''
    temp = numero_decimal
    condicion = True 
    num_bin = ''
    while condicion:
        residuo = temp % 2
        temp= temp // 2
        num_bin+=str(residuo)
        if temp == 0:
            condicion = False
    return num_bin[::-1]
    
def convertir_Binario_Decimal(numero_binario):
    '''
    La funcion recibe argumentos enteros de base diez y regresa una cadena
    de caracteres conteniendo el numero en base 2
    '''
    num_bin_str=str(numero_binario)
    num_decimal=0
    base=1
    for x in range(len(num_bin_str)-1,-1,-1):
        num_decimal+=int(num_bin_str[x])*base
        base*=2
    return num_decimal

def convertir_Decimal_Hexadecimal(numero_decimal):
    
    temp = numero_decimal
    condicion = True
    num_hexa = ''
    while condicion:
        residuo = temp % 16
        temp = temp // 16
        num_hexa += str(num_hexadecimal[residuo])
        if temp == 0:
            condicion = False
    return num_hexa[::-1]

def convertir_Hexadecimal_Decimal(numero_hexadecimal):
    exp = 1
    num_hexa = str(numero_hexadecimal)
    num_dec=0
    for x in range(len(num_hexa)-1,-1,-1):
        base=num_hexadecimal.index(num_hexa[x])
        num_dec += base*exp 
        exp *= 16
    return num_dec

def convertir_Binario_Hexadecimal(numero_binario):
    num_hex = convertir_Binario_Decimal(numero_binario)
    return convertir_Decimal_Hexadecimal(num_hex)

def convertir_Hexadecimal_Binario(numero_hexadecimal):
    num_dec = convertir_Hexadecimal_Decimal(numero_hexadecimal)
    return convertir_Decimal_Binario(num_dec)

print( '''
NP-ID:Conversor de sistemas numericos
Elija alguna opcion:
1) Binario-Decimal
2) Decimal-Binario
3) Decimal-Hexadecimal
4) Hexadecimal-Decimal
5) Binario_Hexadecimal
6) Hexadecimal_Binario
''')
resp = True
while resp:
    seleccion  = int(input('Teclee cual es su eleccion: '))
    if seleccion > 0 and seleccion < 7:
        numero_convertir = input('Introduzca el numero a convertir: ')
        if seleccion == 1:
            numero_convertido = convertir_Binario_Decimal(numero_convertir)
            print('El numero %s base 2 convertido a base 10 es: %s'%(numero_convertir,numero_convertido))
        elif seleccion == 2:
            numero_convertido = convertir_Decimal_Binario(int(numero_convertir))
            print('El numero %s base 10 convertido a base 2 es: %s'%(numero_convertir,numero_convertido))
        elif seleccion == 3:
            numero_convertido = convertir_Decimal_Hexadecimal(int(numero_convertir))
            print('El numero %s base 10 convertido a base 16 es: %s'%(numero_convertir,numero_convertido))
        elif seleccion == 4:
            numero_convertido = convertir_Hexadecimal_Decimal(numero_convertir)
            print('El numero %s base 16 convertido a base 10 es: %s'%(numero_convertir,numero_convertido))
        elif seleccion == 5:
            numero_convertido = convertir_Binario_Hexadecimal(numero_convertir)
            print('El numero %s base 2 convertido a base 16 es: %s'%(numero_convertir,numero_convertido))
        elif seleccion == 6:
            numero_convertido = convertir_Hexadecimal_Binario(numero_convertir)
            print('El numero %s base 16 convertido a base 2 es: %s'%(numero_convertir,numero_convertido))
        resp = input('Desea volver a utilizar el conversor:[si/no] ')=='si'
    else:
        print('Solo teclee alguna de las opciones disponibles.')
    
    
