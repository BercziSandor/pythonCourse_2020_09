# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# Órán a szabályok:
# Amikor valaki úgy gondolja, hogy van ötlete a megoldásra, akkor bemondja, hogy: VAN TIPP!
# Amikor azt mondom, hogy "Kérem a tippeket" és valaki egy kicsit még gondolkodni szeretne, akkor bemondja, hogy: IDŐT KÉREK!
# Egyébként pedig nyilván sorra mindenki bemondja, hogy mit gondolt ki.

###########################################################

# 1.

def func(args):
    print(len(args))

func(10, 20, 30)

###################

# 2.)

def func_1(a, f):
    return a + f(a)

def func_2(param):
    return 3 * param

x = func_1(10, func_2)
print(x)

###################

# 3.)

def func_1(a):
    def f():
        print('2', a)

    print('3')

    return f

print('1')
x = func_1(10)
print('4')
x()

###################

# 4.)

lst = [10, 20, 30]
tup = ('A', 'B', 'C', 'D')

for x, y in (zip(lst, tup)):
    print(x, y)

###################

# 5.)

def func_1(a):
    def f():
        print('2')
        return 10 * a

    print('3')

    return f()

print('1')
x = func_1(8)
print(x)

###################

# 6.)

def f_1(f):
    return f(100)

x = f_1(lambda x: x + 10)

print(x)

###################

# 7.)

def f(*args):
    print(len(args))
    for arg in args:
        print(arg, end=' ')
    print()

tup_1 = (10, 20)
tup_2 = (77, 88)
f(tup_1 + tup_2)

###################

# 8.)

def f(a, b, c):
    for x in c:
        print(x(a, b))

def func_1(p1, p2):
    return p1 + p2

lst = [ func_1, lambda x, y: x - y]

f(100, 10, lst)

###################

# 9.)

def f(**kwargs):
    for x in kwargs:
        print(x, end=' ')
    print()

dic = {'X': 4, 'Y': 6}
f(a=2, b=3, **dic)

###################

# 10.)

lst = [10, -2, 100]
sorted(lst, key=abs)
print(lst)

###################

# 11.)

lst_1 = [1, 2, 3]
print(zip(lst_1))

###################

# 12.)

lst_1 = [1, 2, 3]
print(list(zip(lst_1)))

###################

# 13.)

def f(*args):
    print(len(args))
    for arg in args:
        print(arg, end=' ')
    print()

tup_1 = (10, 20)
tup_2 = (77, 88)
f(*(tup_1 + tup_2))

###################

# 14.)

lst_1 = [('A', 10), ('B', 20), ('C', 30)]
x = list(zip(*lst_1))
print(x)

###################

# 15.)

lst_1 = [('A', 10), ('B', 20), ('C', 30)]
x = list(zip(lst_1))
print(x)

###################
