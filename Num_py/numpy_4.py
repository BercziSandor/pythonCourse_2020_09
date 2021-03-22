# Logikai tömbműveletek, maszkolás, np.average, where, fancy indexing

# https://medium.com/better-programming/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d
# http://jalammar.github.io/visual-numpy/

# A broadcasting lehetővé teszi, hogy egy skalárt hozzáadjunk
# egy tömbhöz:

import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])
y = x + 10
print(y) # [11 12 13 14 15 16]

# Logikai műveletet is végezhetünk:

y = x > 3
print(y)  # [False False False  True  True  True]

y = x % 3 == 0
print(y) # [False False  True False False  True]

# Persze több dimenziós tömbökön is működik:

x = np.array([[1, 2, 3], [ 4, 5, 6]])

y = x % 3 == 0
print(y)

# [[False False  True]
# [False False  True]]

#############################

# Ha egy logikai kifejezéssel INDEXELJÜK a tömböt, akkor azokat az elemeket fogja
# kiadni egy egydimenziós tömbbben, amelyekre teljesül a feltétel. (Maszkolás.)

x = np.array([[1, 2, 3], [ 4, 5, 6]])

# A hárommal osztható elemek:

y = x[x % 3 == 0]
print(y) # [3 6]

# A kettőnél nagyobb elemek:

 y = x[x > 2]
print(y) # [3 4 5 6]

# A logikai kifejezésre persze ráállíthatok egy változót is:

greater_than_two = x > 2
y = x[greater_than_two]
print(y) # [3 4 5 6]

#############################

# Több tömböt is összehasonlíthatok:

x = np.array([[1, 2, 3], [ 4, 5, 6]])
y = np.array([[0, 1, 2], [ 5, 6, 7]])

z = x[x > y]
print(z) # [1 2 3]

#############################

# Adott tulajdonságú elemek INDEXEINEK megkeresése: where művelet.

arr = np.array([10, 20, 30, 10])
print(arr) # [10 20 30 10]

# Hol vannak 10 értékű elemek?

where_10 = np.where(arr == 10)
print(where_10) # (array([0, 3], dtype=int32),)

# Egy egy elemű tuple-t kaptunk (mert egydimenziós a tömb), amelynek
# a nulladik eleme tartalmazza azon idexeket, ahol a tömb megfelel a feltételnek.

indexes = where_10[0]
print('indexes:',indexes) # indexes: [0 3]

for index in indexes:
    print(index, arr[index])

# 0 10
# 3 10

# Magával a where által szolgáltatott index-tömbbel közvetlenül indexelni tudjuk
# az eredeti tömböt (fancy indexing):

print(arr[where_10]) # [10 10]

# A tömb módosítható is az indextömb segítségével:

arr[where_10] += 100
print(arr) # [110 20 30 110]

#############################

# where kétdimenziós tömböknél.

arr = np.array([[20, 10, 30], [40, 50, 10]])
print(arr)

# [[20 10 30]
# [40 50 10]]

where_10 = np.where(arr == 10)
print(where_10) # (array([0, 1], dtype=int32), array([1, 2], dtype=int32))

# Két elemű tuple-t kaptunk, az első a sorok indexeit tartalmazza, a második
# az oszlopokét.

rows = where_10[0]
cols = where_10[1]
print('rows:', rows, 'cols:', cols) # rows: [0 1] cols: [1 2]

for row, col in zip(rows, cols):
    print(f'arr[{row}, {col}] = {arr[row, col]}')

# arr[0, 1] = 10
# arr[1, 2] = 10

# Magával a where által szolgáltatott index-tömbbel közvetlenül indexelni tudjuk
# az eredeti tömböt (fancy indexing):

print(arr[where_10]) # [10 10]

# A tömb módosítható is az indextömb segítségével:

arr[where_10] += 100

print(arr)

# [[20 110 30]
# [40 50 110]]

#############################

# Keressük meg az átlagnál nagyobb elemeket:

x = np.array([[1, 2, 3], [ 4, 5, 6]])

# Az elemek átlaga:
print(np.average(x)) # 3.5

# Az átlagnál nagyobb elemek:

big_ones = x[x > np.average(x)]
print(big_ones) # [4 5 6]

# Az átlagnál nagyobb elemek indexei:

ix_big = np.where(x > np.average(x))
print(ix_big) # (array([1, 1, 1], dtype=int32), array([0, 1, 2], dtype=int32))

rows = ix_big[0]
cols = ix_big[1]
print('rows:',rows, 'cols:', cols) # rows: [1 1 1] cols: [0 1 2]

for row, col in zip(rows, cols):
    print(f'x[{row}, {col}] = {x[row, col]}')

# x[1, 0] = 4
# x[1, 1] = 5
# x[1, 2] = 6

# Az indexeknek akkor szokott jelentősége lenni, ha egy másik tömbben is tárolunk
# adatokat és az azonos indexűek tartoznak össze.

x = np.array([[1, 2, 3],
              [4, 5, 6]])
cities = np.array([['Budapest', 'Szolnok', 'Debrecen'],
                   ['Szeged', 'Eger', 'Sopron']])

for row, col in zip(rows, cols):
    print(cities[row, col], x[row, col])

# Szeged 4
# Eger 5
# Sopron 6

#############################

# A maszkolással előállított tömb másolat, NEM referencia (view).

arr_1 = np.array([10, 20, 30, 40, 50])
print(arr_1)   # [10 20 30 40 50]

arr_2 = arr_1[arr_1 % 20 == 0] # a hússzal osztható elemek
print(arr_2)   # [20 40]

arr_2[0] = 99
print(arr_2)   # [99 40]
print(arr_1)   # [10 20 30 40 50] -- nem változott

# ****** Amikor egy adatszerkezetet előállítunk egy másikból, MINDIG vizsgáljuk
# ****** meg, hogy másolat (copy) keletkezett-e, vagy referencia (view).

#############################

# Viszont a maszkolással kiválasztott elemeket módosítani is tudjuk.

x = np.array([[1, 2, 3],
              [4, 5, 6]])

# Legyen az a feladat, hogy az átlagnál nagyobb elemeket a maximális értékkel
# kell helyettesíteni.

avg =  np.average(x)
print(avg)

m = np.max(x)
x[x > avg] =  m
print(x) # 3.5

# [[1 2 3]
#  [6 6 6]]

#############################
