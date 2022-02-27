

lista1 = [1,12,123]
lista2 = ['Bye', 'Ciao', 'Agur', 'Adieu']

lista1.append(1234)
lista1.append('Hola')

lista2.append('Adios')
lista2.append(1234)

lista3 = lista1[0:len(lista1)-1:1]

lista4 = lista2[1:len(lista2)-1:1]

lista5 = lista3 + lista4

#lista1
print('Lista 1 resultado')
print(lista1)
#lista2
print('Lista 2 resultado')
print(lista2)
#lista3
print('Lista 3 resultado')
print(lista3)
#lista4
print('Lista 4 resultado')
print(lista4)
#lista5
print('Lista 5 resultado')
print(lista5)