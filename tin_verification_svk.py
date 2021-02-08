rodne_cislo = input("Zadaj 10-miestne rodné číslo: ")

x = int(rodne_cislo)

p1 = x % 11 == 0

x_sub = str(x)

m = str(x_sub[2:4])
m2 = int(m)

if m2 > 50:
    m2 = m2 - 50
    
if m2 > 1 and m2 <= 12 and len(str(x)) == 10 and p1:
    print("Správny tvar. ")
    
else:
    print("Nesprávny tvar. ")
