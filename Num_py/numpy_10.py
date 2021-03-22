# Különleges numpy értékek
# np.NaN (not a number): hiányzó érték
# np.isnan() függvény
# np.inf: végtelen nagy szám

# https://www.geeksforgeeks.org/python-infinity/
# https://stackoverflow.com/questions/42315541/difference-between-np-inf-and-floatinf
# https://stackoverflow.com/questions/17534106/what-is-the-difference-between-nan-and-none
# https://stackoverflow.com/questions/944700/how-can-i-check-for-nan-values

import numpy as np

print(type(np.NaN), 10 + np.NaN) # <class 'float'> nan

# Az elnevezés (Not A Number) nem szerencsés, mert valójában hiányzó numerikus értéket jelent.
# np.NaN-nal (is) jelöljük, ha valahol nincs megadva egy érték.

#############################

# np.NaN nem egyenlő saját magával:

print(np.NaN == np.NaN) # False

# Az elv: ismeretlen érték nem egyenlő egy másik ismeretlen értékkel, hiszen el sem
# tudjuk végezni az összehasonlítást. Van két üres doboz, vajon egyenlő a két doboz tartalma?

# Ezzel például akkor szembesülhetünk, amikor ki akarjuk íratni egy tömb azon indexeit,
# ahol NaN található. Ez nem fog kiírni semmit:

arr = np.array([10, np.NaN, 20, np.NaN])

for i, e in enumerate(arr):
    if e == np.NaN:   # sohasem teljesül
        print(i, end=' ')
print()

# Helyes megoldás: isnan() függvénnyel.

arr = np.array([10, np.NaN, 20, np.NaN])

for i, e in enumerate(arr):
    if np.isnan(e):
        print(i, end=' ')
print()

# 1 3

# Viszont ez a megoldás nem mindig alkalmazható, mert az isnan() függvényt csak
# int és float típusú változókra szabad használni:

isnan('a')   # hiba
isnan(None)  # hiba

from decimal import Decimal

isnan(Decimal(1)) # hiba

# Ha tehát a fenti listában előfordulhat sztring, None, stb. akkor másképp kell eljárni.
# Ilyen 'vegyes' tömböknél elég nehézkes a megoldás, itt nem is taglalom, csak a tanulságokat:

# -- A None-t mindig távolítsuk el már a legelején a numpy tömbjeinkből.
# -- 'Vegyes' típusú tömbök kezelése numpy-ban nehézkes. (pandas-ban jobb.)
# -- Ne felejtsük el: ha a tömbben csak egyetlen más típusú (tipikusan sztring) elem
#    is van, akkor a tömb MINDEN eleme sztring vagy object típusú lesz.
# -- A vegyes típusú tömbök megsemmisítik a numpy egyik nagy előnyét: a kis memóriafoglalást
#    és a nagy sebességet.

#############################

# Másik példa: ki akarjuk íratni két azonos hosszúságú listából az azonos indexű
# egyforma elemeket.

arr_1 = np.array([10, np.NaN, 20, np.NaN])
arr_2 = arr_1
for i, e in enumerate(arr_1):
    if arr_2[i] == e:
        print(e, end=' ')
print()

# 10.0 20.0

# Ez így a "nem NaN" egyforma elemeket íratja ki (persze lehet, hogy adott esetben
# pont ezt akarjuk).

# Ha arra is kíváncsiak vagyunk, ahol mindkét listában NaN áll:

arr_1 = np.array([10, np.NaN, 20, np.NaN])
arr_2 = arr_1
for i, e in enumerate(arr_1):
    if arr_2[i] == e or (np.isnan(e) and np.isnan(arr_2[i])):
        print(e, end=' ')

print()

# 10.0 nan 20.0 nan

# Viszont ez a megoldás sem mindig alkalmazható, mert az isnan() függvényt csak
# int és float típusú változókra szabad használni - ld. a fenti megjegyzést a
# vegyes típusú numpy tömbökről.

#############################

# None-nal ellentétben np.NaN logikai igaz értéket képvisel:

if np.NaN: print('IGAZ')    # IGAZ
if not None: print('HAMIS') # HAMIS

#############################

# Az egyenlőtlenségvizsgálat (is) meglepő eredményt hoz:

print(np.NaN != np.NaN) # True

# Ha következetes lenne a szabály, akkor itt is False-nak kellene lennie az eredménynek.

# Van két üres doboz, vajon különböző a két doboz tartalma?

# Az SQL megoldása a legtisztább szerintem, ott a NULL-t összehasonlítva bármivel,
# bárhogyan (=, !=, <...), NULL lesz az eredmény. Ott 3 állapotú a logika:
#   + igaz
#   + hamis,
#   + ismeretlen (NULL).

#############################

# A hiányzó érték másik jelzése: None. NAGYON más!

print(10 + np.NaN) # nan
print(10 + None)   # hiba

# Tanulság (ismét): A None-t már az elején el kell távolítani az adataink közül.

# None egyenlő saját magával:

print(None == None)     # True

#############################

# A végtelen nagy szám jelzése: np.inf

print(type(np.inf), 10 + np.inf)        # <class 'float'> inf
print(np.inf + np.inf, np.inf - np.inf) # inf nan

#############################

# Két másik módon is ábrázolhatjuk a végtelen nagy számot.

# A math modul segítségével:

import math

print(type(math.inf), 10 + math.inf)  # <class 'float'> inf
print(math.inf + math.inf, math.inf - math.inf) # inf nan

# float('inf') segítségével:

print(type(float('inf')), 10 + float('inf'))  # <class 'float'> inf
print(float('inf') + float('inf'), float('inf') - float('inf')) # inf nan

#############################
