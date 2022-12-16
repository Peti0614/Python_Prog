lista = [] #üres lista

lista.append("Fifa")
lista.append("Fortnite")
lista.append("COD")
lista.append("GTA")
lista.append("PUBG")


#kiiratás 3 féle képpen
#1. 
print(lista)

#2.
for item in lista:
    print(item)

#3.
for i in range(len(lista)):
    print(lista[i])
print("*******************************************************")
#szürés
for item in lista:
    if item == "COD":
        print("IGEN")
    else:
        print("NO")







