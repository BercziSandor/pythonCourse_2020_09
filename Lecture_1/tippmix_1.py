# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# Órán a szabályok:
# Amikor valaki úgy gondolja, hogy van ötlete a megoldásra, akkor bemondja, hogy: VAN TIPP!
# Amikor azt mondom, hogy "Kérem a tippeket" és valaki egy kicsit még gondolkodni szeretne, akkor bemondja, hogy: IDŐT KÉREK!
# Egyébként pedig nyilván sorra mindenki bemondja, hogy mit gondolt ki.

###########################################################

# 1.

x = 6
print(type(6//2))

###################

# 2.)

lst = [1, ['A', 2], 'B', (3, 4, 5), 4.5]
print(len(lst))

###################

# 3.)

x = [1, 2, 3]
x.append([4, 5, 6])
print(len(x))

###################

# 4.)

x = "ABCD"
x[1] = "a"
print(x)

###################

# 5.

# A sztringeknél nincs append metódus. Miért?

###################

# 6.)

x = [1, 2, 3]
x[3] = 99
print(len(x))

###################

# 7.)

x = [1, 2, 3]
x[0] = [10, 20]
print(len(x))

###################

# 8.)

def f(x, y, z):
    return x + y - z

print(f(z=20, x=10, y=30))

###################

# 9.)

x = [1, 2, 3]
y = [2, 3]
print(y in x)

###################

# 10.)

x = (10, 20, 30)
y = [100, 200]
z = x + y
print(x)

###################

# 11.)

def f_1(x, y, z):
    return x + y - z

print(f_1(x=20, y=10, 30))

###################

# 12.)

def f_1(x=10, y=100, z=200):
    return x + y - z

print(f_1(y=10, z=30))

###################

# 13.)

def f_1(x, y, z):
    ret = (x + y)
    ret.append(3 * z)

    return ret

lst_1 = [10, 20]
lst_2 = [10, 20]
lst_3 = [90]

print(f_1(lst_1,lst_2, lst_3))

###################
