# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# 1.)

x = [1, 2, 3]

for e in zip(x):
    print(e)

x = ('ABC', [1, 2, 3])

for e in zip(x):
    print(e)

for e in zip(*x):
    print(e)

######################################

# 2.)

# A.

def outer(*args):
    def intern_func(args):
        return sum(args)

    ret = intern_func(args)
    return ret + 3


x = outer(10, 20)
print(x)

# B.

def outer(*args):
    def intern_func(*args):
        return sum(args)

    ret = intern_func(args)
    return ret + 3


x = outer(10, 20)

# C.

def outer(*args):
    def intern_func(*args):
        return sum(*args)

    ret = intern_func(args)
    return ret + 3


x = outer(10, 20)
print(x)

# D.

def outer(*args):
    def intern_func(*args):
        return sum(*args)

    ret = intern_func(*args)
    return ret + 3


x = outer(10, 20)
print(x)

######################################

# 3.)

def outer_decor(param):
    def inner_decor(func):
        def wrapper(*args, **kwargs):
            ret_val = func(*args, **kwargs)
            if param == '+':
                ret_val += 10
            else:
                ret_val -= 10

            return ret_val

        return wrapper

    return inner_decor

@outer_decor('+')
def f_1(a, b):
    return a + b

@outer_decor('-')
def f_2(a, b):
    return a + b

print(f_1(3, 4))
print(f_2(3, 4))

######################################

# 4.)

# A.

def f1():
    print('f1 vagyok')

f2 = f1

id_1 = id(f1)
id_2 = id(f2)
print(id_1 == id_2)

f1.x = 10
f2.x = 20
print(f1.x, f2.x)

# B.

def func_factory():
    def func():
        print('func vagyok')

    return func

f1 = func_factory()
f2 = func_factory()

id_1 = id(f1)
id_2 = id(f2)
print(id_1 == id_2)

f1.x = 10
f2.x = 20
print(f1.x, f2.x)

######################################

# 5.)

# A.

def gen_1(param):
    for e in param:
        yield e.lower()

def gen_2(param):
    for x in param:
        yield 2 * x

x = gen_1('ABC')
y = gen_2(x)

for n in y:
    print(n, end='#')
print()

# B.

def gen_1(param):
    for e in param:
        if e in 'ABCD': continue
        yield e

def gen_2(param):
    for x in param:
        yield x.lower()

x = gen_1('XABYCZ')
y = gen_2(x)
z = ''.join(y)

print(z)

######################################

# 6.)

def func(param):
    param = sorted(param, key=lambda x: abs(x))

lst = [-20, 10, 15];
func(lst);

print(lst)

######################################

# 7.)

def f_1(param):
    return 2 * param

class C():
    def __call__(self, func, value):
        return func(value)

c = C()
y = c(f_1, 20)

print(y)

######################################

# 8.)

class C():
    def __init__(self, param):
        self.__p = param

    def append(self, value):
        self.__p.append(value)

    def get_p(self):
        return self.__p

lst = [10, 20]
c = C(lst)
c.append(-10)
x = c.get_p()
x.append(-20)

print(x)
print(lst[-2])

######################################

# 9.)

class C():
    def __init__(self, param):
        self.__p = param

    def __call__(self, value):
        return self.__p + value

x = 100
c = C(x)
y = c(-10)

print(y)

######################################

# 10.)

def func(param):
    func.a += param
    return func.a

f = func
f.a = 5
x = func(10)
print(x)
x = func(15)
print(x)

######################################

# 11.)

import numpy as np

arr = np.array([10.5, 20, 'Python', 30])
print(arr[0] + arr[1] + arr[3])

######################################

# 12.)

class Base:
    def func_b(self):
        print('func_b')

class Derived(Base):
    def func_d(self):
        print('func_d')

d = Derived()
d = [e for e in dir(d) if not e.startswith('__')]
print(d)

######################################

# 13.)

s = 'építő'
for c in s:
    print(hex(ord(c)),end=' ')  # 0xe9 0x70 0xed 0x74 0x151
print()

b = s.encode('UTF-8')
print(b, type(b)) # b'\xc3\xa9p\xc3\xadt\xc5\x91' <class 'bytes'>

# Mi az í betű Unicode kódja és UTF-8 kódja?

b = b't\xc3\xa9p\xc5\x91'
s = b.decode('UTF-8')
print(s, type(s))

######################################

# 14.)

s = 'kérő'
b = s.encode('ISO-8859-2')
print(type(b), len(b))

######################################

# 15.)

b_a = bytearray('ábcdé', 'UTF-8')
print(len(b_a))

s = b_a[2:4].decode('ISO-8859-2')
print(s)

######################################

# 16.)

b_1 = bytearray(' ', 'ISO-8859-1')
b_1[0] = 56
print(len(b_1))

b_1[0] += 200
print(len(b_1))

######################################

# 17.)

s_1 = 'őr'
b = s_1.encode('UTF-8')
print(len(b))
s_2 = str(b)
print(len(s_2))

######################################
