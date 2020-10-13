# Objektum-metódusok

# Az objektumok általában rendelkeznek olyan függvényekkel, melyek hozáférnek
# az objektum adattagjaihoz és függvényeihez; ezeket metódusoknak hívjuk.

class MyClass():
    def __init__(self, factor):
        self.factor = factor

    def multiply(self, param):
        return param * self.factor

my_obj = MyClass(10)
x = my_obj.multiply(3)
print(x) # 30

#######################################

# Docstring-gel elláthatjuk magát az osztályt és a metódusait is:

class MyClass():
    '''Nagyon ügyes dolgokat tud'''
    def __init__(self, factor):
        '''A factor-ral fogok majd szorozni'''
        self.factor = factor

    def multiply(self, param):
        'Ez meg a szorzó maga'
        return param * self.factor

my_obj = MyClass(10)

print(help(my_obj))

# class MyClass(builtins.object)
#  |  Nagyon ügyes dolgokat tud
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, factor)
#  |      A factor-ral fogok majd szorozni
#  |
#  |  multiply(self, param)
#  |      Ez meg a szorzó maga
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)

#######################################

# Kvázi-private adattagok:

class MyClass():
    def __init__(self, factor):
        self.__factor = factor
        
    def multiply(self, param):
        return param * self.__factor
my_obj = MyClass(10)
#x = my_obj.__factor
print(my_obj._MyClass__factor)

# Ha csak egy alulvonással kezdődik a név, az azt jelzi, hogy ez is alapvetően
# belügye az osztálynak, kívülről ne piszkáljuk. Az egy és két alulvonás közti
# különbségre az örökléssel kapcsolatban még visszatérünk.

#######################################

# Fontos tulajdonsága a MyClass osztálynak, hogy egyetlen, a külvilág számára szánt
# metódusa van. Az ilyen fajta osztályok megvalósítási módjaira többször vissza fogunk
# térni.

#######################################
