# Saját context manager objektummal megvalósítva II.
# Kivételkezelés az __exit__ metódusban (__enter__ sikeres volt)

# Az előző, fájlolvasós példánál maradunk. Az osztály kódja egyelőre változatlan.

class MyReader:
    def __init__(self, path):
        self.path = path
        self.f_obj = None
        print('__init__')

    def __enter__(self):
        self.f_obj = open(self.path)
        print('__enter__')

        return self

    def __exit__(self, excType, excValue, excTraceback):
        self.f_obj.close()
        self.f_obj = None
        print('__exit__', excType, excValue, excTraceback)

    def readLine(self):
        return self.f_obj.readline()

with MyReader('van_ilyen.txt') as r:
    line = r.readLine()
    x = 1/0             # direkt létrehozunk egy kivételt
    print('with vége')

print('with után')

# __init__
# __enter__
# __exit__ <class 'ZeroDivisionError'> division by zero <traceback object at 0x0286B328>
#
# Traceback (most recent call last):
#   File "test.py", line 22, in <module>
#     x = 1/0
# ZeroDivisionError: division by zero

# Az __exit__() metódus végrehajtódott, majd a kivétel továbbdobódott; a futtató
# rendszer kapta el.

###########################################

# Ha az __exit__ metódus False vagy None értéket ad vissza, akkor az történik, amit fentebb
# láttunk: a kivétel továbbdobódik.

# Ha True a visszatérő érték, akkor a kivétel nem dobódik tovább, úgy folytatódik a program
# futása, mintha nem is lett volna kivételdobás.

    ...
    def __exit__(self, excType, excValue, excTraceback):
        self.f_obj.close()
        self.f_obj = None
        print('__exit__', excType, excValue, excTraceback)

        return True  # !!!
    ...

with MyReader('van_ilyen.txt') as r:
    line = r.readLine()
    x = 1/0
    print('with vége')

print('with után')

# __init__
# __enter__
# __exit__ <class 'ZeroDivisionError'> division by zero <traceback object at 0x0286B328>
# with után

###########################################

