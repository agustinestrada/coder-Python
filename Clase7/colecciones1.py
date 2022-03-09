'''gordon lanzo su curva&strawberry ha fallado por un pie! -grito Joe Castiglione&dos
pies -le corrigio Troop&strawberry menea la cabeza como disgustado… -agrega el
comentarista

Transforma el texto en:
Gordon lanzo su curva...
- Strawberry ha fallado por un pie! -grito Joe Castiglione.
- Dos pies le corrigio Troop.
- Strawberry menea la cabeza como disgustado… -agrega el comentarista.'''

texto_crudo = "gordon lanzo su curva&strawberry ha fallado por un pie! -grito Joe Castiglione&dos pies -le corrigio Troop& strawberry menea la cabeza como disgustado... -agrega el comentarista"
texto_modificado = texto_crudo.replace("&"," ")

linea1 = texto_modificado[0:texto_crudo.find('&')] +'...'
linea2 = texto_modificado[texto_crudo.find('&'):texto_crudo.rfind('&dos')]
linea3 = texto_modificado[texto_crudo.find('&dos'):texto_crudo.rfind('&')]
linea4 = texto_modificado[texto_crudo.rfind('&'):len(texto_crudo)]


l1 = linea1.capitalize()
l2 = '- ' + linea2.strip().replace('strawberry', 'Strawberry')+'.'
l3 = '- ' + linea3.strip().capitalize().replace('-','').replace('troop','Troop')
l4 = '- ' + linea4.strip().capitalize() + '.'

#print(texto_crudo)
#print(texto_modificado)
print(l1)
print(l2)
print(l3)
print(l4)
