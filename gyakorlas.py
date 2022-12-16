kor = int(input("Add meg a korod:"))
print(kor)

felnott = 18
nyugdijas = 65

if kor > nyugdijas:
    print("Te már nyugdíjas vagy")
elif kor < felnott:
    print("Te még kiskorú vagy")
elif kor>=felnott and kor<nyugdijas:
    print("Te már felnőtt vagy") 
    
    


