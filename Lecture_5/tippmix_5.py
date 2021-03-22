# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# 1.)

def func_2(param):
    return 2 * param

def func():
    return func_2

f = func()
print(f(4)) # ??

###################################

# 2.)

from other_module import ffunc

print('2222')

# other_module tartalma:

print('1111')
def ffunc():
    print('ffunc vagyok')

###################################

# 3.)

x = ''.join([ e[1].lower() if e[0] > 0 else e[1] for e in enumerate('BUDAPEST') ])
print(x, type(x))

###################################

# 4.)

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

# 5.)

import subdir/other_module

print('BBB')

# other_module a subdir nevű alkönyvtárban van, a tartalma:

def ffunc():
    print('ffunc vagyok')

if __name__ == '__main__':
    print('AAA')

###################################

# 6.)

import math

def func():
    return math.sqrt

f = func()
print(f(25)) # ??

###################################

# 7.)

def func(*args):
    print(len(args))

tup = (1, 2, 3)
func(tup, *tup)

###################################

# 8.)

def func(**kwargs):
    print(len(kwargs))

dic = {'A': 1, 'B': 2, 'C': 3}
func(dic, **dic) # ??
func(**dic, x=7) # ??

###################################

# 9.)

from itertools import zip_longest

tup = (1, 2, 3, 4)
lst = ['a', 'b', 'c', 'd', 'e', 'f']
print(list(zip(tup, lst))) # ??

print(list(zip_longest(tup, lst))) # ??

###################################

# 10.)

class Valami:
    def __init__(self, x, y):
        self.__xy = x + y
        self.__z__ = x - y

v = Valami(4,5)
print(v.__z__) # ??
print(v.__xy)  # ??

###################################

# 11.)

def func():
    def inner(param):
        return param + 100

    return inner

f = func()
print(f(4)) # ??

###################################

# 12.)

def f(x, y):
    return 3*x, 4*y

r = f(20.5, 30.5)
print(type(r))

###################################

# 13.)

x = '|'.join('Hello \t\nworld'.split())
print(x)

###################################

# 14.)

lst = ['DC', 'AB']
x = [x for e in lst for x in e]
print(x)

###################################

# 15.)
# Ezt le is lehet futtatni.

# Rendezni akarunk egy szótárt.

dic = {'B': 1, 'A': 2}
dic_2 = dict(sorted(dic.items()))
print(dic_2)       # {'A': 2, 'B': 1}

# 3.6+ verziókban ez tökéletes megoldás. Korábbi verziókban mi lehetett a probléma vele?

###################################

# 16.)

def f(param):
    for e in param:
        if e < 0:
            e *= - 2

lst = [10, -20, 30]
f(lst)
print(lst)

###################################

# 17.)

lst = [False]
if lst:
    print('Csinálok valamit')
else:
    print('Csinálok valami mást')

###################################

# 18.)

x = 3
y = 8
z = []

# A.

if x and y and z:
    print('igen')
else:
    print('nem')

# B.

if x or y and z:
    print('igen')
else:
    print('nem')

# C.

if (x or y) and z:
    print('fekete')
else:
    print('fehér')

# D.

if (x and y) or z:
    print('1')
else:
    print('2')


# Kell-e mindig a zárójel? Ha nem, adjunk meg olyan x, y, z értékeket, amelyekkel
# más lesz az eredmény zárójellel és anélkül.

###################################
