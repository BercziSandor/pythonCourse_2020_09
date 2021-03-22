# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# 1.)

# A.
# Mi a kimenet?

lst = [10, 20, 30]
for i, item in zip(range(len(lst)), lst):
    print(i, item) # ??

# B.
# Ez elég csúf megoldás. Írjunk szebbet!

################################################

# 2.)

def func(param):
  if isinstance(x, (list, tuple)):
      return len(param)

  if isinstance(x, (int, float)):
      return  100 * param

  return 42

x = (3)
y = func(x)
print(y)

################################################

# 3.)

def func(*args):
    for arg in *args:
        print(arg)
    print()

func(1,2,3)

################################################

# 4.)

def func(*args):
    for arg in args:
        print(arg)
    print()

func(1,2,3)

lst = [1,2,3]
func(lst)

tup = (1)
func(*tup)

################################################

# 5.)

def func(a,*kwargs):
    print(a)
    for key in kwargs:
        print(key)

func(1,b=2)

################################################

# 6.)

dic_1 = {'A': 1, 'B': 2}
dic_2 = {20: ('Q', 'W'), 30: [4, 5, 6]}
list = list(dic_1.items())
print(list)

list = list(dic_2.values())
print(list)

################################################

# 7.)

lst = [7, 8, 9]

for i in range(len(lst) - 1):
    print(lst[i])

################################################

# 8.)

lst = [7, 8, 9]

for i in range(len(lst)):
    print(lst[i])

# Hogy lehetne szebben ugyanezt?

################################################

# 9.)

class C:
    def __init__(self):
        self.__value = None

    def setValue(self, value):
        self.__value = value

    def getValue(self):
        return self.__value

c_1 = C()
c_1.setValue(10)
x = c_1.getValue()
print(x)

x = C.getValue(c_1)
print(x)

x = c_1.__class__.getValue(c_1)
print(x)

################################################

# 10.)

def func_1(param):
    if param > 10:
        return 0
    else:
        return 2

def func_2(param):
    return 5 * param

x = func_1(20) or func_2(20)
print(x)

################################################

# 11.)

import numpy as np

arr_1 = np.array([[1,2,3], [4,5,6], [7,8,9]])

# A.
print(arr_1.shape) #??

# B.
arr_2 = arr_1[:,-2]
print(arr_2) #??

# C.
arr_2 = arr_1[1:3,1:3]
print(arr_2) #??

# D.
arr_2 = arr_1[::-1]
print(arr_2) #??

# E.
arr_2 = arr_1[::-1,::-1]
print(arr_2) #??

################################################

# 12.)

import numpy as np

arr_1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr_1)

arr_2 = np.array([ row[i] for i, row in enumerate(arr_1) ])
print(arr_2) # ??

################################################

# 13.)

lst = [10, 20, 30]
it_1 = iter(lst)
it_2 = iter(it_1)
print(id(it_1) == id(it_2))

################################################

# 14.)

class Miez:
    def __init__(self, value):
        self.__value = value
        self.__index = 0

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__value):
            raise StopIteration

        index = self.__index
        self.__index += 2

        return self.__value[index] + 'e'

m = Miez('rágó')
for e in m:
    print(e, end='')

print()

################################################

# 15.)

def micsoda(value):
    index = 0
    while index < len(value):
        yield value[index] + 'e'
        index += 2

m = micsoda('rigó')
for e in m:
    print(e, end='')

print()

################################################

# 16.)

x = [None]
y = 0
z = {False}

if x and (y or z):
    print('123')
else:
    print('321')

###################################
