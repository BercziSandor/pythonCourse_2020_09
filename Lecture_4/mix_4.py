# * mint ismétlés-operátor

x = 'AB' * 3
print(x) # ABABAB

x = (1, 2) * 4
print(x) # (1, 2, 1, 2, 1, 2, 1, 2)

x = [3, 4] * 3
print(x) # [3, 4, 3, 4, 3, 4]

# Ha a szorzó negatív, akkor üres sorozat lesz az eredmény:

x = (1, 2) * -4
print(x) # ()

####################################

# Sztring-formázás 1. f-sztringek

# Az f-fel megjelölt sztringek belsejében a kapcsos zárójelek közé tett
# kifejezések kiértékelődnek.

lst = [1, 2]
x = 3
s = f'lst: {lst} sum(lst): {sum(lst)} x + 5: {x + 5}'
print(s) # lst: [1, 2] sum(lst): 3 x + 5: 8

####################################

# Introspekció: isinstance

lst = [13, (1, 2), {'A', 'B'}]
for e in lst:
    if isinstance(e, int):
        print(e, 'egész szám')
    else:
        print(e, 'nem egész szám, a típusa:',type(e))

# 13 egész szám
# (1, 2) nem egyész szám, a típusa: <class 'tuple'>
# {'B', 'A'} nem egész szám, a típusa: <class 'set'>

# Vannak függvények, amelyek valamely paramétere lehet többféle típusú.
# Ilyen maga az isinstance függvény is; egy tuple-ban megadhatunk több típust is.

lst = [13, (1, 2), 3.14]
for e in lst:
    if isinstance(e, (int, float)):
        print(e, 'szám')
    else:
        print(e, 'nem szám, a típusa:',type(e))

# 13 szám
# (1, 2) nem szám, a típusa: <class 'tuple'>
# 3.14 szám

# Hasonlóan működik a sztring típus beginswith() és endswith() metódusa is.

####################################

# enumerate: iterálható sorozat bejárása, a sorszám nyilvántartása

lst = [13, -1, 2, 20,]
big_indexes = []
for i, e in enumerate(lst):
    if e > 10:
        big_indexes.append(i)

print(big_indexes)  # [0, 3]

# Persze ez a feladat nagyon kínálja magát, hogy listcomp-pal oldjuk meg:

big_indexes = [ i for i, e in enumerate(lst) if e > 10 ]

####################################
