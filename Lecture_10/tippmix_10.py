# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# 1.)

# A.

def func_1(p):
    return p + 20

def func_2():
    x = 1
    while x < 10:
        yield x
        x *= 2

map_obj = map(func_1, func_2())

print(list(map_obj))


# B.

def func_1(p):
    return p + 20

def func_2(p_2):
    x = 1
    while x < 10:
        yield x
        x *= p_2

map_obj = map(func_1, func_2(3))

print(tuple(map_obj))

######################################

# 2.)

class Valami:
    def __init__(self):
        self._x = 77
        self.__y = 88

v = Valami()
print(v._x)

print(v.__y / 2)

######################################

# 3.)

class Valami:
    def __init__(self):
        self._x = 77

    def func(p1, p2):
        p1._x = p2
v = Valami()
v.func(99)
print(v._x)

######################################

# 4.)

def func(param, f_lst):
    for f in f_lst:
        print(f(param))

x = (10, 20, 30)
y = [min, max, sum]

func(x, y)

######################################

# 5.)

class Base:
    def func(self, param):
        return 2 * param

class Derived(Base): pass

d = Derived()
x = d.func(10)
print(x)

######################################

# 6.)

class Base:
    def func(self, param):
        return 2 * param

class Derived(Base):
    def func(self, param):
        return super().func(param) + 2

d = Derived()
x = d.func(10)
print(x)

######################################

# 7.)

def func(param):
    for e in param:
        yield e

g = func('ABC')
for x in g:
    print(x)

######################################

# 8.)

x = (x * x for x in range(5))
print(x)

######################################

# 9.)

def func(param):
    if param > 100:
        yield 100
    else:
        yield 2 * param

for i in (101, 99):
    print(func(i))

######################################

# 10.)

g = (x for x in (1, 2, 3))
print(min(g))
print(sum(g))

######################################

# 11.)

lst = ['2', '4', '3', '10', '9']

print(lst.sort())

print(sorted(lst))

######################################

# 12.)

x = [range(5)]
print(x)

x = list(range(5))
print(x)

######################################

# 13.)

def dob():
    print('dobálok')
    raise Exception('dobok egy kivételt')

try:
    dob()
except ValueError:
    print('elkaptam egy kivételt')
finally:
    print('itt a vége')

######################################

# 14.)

arr = [20, 30, 40, 10]
ix = [3, 0, 1, 2]
a = sorted(ix, key=lambda e: arr[e])

lst = [arr[i] for i in a]
print(lst)

# Így is lehet, tömörebb, de esetleg nehezebben érthető;
# BIZTOSAN nehezebben (egyáltalán nem) debuggolható:

lst = [arr[i] for i in sorted(ix, key=lambda e: arr[e])]
print(lst)

######################################

# 15.)

lst = [10, 20, 30, 40, 50]
lst[2:40] = [-2, -3, -4]
print(lst)

lst = [10, 20, 30, 40, 50]
lst[-3:-1] = [99]
print(lst)

lst = [10, 20, 30, 40, 50]
lst[-2:40] = [-2, -3, -4]
print(lst)

######################################
