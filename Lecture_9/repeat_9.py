# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# 1.)

import numpy as np

arr_1 = np.array([
['x1.py', 'x1.html', 'x1.txt'],
['x2.cpp','x2.java', 'x2.html']
])

print(arr_1.shape)

arr_2 = arr_1[np.char.endswith(arr_1,'.html')]
print(arr_2)

x = np.where(np.char.endswith(arr_1,'.html'))
print(x[0], x[1])

for i, j in zip(x[0], x[1]):
    print(arr_1[i, j])

######################################

# 2.)

arr_1 = np.array([
[4, 5, 6],
[7, 8, 9]
])

arr_2 = arr_1[arr_1 * arr_1 > 40]
print(arr_2)

######################################

# 3.)

import numpy as np

arr_1 = np.array([
[4, 5, 6],
[7, 8, 9]
])

arr_2 = arr_1.reshape(6,)
print(arr_2)

######################################

# 4.)

from abc import ABC, abstractmethod

class Family(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def greet(self):
        pass

class Grandfather(Family):
    def greet(self):
        print('én vagyok a nagyapa')

class Father(Family):
    def greet(self):
        print('én vagyok az apa')

g = Grandfather()
g.greet()

f = Father()
f.greet()

class Somebody():
    def greet(self):
        print('én is vagyok valaki')

def func(params):
    for p in params:
        p.greet()

arr = [Grandfather(), Father(), Somebody()]
func(arr)

######################################

# 5.)

class C:
    def __init__(self, factor):
        self.factor = factor

    @property
    def factor(self):
        return self.__factor

    @factor.setter
    def factor(self, factor):
        if factor < 0:
            factor *= -1

        self.__factor = factor

c = C(-20)
print(c.factor)
c.factor = -10
print(c.factor)

######################################

# 6.)

# A.

def func(param):
    for e in range(param, 0, -2):
        yield(e)

g = func(8)
for x in g:
    print(x, end= ' ')
print()

# B.

g = func(-8)
for i, x in enumerate(g):
    print(x, end= ' ')
    if i > 4: break

######################################

# 7.)

def func(param):
    for e in range(param, 0, -1):
        if e % 2 == 0:
            yield(5 * e)
        else:
            return 10 * e

g = func(5)
for x in g:
    print(x, end= ' ')
print()

######################################

# 8.)

def my_coroutine(param):
    print('elindultam')
    while True:
        r = yield
        print('elteszem adatbázisba:', r + param)

g = my_coroutine(100)
lst = [10, 20, 30]

x = next(g) # beindítjuk

for e in lst:
    x = g.send(e)

######################################

# 9.)

import numpy as np

arr_1 = np.array([
[4, 5, 6],
[7, 8, 9]
])

arr_2 = np.array([
[40, 50],
[60, 70],
[80, 90]
])

arr = arr_1 + arr_2
print(arr)

arr = arr_1 + ???
print(arr)

# [[44 55 66]
#  [77 88 99]]

######################################
