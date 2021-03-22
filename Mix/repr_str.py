# __repr__ és __str__ dunder metódusok

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2,3)
print(p)  # <__main__.Point object at 0x01F758D0>

# Ez nem túl informatív. Készítsünk egy __str__ metódust a Point osztálynak.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point object, x = {self.x} y = {self.y}'

p = Point(2,3)
print(p)  # Point object, x = 2 y = 3

s = 'Az én pontocskám: ' + str(p)
print(s)  # Az én pontocskám: Point object, x = 2 y = 3

s = f'p: {p}'
print(s)  # p: Point object, x = 2 y = 3

# Ez ember számára jól olvasható; az __str__ metódusnak ez a célja.

#########################################

# A __repr__ metódus célja, hogy jól rekonstruálni lehessen az objektumot az általa
# kiadott sztring segítségével. Nincsenek rá vonatkozó szabályok; ez egy ajánlás:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point object, x = {self.x} y = {self.y}'

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

p = Point(2,3)
print(repr(p)) # Point(2, 3)

# repr() kimenetét bemásolva a terminál-ablakba létre tudunk hozni egy
# ugyanolyan objektumot.

# __repr__-nek az a feladata, hogy EGYÉRTELMŰEN reprezentálja az objektumot, pl.
# debuggoláshoz; __str__ feladata, hogy jól olvasható legyen.

#########################################

# Ha nincs __str__ metódus, de __repr__ van, akkor azt fogja a futtató rendszer használni
# az objektum sztringgé alakításához:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

p = Point(2,3)
print(repr(p)) # Point(2, 3)

#########################################

# A sztringgé alakításkor !r illetve !s formátumspecifikációval meg tudjuk adni,
# hogy melyik megjelenítési formát akarjuk használni:

s = f'p repr: {p!r} p str: {p!s}'
print(s) # p repr: Point(2, 3) p str: Point object, x = 2 y = 3

#########################################

# A beépített datetime típussal jól lehet szemléltetni a két metódus különbségét.

import datetime

today = datetime.datetime.now()

print(str(today))   # 2020-11-13 08:10:08.835484
print(repr(today))  # datetime.datetime(2020, 11, 13, 8, 10, 8, 835484)

#########################################

# Érdemes azt is megfigyelni, hogy sztringek megjelenítésénél repr() kiírja az
# aposztrofokat is:

s = 'abc'
print(s, repr(s)) # abc 'abc'

#########################################
