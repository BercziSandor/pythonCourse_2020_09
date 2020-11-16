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

lst = [-1, None, 10, 100]
print(max(lst))

######################################

# 6.)

def func_1(param):
    for e in param:
        yield(e if e < 20 else 20)

def func_2(param):
    for e in param:
        if e % 3 == 0:
            yield -e
        else:
            yield e

lst = [18, 20, 21]

# A.

g_1 = func_1(lst)
g_2 = func_2(g_1)

for i in g_2:
    print(i)

# B.
g_1 = func_2(lst)
g_2 = func_1(g_1)

for i in g_2:
    print(i)

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

lst = (10, 20, 30)
s1 = Stupid(lst)

print(s1.nums[::-1])

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
