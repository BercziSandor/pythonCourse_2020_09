# Tömb alapműveletek, broadcasting, astype, tömbforgatás, elemek törlése

# https://medium.com/better-programming/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d
# http://jalammar.github.io/visual-numpy/
# https://www.w3resource.com/numpy/manipulation/index.php
# https://www.w3resource.com/python-exercises/numpy/index-array.php

# Azonos formájú tömböknél elemenként hajtja végre a műveletet.

import numpy as np


arr_1 = np.array([10, 20, 30])
arr_2 = np.array([100, 200, 300])

arr = arr_1 + arr_2
print(arr) # [110, 220, 330]

# MÁST JELENT a + művelet, mint Python iterálhatóaknál!

lst_1 = [10, 20, 30]
lst_2 = [100, 200, 300]

print(lst_1 + lst_2) # [10, 20, 30, 100, 200, 300]

#############################

# Két dimenziós példa:

arr_1 = np.array([
[10, 20, 30],
[40, 50, 60]
]
)

arr_2 = np.array([
[100, 200, 300],
[400, 500, 600]
]
)

arr = arr_1 + arr_2
print(arr)

# [[110, 220, 330],
# [440, 550, 660]]

#############################

# Ha sokszorozással egyforma alakra lehet hozni a kettőt, akkor ezt teszi (broadcasting):

arr_1 = np.array([
[10, 20, 30],
[40, 50, 60]
]
)

arr = arr_1 * 2
print(arr)

# [[ 20  40  60]
#  [ 80 100 120]]

# 2 ==> [
#       [2, 2, 2],
#       [2, 2, 2]
#       ]

arr = arr_1 + [2,3,4]
print(arr)

# [[12 23 34]
#  [42 53 64]]

# [2,3,4] ==> [
#             [2,3,4]
#             [2,3,4]
#             ]

arr = arr_1 + [
      [2],
      [3]]
print(arr)
# [[12 22 32]
#  [43 53 63]]

# [            [
#  [2],  ==>     [2, 2, 2],
#  [3]           [3, 3, 3]
# ]            ]

#############################

# Típuskonverzió, astype

arr_1 = np.array([10, 20, 30])
arr_2 = np.array([40, 50, '60'])
print(arr_2.dtype)   # <U11
print(arr_1 + arr_2) # hiba

print(arr_1 + arr_2.astype(int)) # 50 70 90

#############################

# Táblaforgatás: (pivoting): transpose() függvény.

arr_1 = np.array([
['col_1','col_2','col_3'],
[5,6,7],
[8,9,10]
])
arr_2 = np.transpose(arr_1)

print(arr_1)
print(arr_2)

# [['col_1' 'col_2' 'col_3']
#  ['5' '6' '7']
#  ['8' '9' '10']]

# [['col_1' '5' '8']
#  ['col_2' '6' '9']
#  ['col_3' '7' '10']]

# A numpy modulnak RENGETEG hasznos függvény van, érdemes tanulmányozni, pl. itt:

# https://www.w3resource.com/numpy/manipulation/index.php
# https://www.w3resource.com/python-exercises/numpy/index-array.php

#############################

# Listáknál törölni tudunk egy vagy több elemet; a lista helyben marad és a
# specifikált elemek eltűnnek:

lst_1 = [10, 20, 30, 40]
del(lst_1[1:3])
print(lst_1) # [10, 40]

# numpy array esetében ez nem így van:

import numpy as np

arr = np.array([10, 20, 30, 40])
del(arr[1:3]) # ValueError: cannot delete array elements

# A törlésre a delete() metódus szolgál; ilyenkor egy új tömb keletlezik.
# Slicing nem használható.

new_arr = np.delete(arr,[1, 2]) # az 1 és a 2 indexű elemeket akarjuk törölni
print(new_arr) # [10 40]

#############################
