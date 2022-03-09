#Punto 1

primer_numero = float(input('Por favor ingrese un numero\n'))
segundo_numero = float(input('Por favor ingrese un segundo numero\n'))

opciones = input('Elija entre estas opciones\n 1. Mostrar una suma de los dos números\n 2. Mostrar una resta de los dos números (el primero menos el segundo)\n 3. Mostrar una multiplicación de los dos números\n 4. Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará\n')

if opciones == '1':
   print('La suma de los números es ',primer_numero + segundo_numero) 
elif opciones == '2':
   print('La resta de los números es ',primer_numero - segundo_numero)
elif opciones == '3':
   print('La multiplicación de los números es ',primer_numero * segundo_numero)
elif opciones == '4':
    print('Este programa ha finalizado')
else:
    print('La opcion ingresada no es valida')

#Punto 2

numero_elegido = int(input('Por favor ingrese un numero impar\n'))

while (numero_elegido%2) == 0:
   numero_elegido = int(input('Por favor ingrese un numero impar\n'))

print('Gracias ahora puede continuar con su vida')

#Punto 3

#Opcion 1
print('La suma de los numeros impares del 0 al 100 es',sum(range(1,100,2)))

#Opcion 2
acum = []

for i in range(1,100):
   if i%2 != 0:
      acum.append(i)

print(acum)
print('La suma es',sum(acum))


#Punto 4

total_numeros = int(input('Ingrese cuantos numeros esten en el conjunto\n'))
conjunto_numeros = []

if total_numeros <= 0:
   print('daleee, jugá un rato')
else:
   while total_numeros != len(conjunto_numeros): 
      numero = int(input('Ingrese el siguiente número del conjunto\n'))
      conjunto_numeros.append(numero)

print(conjunto_numeros)

print('el promedio de los numeros ingresados es', sum(conjunto_numeros)/total_numeros)


#Punto 5
numeros = [1, 3, 6, 9]

numero_elegido = int(input('Ingresa un numero entero del 0 al 9\n'))

while (numero_elegido < 0) or (numero_elegido > 9):
   numero_elegido = int(input('Ingresa un numero entero del 0 al 9\n'))

if numero_elegido in numeros:
   print(True)
else:
   print(False)



#Punto 6
'''
6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

●	Todos los números del 0 al 10 [0, 1, 2, ..., 10]
●	Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
●	Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
●	Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
●	Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
'''

punto1 = []
punto2 = []
punto3 = []
punto4 = []
punto5 =  []

for i in range(0,11):
   punto1.append(i)

for i in range(-10,1):
   punto2.append(i)

for i in range(0,21,2):
   punto3.append(i)

for i in range(-20,1):
   if i%2 != 0:
      punto4.append(i)

for i in range(0,51):
   if i%5 == 0:
      punto5.append(i)

print(punto1)
print(punto2)
print(punto3)
print(punto4)
print(punto5)



#Punto 7
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

lista_3 = []

for i1 in lista_1:
   for i2 in lista_2:
      if i1 == i2 and i1 not in lista_3:
         lista_3.append(i1)

print(lista_3)

