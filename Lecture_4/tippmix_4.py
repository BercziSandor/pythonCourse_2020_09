# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# 1.)

def f_1(param):
    def inner():
        print(param, x)

    x = 'world'
    inner()

f_1('hello')

###################

# 2.)

set = {'A', 'B', 'B', 'C'}
print(set)

lst_1 = list(set)
print(lst_1)

print(set(lst_1))

###################

# 3.)

x = 'ABCDEF'
print(x[:-4:])
print(x[:-4:-2])

y_1 = x
y_2 = x[:]
print(y_1 is x, y_2 is x)

lst = list(x)
print(lst)

lst_1 = lst
lst_2 = lst[:]
print(lst_1 is lst, lst_2 is lst)

###################

# 4.)

def f_2(a, b):
    print(str(a) + str(b))

f_2(2, 3)

###################

# 5.)

def f_3(*args):
    print(len(args))

f_3(1, 2, 3, 4)
f_3(a=1, b=2)

###################

# 6.)

def f_1(x, y, z):
    print(x + y * z())

f_1(10, 2, lambda : 3)

###################

# 7.)

lst_1 = [10, 20, 30, 40]
lst_2 = [1, 20, 3, 30, 11]
lst_3 = [ 2 * x for x in lst_1 if x not in lst_2 ]
print(lst_3)

###################

# 8.)

x = None
y = None
if x == y:
    print('egyenlő')
else:
    print('különbözik')

###################

# 9.)

lst_1 = [10, 20, 30, 40]
lst_2 = [1, 20, 3, 30, 11]
lst_3 = [ 2 * str(x) for x in lst_1 if x not in lst_2 ]
print(lst_3)

###################

# 10.)

class X:
    def __init__(param):
        self.p = param

x1 = X(100)
print(x1.p)

###################

# 11.)

str_1 = 'ABCD'
lst_1 = ['A', 'BC', 'D', 'E', 'F']
lst_2 = [ e for e in str_1 if e in lst_1 ]
print(lst_2)

###################

# 12.)

class X:
    def __init__(self, param):
        self.p = 2 * param

x1 = X(110).p
print(x1)

###################

# 13.)

for i in range(2, 6, 2):
    print(i, end=' ')

print

for i in ('123'):
    print(2 * i, end=' ')

###################

# 14.)

def func(a, b, c):
    print(a + b - c)

func(*range(3))

###################

# 15.)

def func_1(a, b):
    def f():
        nonlocal y

        return a * y

    y = 'B' + b

    return f()

print(func_1(3, '6'))

###################

# 16.)

set_1 = {'A', 'B', 'C', 'D'}
set_2 = {'A', 'B'}

print(set_2 in set_1)

###################

# 17.)

lst = [10, -2, '100']
sorted(lst, key=abs)
print(lst)

###################
