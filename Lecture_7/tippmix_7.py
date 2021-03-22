# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# 1.)

x = (lambda a,b: 2 * a + 3 * b)(2, 3)
print(x) # ??

######################################

# 2.)

def func(a,b,c):
    print(a,b,c)

dic = {'a': 1, 'b': 2, 'c': 3}
func(*dic)

######################################

# 3.)

def func(a=1, b=2, c=3):
   print(a,b,c)

dic = {'a': 1, 'b': 2, 'c': 3}
func(**dic)

######################################

# 4.)

def func(a=1, b=2, c=3):
   print(a,b,c)

dic = {'a': 1, 'b': 2}
func(**dic)

######################################

# 5.)

dic = {'a': 1, 'b': 2}
for key, value in dic:
    print(key, value)

######################################

# 5.)

def func():
    y = 1 /0

x = 'ok'
try:
    x = func()
except Exception:
    print(x)

######################################

# 6.)

dishes = ["pizza", "sauerkraut"]
countries = ["Italy", "Germany"]

country_specialities_zip = zip(dishes,countries)
print(list(country_specialities_zip))

country_specialities_dict = dict(country_specialities_zip)
print(country_specialities_dict)

######################################

# 7.)

x = 'This',
print(len(x))

######################################

# 8.)

from statistics import mean

def func():
    val = 1
    while val < 4:
        yield(val)
        val += 1

g = func()
print(mean(g))

######################################

# 9.)

def my_gen():
    print('I am my_gen')
    for i in (50, 60, 70):
        yield 2 * i

print('hello')
g = my_gen()
print('hello again')

######################################

# 10.)

import numpy as np

arr = np.array([10, '20', 30, 40])
print(arr[0].dtype)

######################################

# 11.)

import numpy as np

arr_1 = np.array([
['10', '20'],
['40', '50']
]
)

arr_2 = arr_1.astype(int) * 2
print(arr_2)

######################################

# 12.)

import numpy as np

arr_1 = np.array([
[10, 20],
[40, 50]
]
)

arr_2 = np.array([[100], [200]])
print(arr_1 + arr_2)

######################################

# 13.)

class C:
  def __init__(self, param):
      self.__param = param

  def func(self, x):
      print(self.__param * x)

c1 = C(20)
c2 = C(100)
C.func(c2, 3)
c2.__class__.func(c1, 10)

######################################

# 14.)

def func(param):
    yield param - 10
    yield param
    yield param + 10

g = func(100)
print(max(g))
print(sum(g))
print(min(func(100)))

######################################

# 15.)

lst = [10, 20, 30]
it = iter(lst)

for e in it:
    print(e)

for e in it:
    if e > 15:
        break
    print(e)

######################################

# 16.)

x = ['']
y = ''

# A.

if x and y:
    print('egy')
else:
    print('one')

# B.

if x or y:
    print('kettő')
else:
    print('two')

######################################
