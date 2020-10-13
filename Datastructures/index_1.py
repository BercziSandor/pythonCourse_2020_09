# Indexelés kiterjesztése
# Negatív indexek, slicing

# https://www.python-course.eu/python3_sequential_data_types.php

lst = [10, 20, 30, 40, 50]

print(lst[len(lst) - 1]) # 50

# Elég gyakran akarunk a lista (tuple, sztring...) végéről indulva elérni elemeket.
# Ez negatív indexekkel lehetséges. Megjegyzéshez: a fenti kifejezésből elhagyjuk a len(lst)-t.

print(lst[-1], lst[-2]) # 50 40

############################

# Szintén gyakori feladat, hogy nem egyetlen elemet, hanem elemek egy csoportját akarjuk kiválasztani.
# Az ilyen módon kiterjesztett indexelés neve slicing.

# ELSŐ ALAK:

# [kezdő index : utolsó UTÁNI index]

# Amelyiket üresen hagyjuk, az a default értékét veszi fel.

# Kezdő index default: 0, lezáró index: len(lista) - 1.

print(lst[0:])  # [10, 20, 30, 40 50]  0 felesleges
print(lst[:])   # [10, 20, 30, 40 50]  lista másolata!
print(lst[0:3]) # [10, 20, 30]         0 felesleges
print(lst[:3])  # [10, 20, 30]
print(lst[2:4]) # [30, 40]

# Ha a lezárót túlcímezzük, megáll a határnál:

print(lst[2:99])  # [30 40 50]

# Ha a kezdőt túlcímezzük, üres lesz az eredmény:

print(lst[-2:2])  # []

############################

# MÁSODIK ALAK:

# [kezdő index : utolsó UTÁNI index : lépésköz]

# Lépésköz default: 1

print(lst[0::1])  # [10, 20, 30, 40, 50]
print(lst[::1])   # [10, 20, 30, 40, 50]
print(lst[::])    # [10, 20, 30, 40, 50]

print(lst[::3])   # [10, 40]

# Ha a lépésköznek negatívot adunk meg, akkor a kezdőindex default -1
# (a végéről kezdünk) és a lezáró index default -1 (0-ig megyünk);
# persze a lezáró indexhez NEM írhatunk -1-et, hiszen a lista utolsó
# elemét jelöli.

print(lst[::-1])   # [50, 40, 30, 20, 10] a lista megfordítva
print(lst[-1::-1]) # [50, 40, 30, 20, 10]
print(lst[:-1:-1]) # []  hoppá

print(lst[:2:-1])  # [50, 40]

# A slicing jelölésmóddal sok probléma kompakt módon megoldható.
# Tulajdonképpen bevezettünk egy új algebrai műveletet.
