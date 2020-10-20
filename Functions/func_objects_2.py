# Függvény-objektumok 2.

# Attribútumokat adunk a függvénynek.

# Classes\classes_4.py-ban láttunk egy példát hívható osztályra:

class MyMultiplier():
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, param):
        return param * self.factor

my_multiply = MyMultiplier(10)
x = my_multiply(3)
print(x) # 30

# Egyszerűbb ehelyett egy függvényt definiálni, amelynek adunk majd egy factor
# attribútumot:

def my_multiply(param):
    return my_multiply.factor * param

my_multiply.factor = 10
x = my_multiply(3)
print(x) # 30

my_multiply.factor = 100
x = my_multiply(3)
print(x) # 300

# Sokkal áttekinthetőbb a dolog, hiszen csak egy függvényre van szükségünk, az osztályt
# kényszerből definiáltuk, akkor lenne rá feltétlenül szükség, ha függvénynek nem tudnánk
# attribútumot adni.

# De Pythonban tudunk!

# Ilyen módon is egy olyan függvényt készítettünk, amely képes bizonyos paramétereket megjegyezni,
# nem kell minden egyes hívásnál ezeket odaadni neki.

#################################

# A fenti megoldás szépséghibája, hogy a függvény nem hívható, amíg nem kapott factor
# attribútumot:

def my_multiply(param):
    return my_multiply.factor * param

x = my_multiply(3)

# Traceback (most recent call last):
#   File "test.py", line 4, in <module>
#     x = my_multiply(3)
#   File "test.py", line 2, in my_multiply
#     return my_multiply.factor * param
# AttributeError: 'function' object has no attribute 'factor'

# Eredmény helyett egy kifejezetten barátságtalan hibajelzést kapunk.

# Szebb megoldás, ha a függvény magának beállítja a factor attribútumot, amennyiben
# az még nincs definiálva; például célszerűen 1-re vagy 0-ra.

def my_multiply(param):
    if not hasattr(my_multiply,'factor'):
        my_multiply.factor = 1

    return my_multiply.factor * param

x = my_multiply(3)
print(x) # 3

#################################
#################################

# LÁTOGATÁS A GÉPHÁZBAN

# Függvény-objektumok esetében is a __call__ metódust hívjuk fel (illetve hívja
# fel a futtató rendszer), hasonlóan a hívható osztályokhoz.

my_multiply.factor = 100
x = my_multiply(3)
print(x) # 300

x = my_multiply.__call__(3)
print(x) # 300

# my_multiply.__call__ típusa itt más:

# <method-wrapper '__call__' of function object at 0x005A18E8>

# és nem tudjuk átállítani egy másik függvényre (ami persze előny).

#################################
