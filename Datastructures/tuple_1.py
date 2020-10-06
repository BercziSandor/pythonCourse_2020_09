# Tuple 1.

# https://www.python-course.eu/python3_sequential_data_types.php

# Olyan, mint a lista, csak fix, immutábilis.
# Magyar nevét nem találtam. (tupli?)

x = (10, 20, 30)
print(x, type(x), len(x))  # (10, 20, 30) <class 'tuple'> 3

# A hosszat ugyanúgy a len() függvénnyel kérdezzük le, mint a sztringeknél és a listáknál.

# Különféle típusú elemeket tartalmazhat

x = (10, 'John', 32.5)  # (10, 'John', 32.5)
print(x)

Nemcsak alaptípusokat tartalmazhat, hanem listát, tuple-t és egyéb összetett típusokat is .

x = (1, 'AA', (10, 'DD'), [20, 30, (9, 10)])
print(x, len(x))  # (1, 'AA', (10,'DD'), [20, 30, (9, 10)]) 4

# Egy elemű tuple:

x = (2,)  # a vessző fontos

# Így csak egy bezárójelezett int:

x = (2)
print(x, type(x))  # 2 <class 'int'>

# Indexelhető

x = (10, 'John', 32.5)
print(x[0], x[len(x) - 1])  # 10 32.5

# for ciklussal bejárható, iterálható

for e in x:
    print(e, end=' ')  # 10 John 32.5
print()

# Nem módosítható

x[1] = 'Jane'

# Traceback (most recent call last):
#   File "test.py", line 37, in <module>
#     x[1] = 'Jane'
# TypeError: 'tuple' object does not support item assignment

# Ezért aztán append metódusa sincs

x.append('new item')

# Traceback (most recent call last):
#   File "test.py", line 46, in <module>
#     x.append('new item')
# AttributeError: 'tuple' object has no attribute 'append'

# Ugyanezért a del függvény sem alkalmazható egy elemére.

del(x[1])

# Traceback (most recent call last):
#   File "test.py", line 2, in <module>
#     del(x[1])
# TypeError: 'tuple' object doesn't support item deletion

# Konkatenálás

# Hiba:

x = (1, 2, 3)
y = x + 4

# Traceback (most recent call last):
#   File "test.py", line 68, in <module>
#     y = x + 4
# TypeError: can only concatenate tuple (not "int") to tuple

x = (1, 2, 3)
y = x + (4, 5)
print(y)  # (1, 2, 3, 4, 5)

# Persze az eredeti változó is mutathat a megnövelt tuple-ra, ha az eredeti
# tuple-ra már nincs szükség:

x = (1, 2, 3)
x = x + (4, 5)
print(x)  # (1, 2, 3, 4, 5)

# += operátor (addition assignment, inkrementálás operátor, összeadás rekurzív operátor)

x = (1, 2, 3)
x += (4, 5)
print(x)  # (1, 2, 3, 4, 5)

# x = x + (4, 5) és x += (4, 5) PONTOSAN ugyanazt csinálja.

x = (1, 2, 3)
id_1 = id(x)
x += (4, 5)
id_2 = id(x)
print(id_1, id_2)  # 37013584 35223760

# Az inkrementáló operátor hatására is más memóriacímre kerül a tuple. Miért?
# A list-nél ez nem így volt (ld. list_2.py).

#################

# Tartalmazásvizsgálat: in operátor

x = ('A', 'B', 'C')
print('B' in x, 'D' in x)  # True False

##################

# Sztring átalakítása tuple-á:

x = 'ABC'
y = tuple(x)
print(y)  # ('A', 'B', 'C')

# Lista átalakítása tuple-ba és vissza:

x = [1, 2, 3]
y = tuple(x)
z = list(y)
print(y, z)  # (1, 2, 3) [1, 2, 3]

# Ez csak iterálható típusokkal működik, ez nem megy:

x = 2
y = list(x)

# Traceback (most recent call last):
#   File "test.py", line 2, in <module>
#     y = list(x)
# TypeError: 'int' object is not iterable

# Az, hogy az összetett típusokat könnyen tudjuk egymásba alakítani: NAGYON nagy előny.
# Az adatszerkezetek egymásba alakítását tudatosan érdemes tanulni.
