# map objektum (map függvény)
# map kontra generátor kifejezés
# map egynél több sorozattal
# map lambda függvénnyel
# map beépített függvénnyel

# https://www.geeksforgeeks.org/python-map-function/
# https://realpython.com/python-map-function/
# https://www.digitalocean.com/community/tutorials/how-to-use-the-python-map-function
# https://stackoverflow.com/questions/1247486/list-comprehension-vs-map

##################################################

# A map objektum egy iterátor, amelynek első paramétere egy függvény, a többi paramétere
# egy, vagy több iterálható sorozat. Először a legegyszerűbb esetet vizsgáljuk, amikor
# csak két paraméter van, tehát egyetlen sorozat.

def func(n):
    return 2 * n

numbers = (1, 2, 3, 4)

map_obj = map(func, numbers)
print(map_obj) # <map object at 0x02867530>

for i in map_obj:
    print(i, end=' ')

print()  # 2, 4, 6, 8

# Ugyanez generátor kifejezéssel:

gen_exp = (func(n) for n in numbers)
print(gen_exp) # <generator object <genexpr> at 0x02868810>

for i in gen_exp:
    print(i, end=' ')

print()  # 2, 4, 6, 8

# A map objektum mindig helyettesíthető egy generátor kifejezéssel; Guido van Rossum
# el is akarta hagyni a Python 3-as verziójából:

# https://www.artima.com/weblogs/viewpost.jsp?thread=98196

# de aztán akkora volt az ellenállás, hogy megmaradt. Szerintem bizonyos esetekben a
# map-megoldás olvashatóbb, de ez persze szubjektív. Mindenképpen meg kell ismerkedni
# ezzel az eszközzel, mert találkozhatunk vele Python programokban.

##################################################

# Ha több iterálható sorozatot adunk meg, akkor a függvénynek annyi paraméterének
# kell lennie, ahány sorozat van. Az iterálás megszűnik a legrövidebb sorozat végének
# elérésekor ugyanúgy, mint a zip függvény esetében.

def func(a, b):
    return a + b

lst_1 = [1, 2, 3]
lst_2 = [100, 200, 300, 400]

map_obj = map(func, lst_1, lst_2)
print(list(map_obj)) # [101, 202, 303]

# Ugyanez generátor kifejezéssel:

gen_exp = (func(x, y) for x, y in zip(lst_1, lst_2))
print(list(gen_exp)) # [101, 202, 303]

# Vagy így is írhatjuk:

gen_exp = (func(*e) for e in zip(lst_1, lst_2))
print(list(gen_exp)) # [101, 202, 303]

# Ebben az esetben például szerintem a map-megoldás olvashatóbb.

##################################################

# Ha az illető függvény "egylövetű", csak itt van rá szükség, akkor persze lambda
# kifejezést is használhatunk:

map_obj = map(lambda a, b: a + b, lst_1, lst_2)
print(list(map_obj)) # [101, 202, 303]

# Ugyanez generátor kifejezéssel:

gen_exp = ((lambda a, b: a + b)(x, y) for x, y in zip(lst_1, lst_2))
print(list(gen_exp)) # [101, 202, 303]

# Vagy így is írhatjuk:

gen_exp = ((lambda a, b: a + b)(*e) for e in zip(lst_1, lst_2))
print(list(gen_exp)) # [101, 202, 303]

##################################################

# Az alkalmazott függvény persze beépített függvény is lehet, például a hatványozás:
lst_1 = [2, 3, 10]
lst_2 = [2, 3, 4]

map_obj = map(pow, lst_1, lst_2)
print(list(map_obj)) # [4, 27, 10000]

# Ugyanez generátor kifejezéssel:

gen_exp = (pow(x, y) for x, y in zip(lst_1, lst_2))
print(list(gen_exp)) # [4, 27, 10000]

##################################################

