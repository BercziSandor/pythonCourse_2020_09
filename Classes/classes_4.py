# Hívható osztályok

# classes_2.py-ban láttunk egy egyszerű osztályt, amelynek egy (lényeges)
# metódusa van:

class MyClass():
    def __init__(self, factor):
        self.factor = factor

    def multiply(self, param):
        return param * self.factor

my_obj = MyClass(10)
x = my_obj.multiply(3)
print(x) # 30

# Az ilyeneknél érdemes lehet inkább egy hívható osztályt készíteni.

class MyMultiplier():
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, param):
        return param * self.factor

my_multiply = MyMultiplier(10)
x = my_multiply(3)
print(x) # 30

my_multiply.factor = 100
x = my_multiply(3)
print(x) # 300

# Így egy olyan függvényt készítettünk, amely képes bizonyos paramétereket megjegyezni,
# nem kell minden egyes hívásnál ezeket odaadni neki.

#########################################
#########################################

# LÁTOGATÁS A GÉPHÁZBAN (bound method, __class__ attribútum)

# Az itt következő hívási módokat nem szoktuk használni, csak azért lehet érdekes
# megnézni ezeket, hogy a Python működéséről megtanuljunk valamit.

# Amikor a my_multiply objektumot függvényként felhívjuk, akkor tulajdonképpen a
# __call__ metódusát hívjuk fel:

my_multiply.factor = 100

x = my_multiply(3)
print(x) # 300

x = my_multiply.__call__(3)
print(x) # 300

# Mi is ez a __call__ metódus?

print(my_multiply.__call__)
# <bound method MyMultiplier.__call__ of <__main__.MyMultiplier object at 0x004E5510>>

# Másképpen: a my_multiply OSZTÁLYÁNAK a __call__ metódusát hívjuk fel úgy, hogy
# első paraméterként az aktuális objektumot adjuk oda neki. Bound method: egy objektum
# példányhoz kötött metódus.

x = MyMultiplier.__call__(my_multiply, 3)
print(x) # 300

x = my_multiply.__class__.__call__(my_multiply, 3)
print(x) # 300

# Akár egy másik függvényre is átállíthatjuk a __call__ referenciát (ez nyilván
# nem hasznos, Ön az otthonában csak saját felelősségére próbálja ki):

def new_func(self, param):
    return param * self.factor + 9

MyMultiplier.__call__ = new_func
x = my_multiply(3)
print(x) # 309

# vagy:

my_multiply.__class__.__call__ = new_func
x = my_multiply(3)
print(x) # 309

# Ezeknek a részleteknek a megfigyelése segíteni fog megkülönböztetni az objektum-metódusokat
# az osztály-metódusoktól.

#########################################
