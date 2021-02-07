from math import pi
#premenna r sa rovna vstupu od uzivatela, ktory premenime na integer, pri vyziadani vstupu uzivatela vypise argument funkcie v " "
r = int(input("Napis polomer kruhu: "))
#funkcia print vo vete vypise polomer kruhu, ktory je povodne int a musime ho premenit na string, a plochu, ktora je matematicka operacia, premenena na string
print("Kruh s polomerom " + str(r) + " ma obsah " + str(pi*r**2))
