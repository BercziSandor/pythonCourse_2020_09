# 1.

# Adott két lista:

lst_1 = [10, 99, 0, 20, 88]
lst_2 = [0, 30, 99, 40, 77]

# Gyűjtsük ki egy tuple-ba azokat az elemeket, amelyek lst_1-ben szerepelnek,
# de lst_2-ben nem. A tuple legyen rendezve.

# Várt eredmény:
# (10, 20, 88)

#############################

# 2.

# Egy mások által írt függvény visszatérő értékéről nem tudjuk, milyen
# típusú. Hogyan állapítjuk meg?

#############################

# 3.

# A.

# El kell dönteni, hogy egy lst_1 lista tartalmazza-e az lst_2 lista
# minden elemét. Ez a megoldás miért nem jó?

lst_1 = [1, 2, 3, 4, 5]
lst_2 = [1, 2, 3]

contains = lst_2 in lst_1
print(contains) # False

# B. Adjunk meg olyan tesztadatokat, amelyekkel a contains változó
# értéke True lesz, tehát a hibás vizsgálat helyes eredményt ad.

# C. Mi a jó megoldás?

#############################

# 4.

# Írjunk egy függvényt, amely a paraméterként kapott sztringből kigyűjti aa számjegyeket,
# mintegy egy telefonszámból eltávolít minden felesleges karaktert.

in_str = '  + 36 1/555\t6677\n'
print(myfunc(in_str))  # 3615556677

#############################

# 5.

# Írjunk egy függvényt, amely paraméterként tetszőleges számú iterálható sorozatot
# kap és egy olyan listát ad vissza, amely az egyes sorozatok maximumait tartalmazza.
# Ha egy listát sem kap bemenetként akkor adjon vissza üres listát.
# A bemeneti sorozatok biztosan nem üresek.

lst_1 = [1, 2, 3]
tup_2 = [10, 20, 30]
set_3 = {100, 200, 300}

print(listofmax(lst_1, tup_2, set_3)) # [3, 30, 300]
print(listofmax())  # []

#############################
