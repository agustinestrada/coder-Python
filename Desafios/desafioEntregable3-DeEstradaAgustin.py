#Punto 1
'''
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
'''

#Punto 4
