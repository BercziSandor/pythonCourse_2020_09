# class és static metódusok
# osztály- és objektum-adattagok (adattag = attribútum)
# __del__() metódus alkalmazása
# gyár (factory) függvény vagy metódus

# https://realpython.com/instance-class-and-static-methods-demystified/
# https://www.geeksforgeeks.org/class-method-vs-static-method-python/
# https://www.programiz.com/python-programming/methods/built-in/classmethod
# https://www.python-course.eu/python3_class_and_instance_attributes.php

# https://realpython.com/factory-method-python/
# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html

class Test:
    def bound_method(self):
        # "szokásos", objektumhoz kötődő metódus

        print('bound_method vagyok, objektumom (self):', self)
        print('osztályom (self.__class__):', self.__class__)

    @classmethod
    def class_method(cls):
        print('class_method vagyok, ez az osztályom:', cls)

    @staticmethod
    def static_method():
        print('static_method vagyok, nem ismerem sem objektumomat, sem osztályomat')

t = Test()
print('az objektum:', t)    # az objektum: <__main__.Test object at 0x01E27BB0>
print('az osztály:', Test)  # az osztály: <class '__main__.Test'>

#-------------------------------------

# Az objektum ismeri a hozzá kötött metódusokat és az osztályát is:

t.bound_method()
# bound_method vagyok, objektumom (self): <__main__.Test object at 0x01E27BB0>
# osztályom (self.__class__): <class '__main__.Test'>

#-------------------------------------

# Az osztály persze ismeri az osztálymetódusokat:

Test.class_method()         # class_method vagyok, ez az osztályom: <class '__main__.Test'>

# Az objektum ismeri az osztályát, azaz rajta keresztül is felhívható az osztálymetódus:

t.class_method()            # class_method vagyok, ez az osztályom: <class '__main__.Test'>

# Ilyenkor tulajdonképpen ez történik, ennek a rövidített formáját írtuk le:

t.__class__.class_method()  # class_method vagyok, ez az osztályom: <class '__main__.Test'>

#-------------------------------------

# Az osztály és az objektum is ismeri az osztály static metódusait:

Test.static_method()        # static_method vagyok, nem ismerem sem objektumomat, sem osztályomat
t.static_method()           # static_method vagyok, nem ismerem sem objektumomat, sem osztályomat

########################################

# Osztály-attribútumok (adattagok)

class Test:
    class_data = 99  # osztály-szintű adattag

    def bound_method(self):
        print('bound_method, class_data OBJEKTUMOMON keresztül:', self.class_data)
        print('bound_method, class_data OSZTÁLYOMON keresztül:', self.__class__.class_data)

    @classmethod
    def class_method(cls):
        print('class_method, class_data:', cls.class_data)

    @staticmethod
    def static_method():
        print('static_method vagyok, class_data:', class_data) # hibás!

t = Test()
print('class_data Test osztályon keresztül:', Test.class_data) # 99
print('class_data t objektumon keresztül:', t.class_data, t.__class__.class_data) # 99 99

# Az osztály-szintű adattagokat az objektum- és az osztály-metódusok is látják:

t.bound_method()
# bound_method, class_data OBJEKTUMOMON keresztül: 99
# bound_method, class_data OSZTÁLYOMON keresztül: 99

Test.class_method() # class_method, class_data: 99

# A statikus metódusok persze ezeket nem látják:

t.static_method() # NameError: name 'class_data' is not defined

# A statikus metódusok olyan segédfüggvények, amelyek se nem olvassák, se nem módosítják
# az objektum és az osztály állapotát. Példa: sok metódus használ átszámítást Celsius
# fokról Fahrenheitbe és az erre szolgáló függvényt statikus metódusként definiáljuk.
# Ezel világossá tesszük, hogy csak az osztályon belül akarjuk használni. "Szabad"
# (modul szintű) függvényként akkor célszerűbb definiálni, ha máshol is alkalmazni akarjuk.

########################################

# Hozzunk létre több objektumpéldányt és legyenek bennük példányhoz kötött (bound)
# adattagok és osztály-szintű adattag is.

class Test:
    class_data = 99

    def __init__(self, boundData):
        self.bound_data = boundData

    def bound_method(self):
        print('bound_method, bound_data:', self.bound_data)
        print('bound_method, class_data:', self.class_data, self.__class__.class_data)

t_1 = Test(1)
t_2 = Test(2)

t_1.bound_method()
print('----')
t_2.bound_method()

# bound_method, bound_data: 1
# bound_method, class_data: 99 99
# ----
# bound_method, bound_data: 2
# bound_method, class_data: 99 99

# A példány-adattagok példányonként különbözőek lehetnek, az osztály-adattag közös.

# Amikor ezt írjuk:

print(t_1.class_data)

# akkor nem tudhatjuk, hogy a kapott eredmény a t_1 OBJEKTUM adattagja-e, vagy az OSZTÁLYÉ,
# amit ezzel a szintaktikával is elérhetünk, mintegy az objektumon keresztül nézve. Ebből
# néha kavarodás tud lenni, mint mindjárt látni fogjuk.

########################################

# Példa osztály-adattag használatára: számoljuk az elkészült példányokat.

class Test:
    number_created = 0

    def __init__(self):
        self.__class__.number_created += 1
        # self.number_created += 1  # így nem lesz jó! ld. lentebb

    def bound_method(self):
        print('eddig ennyi példány készült belőlem:', self.number_created)


t_1 = Test()
t_1.bound_method() # eddig ennyi példány készült belőlem: 1

t_2 = Test()
print('ennyi Test objektum készült:', Test.number_created)  # ennyi Test objektum készült: 2

print('----')
t_1.bound_method() # eddig ennyi példány készült belőlem: 2
t_2.bound_method() # eddig ennyi példány készült belőlem: 2

########################################

# Egy érdekes anomália: nem kívánt osztályattribútum --> objektumattribútum átalakulás.

class Test:
    number_created = 0

    def __init__(self):
        # self.__class__.number_created += 1  # így volt jó (ld. fentebb)
        self.number_created = self.number_created + 1 # !!!!!

    def bound_method(self):
        print('eddig ennyi példány készült belőlem:', self.number_created)

# Furcsa eredmények születnek:

t_1 = Test()
t_1.bound_method() # eddig ennyi példány készült belőlem: 1

t_2 = Test()
print('ennyi Test objektum készült:', Test.number_created)  # ennyi Test objektum készült: 0

print('----')
t_1.bound_method() # eddig ennyi példány készült belőlem: 1
t_2.bound_method() # eddig ennyi példány készült belőlem: 1

# A problémát az okozza, hogy az __init__ metódusban az értékadás jobboldalán az
# osztály-adattagot találja meg a fordító, ami nulla értékű, ehhez hozzáad egyet,
# és ebből készít EGY OBJEKTUM-ADATTAGOT. És ettől kezdve self.number_created már
# az objektum-adatot jelenti.

# Egészítsük ki néhány kiíratással az osztályt, ettől remélhetőleg világosabb lesz,
# hogy mi zajlik a háttérben.

class Test:
    number_created = 0

    def __init__(self):
        # self.__class__.number_created += 1  # így volt jó (ld. fentebb)
        self.number_created += 1
        print('__init__:', self.__class__.number_created, self.number_created)

    def bound_method(self):
        print('bound_method:', self.__class__.number_created, self.number_created)


t_1 = Test()       # __init__: 0 1
t_1.bound_method() # bound_method: 0 1

print('főprogram:', Test.number_created, t_1.__class__.number_created, t_1.number_created)
# főprogram: 0 0 1

# TANULSÁG: Ha osztály-adattagra akarunk hivatkozni, akkor ezt mindig explicit módon tegyük meg:

# self.__class__.number_created
# t1.__class__.number_created

# és nem így:

# self.number_created
# t1.number_created

# mert így világos, hogy mire gondoltunk.

########################################

# Legyen most az a feladat, hogy az aktuálisan LÉTEZŐ objektumokat tartsuk számon.
# Ehhez a __del__() metódusban csökkenteni kell a számlálót.

class Test:
    number_existing = 0

    def __init__(self):
        self.__class__.number_existing += 1

    def __del__(self):
        self.__class__.number_existing -= 1

    def bound_method(self):
        print('most ennyi példány van belőlem:', self.__class__.number_existing)


t_1 = Test()
t_2 = Test()

t_1.bound_method()  # most ennyi példány van belőlem: 2
print('ennyi Test objektum van:', Test.number_existing) # ennyi Test objektum van: 2

del(t_1)

t_2.bound_method()  # most ennyi példány van belőlem: 1
print('ennyi Test objektum van:', Test.number_existing) # ennyi Test objektum van: 1

#-----------------------------------

# Persze szebb ezt a metódust OSZTÁLY-SZINTEN definiálni és kifejezőbb nevet adni neki,
# továbbá az adattagot elrejteni a külvilág elől:

class Test:
    __number_existing = 0 # így nem látszik kifelé

    def __init__(self):
        self.__class__.__number_existing += 1

    def __del__(self):
        self.__class__.__number_existing -= 1

    @classmethod
    def number_objects(cls):
        print('most ennyi példány van belőlem:', cls.__number_existing)


t_1 = Test()
t_2 = Test()

t_1.number_objects()  # most ennyi példány van belőlem: 2

del(t_1)

t_2.number_objects()  # most ennyi példány van belőlem: 1

# Ez nem működik (és ennek örülünk):

# print('ennyi Test objektum van:', Test.__number_existing) # ennyi Test objektum van: 1

########################################

# FAKULTATÍV

# class method gyakori felhasználása: gyár (factory) metódus. Ezeket sok esetben
# "szabad" függvényként vagy statikus metódusként is meg tudjuk írni.

# Egy Person nevű osztály példányainak elkészítéséhez szükség van az illető nevére
# és életkorára (ld. az __init_() metódust), azaz tulajdonképpen egy másik konstruktort
# akarunk készíteni az osztályhoz.

# Szeretnénk egy olyan függvényt, ami a születési év ismeretében előállítja az
# objektumot (ld. a fromBirthYear() metódust).

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def __str__(self):
        return self.name + ' kora: ' + str(self.age)

person_1 = Person('Adam', 19)
print(person_1) # Adam kora: 19

person_2 = Person.fromBirthYear('John',  1985)
print(person_2) # John kora: 36

# Feltéve persze, hogy 2021-ben vagyunk.

########################################

# Másik példa gyár-metódusra: geometriai alakzatok létrehozása.

class Shape:
    @classmethod
    def createObject(cls, which, *args, **kwargs):
        which = which.lower().strip()
        if which == 'circle': return Circle(*args, **kwargs)
        if which == 'square': return Square(*args, **kwargs)

        raise ValueError(f'False shape specification: {which}')

class Circle(Shape):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        print(f'Circle született, középpont: {self.center}, sugár: {self.radius}')

class Square(Shape):
    def __init__(self, lowerLeftCorner, sideLength):
        self.lower_left_corner = lowerLeftCorner
        self.side_length = sideLength
        print(f'Square született, bal alsó sarok: {self.lower_left_corner}, oldalhossz: {self.side_length}')

c = Shape.createObject('circle', center=(2, 3), radius=1)
s = Shape.createObject('square', lowerLeftCorner=(6, 4), sideLength=1.5)

# Circle született, középpont: (2, 3), sugár: 1
# Square született, bal alsó sarok: (6, 4), oldalhossz: 1.5

########################################

# Egy valóságosabb példa: Egy objektumnak szüksége van egy adattag-objektumra, amely
# a tartalmát valamilyen formátumban egy sztringbe tudja írni. A megfelelő segéd
# objektumot egy gyár függvény vagy metódus állítja elő; az egyik fajta JSON formátumban
# tudja szerializálni az objektumot, a másik, XML formában, a harmadik YAML formában...

########################################
