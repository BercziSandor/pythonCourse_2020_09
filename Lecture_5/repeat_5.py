# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# 1.)
# Ezt le is lehet futtatni.

# Rendezni akarunk egy szótárt.

dic = {'B': 1, 'A': 2}
dic_2 = dict(sorted(dic.items()))
print(dic_2)       # {'A': 2, 'B': 1}

# 3.6+ verziókban ez tökéletes megoldás. Korábbi verziókban mi lehetett a probléma vele?

###################################

# 2.)

def func_2(param):
    return 2 * param

def func():
    return func_2

f = func()
print(f(4)) # ??

###################################

# 3.)

def func():
    def inner(param):
        return param + 100

    return inner

f = func()
print(f(4)) # ??

###################################

# 4.)

import math

def func():
    return math.sqrt

f = func()
print(f(25)) # ??

###################################

# 5.)

def func(*args):
    print(len(args))

tup = (1, 2, 3)
func(tup, *tup)

###################################

# 6.)

def func(**kwargs):
    print(len(kwargs))

dic = {'A': 1, 'B': 2, 'C': 3}
func(dic, **dic) # ??
func(**dic, x=7) # ??

###################################

# 7.)

from itertools import zip_longest

tup = (1, 2, 3, 4)
lst = ['a', 'b', 'c', 'd', 'e', 'f']
print(list(zip(tup, lst))) # ??

print(list(zip_longest(tup, lst))) # ??

###################################

# 8.)

class Valami:
    def __init__(self, x, y):
        self.__xy = x + y
        self.__z__ = x - y

v = Valami(4,5)
print(v.__z__) # ??
print(v.__xy)  # ??

###################################

# 9.)

class Miez:
    def __init__(self, value):
        self.__value = value
        self.__index = len(self.__value) - 1

    def __iter__(self):
        self.__index = len(self.__value) - 1
        return self

    def __next__(self):
        if self.__index < 0:
            raise StopIteration

        index = self.__index
        self.__index -= 1

        return self.__value[index].lower()

m = Miez('PYTHON')
for e in m:
    print(e, end='')

print()

###################################
