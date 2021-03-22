# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# Órán a szabályok:
# Amikor valaki úgy gondolja, hogy van ötlete a megoldásra, akkor bemondja, hogy: VAN TIPP!
# Amikor azt mondom, hogy "Kérem a tippeket" és valaki egy kicsit még gondolkodni szeretne, akkor bemondja, hogy: IDŐT KÉREK!
# Egyébként pedig nyilván sorra mindenki bemondja, hogy mit gondolt ki.

###########################################################

# 1.

def f(x, y, z):
    print(x, y, z)

f(z=30, y=20, x=10)

###################

# 2.)

def f(x, y, z):
    print(x, y, z)

f(z=30, y=20, 10)

###################

# 3.)

lst = [3, (10, 20, 30),['A', 'B']]
print(lst[1][2])
print(lst[1],[2])

###################

# 4.)

lst = [3, (10, 20, 30),['A', 'B']]
print(len(lst[2][1]))
print(len(lst[1][2]))

###################

# 5.)

def f(x, y, z):
    print(x, y, z)

f(10, y=20, z=30)

###################

# 6.)

dic = {'a': 10, 'b': 20}
print(dic['B'])

###################

# 7.)

for i in range(1,2):
    print(10*i)

###################

# 8.)

def f(*, x, y, z):
    print(x, y, z)

f(10, y=20, z=30))

###################

# 9.)

x = 100
X = 10
print(x + X)

###################

# 10.)

for x in range(3, 1, -2):
    print(x)

###################

# 11.)

def f(x, y, z):
    print(x, y, z)

f(30, y=20, x=10)

###################

# 12.)

r = range(1, 4)
for x in r:
    print(x, end=' ')
print()

###################

# 13.)

def func(param):
    return y + param

y = 'abc'
print(func('xxx'))

y = [10, 20, 30]
print(func([99]))

y = (100)
print(func((5, 4, 3)))

###################

# 14.)

def func(param):
    y += 100
    return y + param

y = 30
print(func(1))

###################