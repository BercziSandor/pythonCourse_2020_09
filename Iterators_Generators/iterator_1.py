# Iterálható sorozatok (iterables) és iterátorok (iterators)
# (Avagy: hogy működik a for ciklus)

# Iterálható: olyan elemsorozat, amelyet egy iterátor a next() függvény segítségével be tud járni.
# Iterátor: memóriával rendelkező elem, amely mindig tudja, hányadik elemnél tart, a next() függvényt
# alkalmazva rá visszaadja a következő elemet. Ha már nincs következő elem, akkor a next() StopIteration
# kivételt dob. Az iterátort az iter() függvénnyel hozzuk létre.

# Ezek nagyon fontos alapfogalmak; egy lista segítségével kezdjük az ismerkedést.

# A list típus iterálható.

lst = [10, 20, 30]

it = iter(lst)
print(it)  # <list_iterator object at 0x02865510>

# Létrejött egy iterátor objektum. Járjuk be vele a listát!

x = next(it); print(x) # 10
x = next(it); print(x) # 20
x = next(it); print(x) # 30
x = next(it); print(x) # --> exception

# Traceback (most recent call last):
#   File "test.py", line 8, in <module>
#     x = next(it); print(x)
# StopIteration

# Az iterátor csak egy irányban tudja bejárni egyesével a sorozatot, semmi más
# művelet nincs értelmezve rajta. Ha újra be akarjuk járni a sorozatot, újra
# létre kell hoznunk egy iterátort.

##################################

# Mit csinál az iter() függvény? Felhívja az iterálható elem __iter__() függvényét.

it = lst.__iter__()
print(it) # <list_iterator object at 0x02357B50>

# Az iter() függvény csak egy szintaktikai szépítés.

# Mit csinál a next() függvény? Felhívja az iterátor __next__() függvényét.

x = it.__next__(); print(x) # 10

# A next() függvény is csak egy szintaktikai szépítés.

##################################

# Ha saját iterálhatót és iterátort akarunk létrehozni, akkor az __iter__() és a __next__()
# metódusokat kell megvalósítani. Az __iter__()-nek egy olyan objektumot kell visszaadnia,
# ami eléri az iterálandó sorozatot; az iterátor __next__() metódusa pedig:

# * visszaadja a következő elemet, ha van ilyen, illetve
# * StopIteration kivételt dob, ha már nincs több elem.

##################################

# Hogy működik a for ciklus?

# 1. Létrehozza az iterálandó sorozat iterátorát.
# 2. Mindaddig hívja az iterátor __next__() metódusát, míg az StopIteration
#    kivételt nem dob.
# 3. Elkapja ezt a kivételt és kilép a ciklusból.

lst = [10, 20, 30]

it = iter(lst)
while True:
   try:
       x = next(it)
       print(x)
   except StopIteration:
       break

# 10
# 20
# 30

##################################
