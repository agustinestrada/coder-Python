'''Haremos el siguiente listado de ejercicios:
Escribir un programa que enumere los países de la siguiente lista:-------3
paises = ['Canada', 'USA', 'Mexico', 'Australia', Argentina, China, India]
Crear un bucle que sume los pares del 0 al 100-------------1
Imprimir por pantalla los números del 1 al 10 al revés-----------2
Pedirle a un usuario que ingrese un número, y devolver los dígitos totales del número
Por ejemplo, si el número es 75869, la salida debería ser 5.----------4
'''

paises = ['Canada', 'USA', 'Mexico', 'Australia', 'Argentina', 'China', 'India']


for indice, pais in enumerate(paises):
    print('indice ',indice)
    print('pais ',pais)

    print(paises[indice])