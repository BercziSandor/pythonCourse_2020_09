# Fancy indexing
# Egyes szerzőknél a boolean indexelés (maszkolás) is ezen címszó alá tartozik.
# Én csak az integer listával való indexelést hívom így.

# http://scipy-lectures.org/intro/numpy/array_object.html#fancy-indexing
# https://medium.com/better-programming/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d
# http://jalammar.github.io/visual-numpy/

# Fancy indexing: tetszőleges indexeket összegyűjtök egy listába és ezzel indexelem a tömböt.
# Ellentétben a slicing-gal itt nem kell semmilyen szabályosságnak fennállnia.

import numpy as np

arr_1 = np.array([10, 20, 30, 40, 50])
arr_2 = arr_1[[1, 2, 4]]
print(arr_2) # [20 30 50]

# Ezt helyettesíti:

arr_2 = np.array([arr_1[1], arr_1[2], arr_1[4]])

# Az indexet sokszor egy változóba tesszük:

ix = [1, 2, 4]
arr_2 = arr_1[ix]
print(arr_2) # [20 30 50]

#############################

# Két dimenziós tömböknél persze külön indexelhetjük a sorokat és az oszlopokat:

arr_1 = np.array([
[ 0, 1, 2, 3],
[ 4, 5, 6, 7],
[ 8, 9, 10, 11]
])

row = np.array([0, 1, 2])
col = np.array([2, 1, 3])

arr_2 = arr_1[row, col]
print(arr_2) # [2, 5, 11]

#############################

# A keletkező tömb másolat, NEM referencia (view).

arr_1 = np.array([10, 20, 30, 40, 50])
arr_2 = arr_1[[1, 2, 4]]

print(arr_2)    # [20 30 50]
arr_2[0] = 99
print(arr_2)    # [99 30 50]
print(arr_1)    # [10 20 30 40 50] -- nem változott

# ****** Amikor egy adatszerkezetet előállítunk egy másikból, MINDIG vizsgáljuk
# ****** meg, hogy másolat (copy) keletkezett-e, vagy referencia (view).

#############################

# Viszont a fancy indexeléssel kiválasztott elemeket módosítani is tudjuk.

arr_1 = np.array([10, 20, 30, 40, 50])
ix = [1, 2, 4]

arr_1[ix] = 99
print(arr_1)  # [10 99 99 40 99]

# Nem csak egyetlen értékkel írhatjuk fölül a tömb elemeit, a broadcast itt is működik:

arr_1 = np.array([10, 20, 30, 40, 50])
ix = [1, 2, 4]

arr_1[ix] = [97, 98, 99]
print(arr_1)  # [10 97 98 40 99]

#############################
