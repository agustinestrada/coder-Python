'''5) La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila 
el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz 
de modificar las sumas incorrectas utilizando la técnica del slicing? 
 
🖐 Ayuda:  La función llamada sum(lista) devuelve una suma de todos los elementos de la 
lista
'''

e = (4,5,6)

print(e+(7,8,9))


matriz = [  
    [1, 5, 1], 
    [2, 1, 2], 
    [3, 0, 1], 
    [1, 4, 4] 
]

matriz[0].append(sum(matriz[0]))
matriz[1].append(sum(matriz[1]))
matriz[2].append(sum(matriz[2]))
matriz[3].append(sum(matriz[3]))


print(matriz)