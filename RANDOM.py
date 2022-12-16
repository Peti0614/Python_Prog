import random


lista = []

#feltöltjükl a listát random számokkal

for i in range(10): #10 darab szám lesz a listában
    lista.append(random.randint(1,100))
print(lista)


#Feladat
#for i in range(len(lista)):
    #if lista[i] >= 10 :
        #print(lista[i])

for i in range(len(lista)):
    if lista[i] <=10:
        print(lista[i])





