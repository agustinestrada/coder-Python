'''Un curso se ha dividido en dos grupos: A y B de acuerdo al nombre y a una
preferencia (Marvel o Capcom). 
El grupo A está formado por fans de Marvel con un nombre anterior a la M y los fans de Capcom con un nombre posterior a la N
El grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y preferencia, y muestre por pantalla el grupo que le corresponde.'''

nombre_nuevo_miembro = input('Por favor introduzca su nombre\n')

nombre_en_minuscula = nombre_nuevo_miembro.lower()

fan_de = input('Sos fan de Marvel o de Capcom?\n')
fan_de_minuscula = fan_de.lower()

inicial = nombre_en_minuscula[0]

grupo_A = []
grupo_B = []

if (fan_de_minuscula == 'marvel' and inicial < 'm') or (fan_de_minuscula == 'capcom' and inicial > 'n'):
    grupo_A.append(nombre_nuevo_miembro)
    print('Tu grupo es A')
else:
    grupo_B.append(nombre_nuevo_miembro)
    print('Tu grupo es B')

print('grupo A',grupo_A)
print('grupo B',grupo_B)


