# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# 1.)

def func_1():
    for i in range(1, 4):
        yield(10 * i)

def func_2(f):
    return max(f()) - min(f())

print(func_2(func_1))

######################################

# 2.)

import numpy as np

books = np.array([['Coffee Break NumPy', 4.6],
['Lord of the Rings', 5.0],
['Harry Potter', 4.3],
['Winnie-the-Pooh', 3.9],
['The Clown of God', 2.2],
['Coffee Break Python', 4.7]])

print(books[:,1])

######################################

# 3.)

import numpy as np

books = np.array([
['Coffee Break NumPy', 4.6],
['Lord of the Rings', 5.0],
['Harry Potter', 4.3],
['Winnie-the-Pooh', 3.9],
['The Clown of God', 2.2],
['Coffee Break Python', 4.7]
])

print(books.dtype) # <U19 miért?

lst = books[:,1]
print(lst)
print(lst.dtype) # <U19 miért?

lst_num = lst.astype(float)
print(lst_num)
print(lst_num.dtype)

lst_num = lst.astype(np.float32)
print(lst_num)
print(lst_num.dtype)

lst = [ x[0] for x in books if x[1].astype(float) > 4.6 ]
print(lst)

######################################

# 4.)

import numpy as np

books = np.array([
['Coffee Break NumPy', 4.6],
['Lord of the Rings', 5.0],
['Harry Potter', 4.3],
['Winnie-the-Pooh', 3.9],
['The Clown of God', 2.2],
['Coffee Break Python', 4.7]
])

lst = books[books[:,1].astype(float) > 4.6]
print(lst[:,0])

######################################

# 5.)

lst = [10, 20, 30, 40]
print(lst[::-2] + lst[-2::-2])

######################################

# 6.)

def f(x):
    def f1(*args, **kwargs):
        print("*" * 5)
        x(*args, **kwargs)
        print("*" * 5)
    return f1

def a(x):
    def f1(*args, **kwargs):
        print("%" * 5)
        x(*args, **kwargs)
        print("%" * 5)
    return f1

@f
@a
def p(m):
    print(m)

p("hello")

######################################

# 7.)

lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
id_orig = id(lst_1)

lst_1[:] = lst_2
id_new = id(lst_1)
print(id_new == id_orig)

lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
id_orig = id(lst_1)

lst_1 = lst_2[:]
id_new = id(lst_1)
print(id_new == id_orig)

######################################

# 8.)

class Stupid:
    def __init__(self, numbers):
        self.nums = numbers

lst = [10, 20, 30]
s1 = Stupid(lst)

print(s1.nums)

lst[0] = 99
s2 = Stupid(lst)
print(s2.nums[0] - s1.nums[0])

######################################

# 9.)

class Stupid:
    def __init__(self, numbers):
        self.nums = numbers[:]
        if len(self.nums) > 2:
            self.nums[0] *= -1

lst = [10, 20, 30] # (10, 20, 30)
s1 = Stupid(lst)

print(s1.nums[::-1])
print(lst[::-1])

######################################

# 10.)

str = '0' * 2 + str(7)
print(str)

print(True == 1)

print(str(True) == 1)

######################################

# 11.)

s = 'é'
b = s.encode('utf-8')
print(len(s), len(b))

######################################

# 12.)

def func(x):
    return x * x

lst = [1, -2, -4, 3]

map_obj = map(func, lst)
if max(map_obj) < 25:
    print(sum(map_obj))
else:
    print(lst[0])

######################################

# 13.)

class X():
    def __init__(self, value):
        self.val = value
        self.val.sort()

    def m(self):
        self.val[-1] = 99

lst = [20, 15, 10];
x = X(lst)
x.m()
print(lst[1:])

######################################

# 14.)

import numpy as np

arr = np.array([10, np.NaN, 20, np.NaN])
lst = list(e for e in arr if e != np.NaN)
print(len(lst))

######################################

# 15.)

lst_1 = [10, 20, 30, 40, 50]
lst_2 = lst_1

lst_1 = [99, 100]
print(lst_2)

lst_1 = [10, 20, 30, 40, 50]
lst_2 = lst_1

lst_1[:] = [99, 100]
print(lst_2)

######################################

# 16.)

def c(f):
    def inner(*args, **kargs):
        inner.co += 1
        return f(*args, **kargs)
    inner.co = 0
    return inner
@c
def fnc():
    pass
if __name__ == '__main__':
    fnc()
    fnc()
    fnc()
    print(fnc.co)

######################################

# 17.)

b_a = bytearray('abc', 'ascii')
print(b_a) # bytearray(b'abc')

for i in range(len(b_a)):
    b_a[i] += 1

b = bytes(b_a)
print(b)

for i in range(len(b)):
    b[i] += 1

print(b)

######################################

# 18.)

print(b'Nagyon j' + b'ó' * 4)

######################################
