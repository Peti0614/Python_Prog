pont = int(input("Add meg a pontszámod"))
print(pont)


if pont<50:
    print("Elégtelen")
elif  50<=pont and pont<60:
    print("Elégséges")
elif 60<=pont and  pont<70:
    print("Közepes")
elif 70<=pont and pont<85:
    print("Jó")
elif pont>=85:
    print("Jeles")
else: pont>85:
    print("Nem megfelelő pontszámot írt be")
     