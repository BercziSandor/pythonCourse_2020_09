# https://www.python-course.eu/python3_inheritance.php

# örököltetés, issubclass() függvény

# A leszármaztatott osztály mindent tud, amit az ős.

class Base:
    def base_function(self):
        print('base_function vagyok')

class Derived(Base):
    pass

d = Derived()
d.base_function()    # base_function vagyok

############################

# Meg persze tudni szokott mást is.

class Base:
    def base_function(self):
        print('base_function vagyok')

class Derived(Base):
    def derived_function(self):
        print('derived_function vagyok')

d = Derived()
d.base_function()    # base_function vagyok
d.derived_function() # derived_function vagyok

############################

# Az ős-osztály metódusait felül is lehet definiálni.

class Base:
    def base_function(self):
        print('base_function vagyok')

class Derived(Base):
    def base_function(self):
        print('base_function vagyok, felüldefiniálva')

b = Base()
b.base_function() # base_function vagyok

d = Derived()
d.base_function() # base_function vagyok, felüldefiniálva

############################

# Rá is tudunk kérdezni, hogy egy osztály egy másiknak leszármazottja-e.

print(issubclass(Derived, Base))     # True
print(issubclass(d.__class__, Base)) # True

############################

# Ha az ősnek van konstruktora, azt explicit módon fel kell hívni a leszármazott
# konstruktorában.

class Base:
    def __init__(self, valueBase):
        self.value_base = 3 * valueBase

class Derived(Base):
    def __init__(self, valueBase, valueDerived):
        super().__init__(valueBase)
        self.value_derived = valueDerived

d = Derived(10,20)
print(d.value_base, d.value_derived) # 30 20

############################
