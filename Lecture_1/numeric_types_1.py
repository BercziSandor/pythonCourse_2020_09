# *** Egész számok (int)

x = 100
print(x, type(x))  # 100 <class 'int'>

# Tetszőlegesen nagy lehet

x = 10000000000000000000000000000000000000000000000000
y = x + 1
print(y)   # 10000000000000000000000000000000000000000000000001

# Alulvonásokkal tagolhatjuk a jobb olvashatóság érdekében

x = 100_000
print(type(x), 2 * x)  # <class 'int'> 200000

# Osztás, egész-osztás, maradékképzés

x = 11 / 4
y = 11 // 4
z = 11 % 4
print(x, y, z)   # 2.75 2 3   // kerekít!

# Hatványozás

x = 2 ** 8
y = 2 ** -2
print(x, y)    # 256 0.25

# += operátor (addition assignment, inkrementálás operátor, összeadás rekurzív operátor)

x = 10
x += 1
print(x)  # 11

# -= operátor (subtraction assignment, dekrementálás operátor, kivonás rekurzív operátor)

x = 10
x -= 1
print(x)  # 9

# *** Valós számok (float)

x = 10.0
y = x / 2
print(type(y), y)  # <class 'float'> 5.0

# Valós --> int

x = 5.6
y = int(x)
print(x, y)    # 5.6 5  csonkít, nem kerekít

y = round(x)
print(y, type(y))      # 6 <class 'int'> kerekít és int-re alakít
