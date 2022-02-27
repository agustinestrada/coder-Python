# Desafio Tuplas

tupla = (5, 12, 7, 37, 8, 86, 19, 7, -783, 87, 188, 7, 9, 12, 7, 3982)

#El último ítem de tupla
print(tupla[len(tupla)-1])
#El número de ítems de tupla
print(len(tupla))
#La posición donde se encuentra el ítem 87 de tupla
print(tupla.index(87))
#Una lista con los últimos tres ítems de tupla
print(tupla[len(tupla):len(tupla)-4:-1])
#Un ítem que haya en la posición 8 de tupla
print(tupla[8])
#El número de veces que el ítem 7 aparece en tupla
print(tupla.count(7))