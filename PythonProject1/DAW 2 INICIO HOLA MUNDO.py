from struct import pack_into

print("hola\n MUndo")
#comentario
#comentario de bloque
'''
comentario blque
 deddedededede 
'''
"""
RERE
"""
edad=56
print(edad)
edad="cincuenta y seis"
print(edad)
texto="golo"
print(texto)
precio=56.6
acertado=True
#si quiero intentar hacer una constante aunque realmente no existan se pone
MESES_ANYO=12
#operaciones  aritmeticas +-*/ % == -= += /= =
# no existen ++ --
#operadores nuevos
# // calcula cociente de la division entera
# ** para calcular potencias 2 elevado a 3 = 2**3
nuevo =precio *5 +MESES_ANYO
print(5//2)
print(5%2)
print(5/2)
texto="y"+"y"
print(texto)
print(texto,"mundo")
texto=("hola")
curso=2
ciclo ="saw"
print(texto,"mundo")
print("hola bien",curso,ciclo)
#en define el caracter q se va a utilizar como definidor de espacio en blanco en vez salto de linea
print(texto,"Mundo","cruel","siempre","pepe",end=" *** ",sep="-")# sin salto de linea
#sep no cambia el separador entre variables y textos y argumentos por defecto sep es caracteren blanco
# input()#nuestro scanner
# edad=input("mete name q te ")
# print(edad)

''' '''
# edad1=int(input("mete edad "))
# if int(edad1) < 10:
#     print("eres menor")
# else:
#     print("Eres mayo")

# sueldo = float(input("mete edad "))
# tiene q estar pegaqdo en forma de escalera o dara error es necesario tabulacion
# if sueldo > 10000.56:
#     print("debes ser rico")
# elif sueldo==10:
#     pass#si quiero q en este bloque no salga nada no se puede dejar vacio
# else:
#     print("SISASS")

# for n in range(0,10):#n va a tomar los rangos entre el parentesis de 0 a 10 (0 incluido) (0,10]
#     print(n)
#     print("FIN de programa")
# for p in range(0, 10, 2):#esto es de 0 a 10 de 2 en 2
#         print(p)
#         print("FIN de programa")
# for n in range(0, -10, -1):  # esto es de 0 a -10 de 1 en 1
#     print(n)
#     print("FIN de programa")
#
# for c in "holas":
#     print(c)


#
# print("\n")
# cad=input("mete cad\n")# recorrer una cadena
# cadsinEsp=""
# for e in cad:
#     if(e==" "):
#         pass
#     else:# si no es un espacio lo muestro y añado
#         print(e)
#         cadsinEsp +=e
#
# print(cadsinEsp)




#bucle while
print("\n")
i=0
while i<10 :#los : para abrir bloque no necesario parentesis
    print(i)
    i+=1

#numeros aleatorios libreria random
import random
# print(random.randint(1,2))
azar =random.randint(1,6)#numeros randoms entre 1 y 6 ambos incluidos
print(azar)


#como redondear matematicamente nos deveuleve valor redondeado sin modificar valor original
pi = 3.14159
print(round(pi,2))
print(round(pi,3))
print(round(pi,4))
print(pi)

import random
for i in range(0,5):
    print(random.randint(1,6))

for _ in range(0,5):#cuando la variable del for no la uso ponemos _ necesitamos un for de 5 vueltas no una variable auxiliar
    print(random.randint(1,6))

 #si creas una variable dentro de un bloque(if,for,while,etc) aqui si existe fuera
for j in range(0,5):
    azar=random.randint(1,6)
    print(azar)

# print(j)
print(azar)
#para mostrar 2 variables juntos     print(dado1,dado2) la , es el espacio

#max y min
mayor=max(34.5,4,5,56,7,4,332,5,0.43)
print(mayor)
menor=min(34.5,4,5,56,7,4,332,5,0.43)
print(menor)

#convertir a string cualquier cosa con str
texto ="el numero es "+str(45)
print(texto)