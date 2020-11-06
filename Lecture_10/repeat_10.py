# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# 1.)

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

g_1 = (x for x in 'ABCDEFG')
g_2 = (x for x in (1, 2, 3))
for i, j in zip(g_1, g_2):
    print(i, j)

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
