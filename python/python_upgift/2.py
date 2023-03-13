#importerar random så jag kan generera slump tal
from random import *

#skapar en lista
lista = []

#en loop som kör koden 100 gånger
for n in range(100):

    #genererar ett slump tal mellan 1-1000 
    tal = randrange(1,1001)

    #lägger till talet till listan
    lista.append(tal) 


#sparar största talet från listan
största_talet = max(lista)

#sparar minsta talet från listan
minsta_talet = min(lista)

#sparar medelvärdet
medelvärdet = sum(lista)/100

#sorterar listan
lista.sort()

#printar 
print("sorterad lista: ",lista)
print("")
print("största talet:",största_talet,)
print("minsta talet:",minsta_talet)
print("medelvärdet: ",medelvärdet)

