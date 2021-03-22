# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# 1.)

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

# 2.)

class MyException_1(Exception): pass

class MyException_2(MyException_1): pass

def func():
    raise MyException_1('dobok egy kivételt')

try:
    func()
except MyException_2:
    print('elkaptam egy kivételt')
finally:
    print('itt a vége')

######################################

# 3.)

def func(param):
    if param > 100:
        return 100
    else:
        yield 2 * param

g = func(101)
for x in g:
    print(x)

######################################

# 4.)

lst = [-1, None, 10, 100]
print(max(lst))

######################################

# 5.)

# A.

lst = [-1, None, 10, 100]

g = [ x for x in lst if x ]
print(max(g))

# B.

# Adjunk meg olyan adatokat, amelyekkel rossz eredményt ad.

# C.

# Javítsuk ki.

######################################

# 6.)

def func(param):
    if param > 10:
        raise ValueError('dobok egy kivételt')

    print('nem dobok')

for x in (5, 15):
    try:
        func(x)
    except Exception:
        print('elkaptam egy kivételt')
    finally:
        print('eléneklem a finálét')

######################################

# 7.)

g_1 = (x for x in 'ABCDEFG')
g_2 = (x for x in (1, 2, 3))
for i, j in zip(g_1, g_2):
    print(i, j)

######################################

# 8.)

companies = {
'CoolCompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
'CheapCompany' : {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}}

bad_comps = [x for x in companies if any(y<9 for y in companies[x].values())]
print(bad_comps)

# Fogalmazzuk meg szóban is, mit csinál!

######################################

# 9.)

import numpy as np

arr_1 = np.array([10, 20, 30])
arr_2 = arr_1[arr_1 > 10]
print(arr_2)

arr_2[0] = 99
print(arr_2)
print(arr_1)

######################################

# 10.)

import numpy as np

def func(arr, step):
    return arr[::step]

arr_1 = [10, 20, 30, 40]
arr_2 = func(arr_1, 2)
arr_2[1] = 99
print(arr_2)
print(arr_1)

arr_3 = np.array([10, 20, 30, 40])
arr_4 = func(arr_3, -2)
arr_4[1] = 99
print(arr_4)
print(arr_3)

######################################

# 11.)

# A.

def gen_f(param):
    print(gen_f.__name__, 'vagyok, param:', param)
    yield 3 * param

print('111')
g = gen_f(10)
print('222')
for e in g:
    print(e)

# B.

def gen_f(param):
    while param < 100:
        yield param
        param *= 3

g = gen_f(10)
for e in g:
    print(e)

# C.

def gen_f(param):
    while param < 100:
        received = yield param
        if isinstance(received, int):
           param += received

g = gen_f(10)
x = next(g)
print(x)

x = g.send(x)
print(x)

x = g.send(x)
print(x)

######################################

# 12.)

def func(param):
    param.append(99)
    p2 = param
    p2.append(100)
    param = param[:]
    param.append(101)

lst = [1]
func(lst)
print(lst)

######################################

# 13.)

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr[arr * arr > 10])

######################################

# 14.)

def f_1(param):
    if param % 9 == 0:
        return 1
    elif param % 8 == 1:
        return 2

def f_2(param):
    if not param:
        return 1
    elif param > 10:
        return 2

if f_1(66) == f_2(3):
    print('igen')
else:
    print('nem')

######################################

# 15.)

lst_1 = [10, 20, 30, 40, 50]
lst_2 = lst_1
lst_1 = [99, 100]
print(lst_1)
print(lst_2)


lst_1 = [10, 20, 30, 40, 50]
lst_2 = lst_1
lst_1[:] = [99, 100]
print(lst_1)
print(lst_2)

######################################

# 16.)

b_a = bytearray('abcde', 'UTF-8')
print(len(b_a))

x = b_a[2:50].decode('ISO-8859-1')
print(x, type(x))

######################################

# 17.)

b_1 = bytes('1', 'UTF-8')
b_2 = bytes('3', 'UTF-8')

print(b_1 + b_2)

######################################

# 17.)

b_1 = bytearray('őr', 'UTF-8')
print(len(b_1))
print(type(b_1[0]))

######################################

# 18.)

b_1 = bytearray('ö', 'UTF-8')
print(len(b_1))

x = b_1.decode('ISO-8859-1')
print(type(x))
print(len(x))

######################################

# 19.)

print(b'C' + b'+' * 2)

b_1 = b'satu'
b_2 = b'séta'

print(len(b_1) == len(b_2))

######################################
