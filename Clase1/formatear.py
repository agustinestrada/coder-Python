# Desafio Slicing


nombre_alumno = input('ingrese su nombre y apellido\n')
nota = input('ingrese su nota\n')
materia = input('ingrese la materia\n')

cadena = f'{nombre_alumno} ha sacado un {nota} en {materia}'
cadena_volteada = cadena[len(cadena):0:-1]

print(cadena)
print(cadena_volteada)