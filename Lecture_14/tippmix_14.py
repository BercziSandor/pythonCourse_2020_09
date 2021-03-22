# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# 1.)

lst = [10, 20, 30]

for e in lst:
    e += 2

print(lst)

lst = [10, 20, 30]

for i, e in enumerate(lst):
    lst[i] += 2

print(lst)

######################################

# 2.)

def f(x):
    def f_1():
        print("bbb")
        x()

    return f_1

def f_2():
    print("aaa")

p = f(f_2)
p()

######################################

# 3.)

def d(f):
    def n(*args):
        return '$' + str(f(*args))
    return n

@d
def p(a, t):
    return a + a*t

print(p(100,0.1))

######################################

# 4.)

def func(param):
    param[0] = [99, 100]

lst_1 = [10, 20];
lst_2 = [lst_1, 'ABC']
func(lst_2)

print(lst_2)

######################################

# 5.)

def decor(func):
    def inner(*args, **kwargs):
        print('hello')
        return func(*args, **kwargs)

    return inner

sum = decor(sum)
print(sum((1, 2, 3)))

######################################

# 6.)

import numpy as np

x = np.array([1, 2])
x *= 2
print(x)

x = [1, 2]
x *= 2
print(x)

x = np.array([1, 2])
x += 2
print(x)

x = [1, 2]
x += 2
print(x)

######################################

# 7.)

def func(param):
    func.x += param

    return func.x

f = func
f.x = 100
print(f(2))
print(f(8))

######################################

# 8.)

class C():
    def __init__(self, p):
        self.param = p

    def __call__(self, value):
        return self.param * value + 100

print(C(3)(10))

######################################

# 9.)

import numpy as np

arr = np.array([np.NaN, 200, np.NaN, 300])
print(len(arr[arr != np.NaN]))

######################################

# 10.)

import numpy as np

arr = np.array([10, 20, 'C++', 100])

if arr[-1] == 100:
    print('IGEN')
else:
    print('NEM')

######################################

# 11.)

lst = [10, 20, 30]
x = sum([1 for e in lst])
print(x)
print(len(lst))

def func():
    for e in (10, 20, 30):
        yield e

x = sum(1 for e in func())
print(x)

print(len(func()))

######################################

# 12.)

# input.txt tartalma:

# line 1
# line 2

f_obj = open('input.txt')

print(list(f_obj))
print(tuple(f_obj))

f_obj.close()

######################################

# 13.)

x = ['0123401234']
y = ('0123401234')
print(len(x) + len(y))
print(len(x + y))

######################################

# 14.)

s = 'kérő'
b = s.encode('ISO-8859-1')
print(type(b), len(b))

######################################

# 15.)

class Valami:
    x = 100

    def __init__(self, X):
        self.x = self.x + X

v = Valami(10)
print(v.x, v.__class__.x)

######################################

# 16.)

b_1 = bytearray('1', 'ISO-8859_2')
b_2 = [7, 3, 4]

b_1[0] += b_2[0]
print(b_1.decode('UTF-8'))

######################################

# 17.)

b_1 = b'ABC'
b_2 = b'XY'
b_3 = b_1 + b_2
print(b_3)
print(type(b_3))
print(type(b_3[0]))

######################################

# 18.)

x = 'őr'.encode('UTF-8') + 'angyal'
if len(x) == 8:
    print('nyolc')
else:
    print('nem nyolc az!')

######################################

# 19.)

b_a = bytearray('20', 'ISO-8859-1')
print(b_a)   # bytearray(b'20')
for e in b_a:
   print(e, end=' ')
print()      # 50 48

b_a.append(50)
print(b_a)   # bytearray(b'202')
b_a[2] = 0x33
print(b_a)

######################################

# 20.)

str_1 = '!gvatI'
str_2 = ' eé  t'
x = ''.join([e[0] + e[1] for e in zip(str_1[::-1], str_2[::-1])]).rstrip()

print(x)

######################################
