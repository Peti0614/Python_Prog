lista = [10, 3, 6, 5, 3 ,10, 9]

#megszámolás tétele
db = 0
for i in range(len(lista)):
    #if lista[i] == 3:
        db = db +1
print(db)

#összegzés tétele
osszeg = 0
for i in range(len(lista)):
    osszeg = osszeg + lista[i] 
print(osszeg)
print(sum(lista))

#szorzas tétele
szorzat = 1
for i in range(len(lista)):
    szorzat = szorzat * lista[i]
print(szorzat)

print(max(lista))
print(min(lista))

#szorzat 
