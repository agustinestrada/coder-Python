'''Escribir un programa que le pregunte al usuario números hasta que ingrese el 0, 
cuando lo haga mostrar por pantalla la suma de todos los números ingresados.'''

acumulador = []
numero = int(input('Por favor introduzca un numero\n'))

while numero != 0:
    if numero:
       acumulador.append(numero)

    if len(acumulador) > 4:

        print('Si queres terminar con este calvario pone 0')
        
    numero = int(input('Por favor introduzca un numero\n'))

  
print('La suma de tus numeros es',sum(acumulador))