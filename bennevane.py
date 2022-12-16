# szoveg = "ez egy szöveg"
# if "v" in szoveg:
#     print("benne van")
# else: print("nincs benne")
# print("**************************************")
# szoveg1 = "ezegyszöveg"
# beker = input("kérem a betűt!")
# if beker in szoveg:
#     print(f"{beker} betű benne van a szövegben")
# else: print(f"{beker} betű nincs a szövegben")

# hetnapjai = ["hetfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]

# beker = input("Kérem a napot! ").lower()

# if beker in hetnapjai:
#     print(f"{beker} nap benne van a listában")
# else: 
#     print(f"{beker} nap nincs a listában")


# jatekosok = ["messi", "ronaldo", "robben", "neymar", "lewandowski", "suarez"]

# beker = input("Kérek egy focista nevet! ").lower()

# if beker in jatekosok:
#     print(f"{beker} nevű focista benne van a listában")
# else:
#     print(f"{beker} nevű focista nincs benne a listában")

# hetnapjai = ["hetfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]

# hetnapjai_kisbetu = [item.upper() for in hetnapjai]
# hetnapjai_nagybetu= [item.upper() for in hetnapjai]

# beker = input("Kérem a napot! ").upper()

# if beker in hetnapjai_nagybetu:
#     print(f"{beker} nap benne van a listában")
# else:
#     print(f"{beker} nap nincs benne a listában")


jatekosok = ["messi", "ronaldo", "robben", "neymar", "lewandowski", "suarez"]

jatekosok_kisb = [item.lower() for item in jatekosok]


beker = input("Kérek egy focista nevet! ").lower()

if beker in jatekosok:
     print(f"{beker} nevű focista benne van a listában")
else:
     print(f"{beker} nevű focista nincs benne a listában")







