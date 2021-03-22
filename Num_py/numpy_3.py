# array tuple-ból, set-ből, dict-ből, delimitált sztringből
# reshape, newaxis
# shape változtatása helyben
# a helyben végzett műveletek előnyei
# len() függvény kontra size attribútum

# https://medium.com/better-programming/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d
# http://jalammar.github.io/visual-numpy/

# tuple a forrás:

import numpy as np

tup = (10, 20, 30)
arr_1 = np.array(tup)
print(arr_1) # [10 20 30]

# Itt csak át kellett adni a tuple-t a tömb konstruktorának, ő végigiterál rajta,
# ahogy egy listán is és létrehozza az elemekből a tömböt.

#############################

# set a forrás:

s = {1, 2, 3, 1, 2, 3}
x = np.array(list(s))

# vagy:

x = np.array(tuple(s))

print(x, x.shape, x.ndim) # [1 2 3] (3,) 1

# NEM adhatjuk oda közvetlenül a halmazt a tömb konstruktorának, mert akkor egy
# egyelemű, 0 dimenziós tömb keletkezik:

s = {1, 2, 3, 1, 2, 3}
x = np.array(s)
print(x, x.shape, x.ndim) # {1, 2, 3} () 0

# Lett egy tömbünk, aminek egyetlen eleme van (a halmaz). Ez nyilván azért van így,
# mert a halmaz iterálásakor nem garantált az elemek sorrendje és nem mindig van értelme
# egy olyan tömböt létrehozni, amelyben tetszőleges sorrendben lesznek az elemek.
# Tehát először elő kell állítanunk egy határozott sorrendű sorozatot.

# Léteznek persze esetek, amikor nem számít az elemek sorrendje, pl. van egy csomó
# mérési eredményünk, melyek közt sem időrendi, sem egyéb sorrend nem létezik. Szóval
# szerintem meg lehetett volna engedni, hogy tetszőleges iterálható sorozatot odaadjunk
# a tömb konstruktorának, amely aztán végigmegy a sorozaton és elhelyezi a tömbben az
# elemeket. Pl.létrehoz egy tuple-t, amit aztán átkonvertál.

#############################

# dict a forrás.
# A kulcsokat akarjuk elhelyezni egy tömbben.

dic = {'A': 10, 'B': 20, 'C': 30}

arr_1 = np.array([k for k in dic.keys()])
print(arr_1) # ['A' 'B' 'C']

# Ez feleslegesen bonyolult, egyszerűbben:

arr_1 = np.array(list(dic.keys()))
print(arr_1) # ['A' 'B' 'C']

# vagy:

arr_1 = np.array(tuple(dic.keys()))
print(arr_1) # ['A' 'B' 'C']

# Persze az értékekből ugyanígy tudunk tömböt készíteni:

arr_1 = np.array(list(dic.values()))
print(arr_1) # [10 20 30]

arr_1 = np.array(tuple(dic.values()))
print(arr_1) # [10 20 30]

#############################

str_1 = '10; 20; 30'

lst_1 = str_1.split(';')
print(lst_1) # ['10', ' 20', ' 30']

arr_1 = np.array(lst_1).astype(int)
print(arr_1) # [10 20 30]

# Nagy adatmennyiségeknél számíthat, ezért tudatosítsuk, hogy itt:

arr_1 = np.array(lst_1).astype(int)

# KÉT tömb keletkezett, először ez:

arr_0 = np.array(lst_1) # ['10' '20' '30']

# aztán ebből a végleges:

arr_1 = arr_0.astype(int)

# Majd látni fogunk memóriaszükséglet és sebesség szempontjából jobb megoldást,
# ami persze cserében kicsit bonyolultabb.

# Fontos mindig ellenőrizni a létrejövő tömb elemtípusát (dtype) - illetve adott
# esetben megváltoztatni azt.

#############################

# Alak, azaz dimenzióváltások.

# Egy dimenziós tömb --> egy soros két dimenziós tömb:

x = np.array([1, 2, 3])
print(x, x.shape, x.ndim) # [1 2 3] (3,) 1

y = x.reshape((1, 3))
print(y, y.shape, y.ndim) # [[1 2 3]] (1, 3) 2

# Ugyanezt a newaxis kulcsszóval és slicing-gal is elérhetjük:

y = x[np.newaxis,:]
print(y, y.shape, y.ndim) # [[1 2 3]] (1, 3) 2

#############################

# Egy dimenziós tömb --> egy oszlopos két dimenziós tömb:

y = x.reshape((3, 1))
print(y, y.shape, y.ndim)

# [[1]
#  [2]
#  [3]] (3, 1) 2

# Ugyanezt a newaxis kulcsszóval és slicing-gal is elérhetjük:

y = x[:,np.newaxis]
print(y, y.shape, y.ndim)

# [[1]
#  [2]
#  [3]] (3, 1) 2

#############################

# Két soros, három oszlopos tömb --> három soros, két oszlopos tömb:

x = np.array([[1, 2, 3], [4, 5, 6]])
print(x, x.shape, x.ndim)

# [[1 2 3]
#  [4 5 6]] (2, 3) 2

y = x.reshape((3, 2))
print(y, y.shape, y.ndim)

# [[1 2]
#  [3 4]
#  [5 6]] (3, 2) 2

#############################

# A reshape segítségével  új tömböt hoztunk létre; ha helyben akarjuk elvégezni
# az átalakítást, akkor egyszerűen a shape attribútumot módosítjuk.

x = np.array([[1, 2, 3], [4, 5, 6]])
print(x, x.shape, x.ndim)

# [[1 2 3]
#  [4 5 6]] (2, 3) 2

x.shape = (3, 2)
print(x, x.shape, x.ndim)

# [[1 2]
#  [3 4]
#  [5 6]] (3, 2) 2

# Ha nincs szüség egszerre a két tömbre, akkor használjuk a helyben történő módosítást.
# Egyrészt memóriát spórolunk, másrészt így sokkal gyorsabb lesz, harmadrészt jobban
# olvasható a program, mert nem kell azon gondolkozni, hogy vajon miért van szükség
# két tömbre (miközben nincs rá szükség).

#############################

# Ha valamelyik dimenzió mérete egyértelműen kiszámítható, akkor a helyére -1-et írhatunk:

x = np.array([[1, 2, 3], [4, 5, 6]])
y = x.reshape((3, -1))
print(y, y.shape, y.ndim)

# [[1 2]
#  [3 4]
#  [5 6]] (3, 2) 2

# Ugyanez helyben elvégezve:

x.shape = (3, -1)
print(x, x.shape, x.ndim)

# [[1 2]
#  [3 4]
#  [5 6]] (3, 2) 2

#############################

# A len() függvény (nem tudom, miért) egynél több dimenziós tömb esetén a SOROK számát
# adja meg, nem az elemekét. A size attibútum mindig az elemek számát szolgáltatja.

x = np.array([1, 2, 3, 4, 5, 6])     # 1 dimenziós
print(len(x), x.size) # 6 6

x = np.array([[1, 2, 3, 4, 5, 6]])   # 2 dimenziós
print(len(x), x.size) # 1 6

x = np.array([[1, 2, 3], [4, 5, 6]]) # 2 dimenziós
print(len(x), x.size) # 2 6

#############################

# Két soros, három oszlopos tömb --> egydimenziós tömb:

x = np.array([[1, 2, 3], [4, 5, 6]])
print(x, x.shape, x.ndim)

# [[1 2 3]
#  [4 5 6]] (2, 3) 2

y = x.reshape(x.size)
print(y, y.shape, y.ndim) # [1 2 3 4 5 6] (6,) 1

# Így is írhatjuk:

y = x.reshape(-1)
print(y, y.shape, y.ndim) # [1 2 3 4 5 6] (6,) 1

# Helyben elvégezve:

x.shape = (x.size) # vagy x.shape = (-1)
print(x, x.shape, x.ndim) # [1 2 3 4 5 6] (6,) 1

#############################

# Példa reshape alkalmazására: mérési adatok jönnek be, naponta egy. Ez persze
# egy egydimenziós tömböt alkot. Szeretnénk úgy átrendezni, hogy a hét azonos
# napjához tartozó értékek egymás alá kerüljenek.

input_arr  = np.array([10, 20, 30, 40, 50, 60, 70, 11, 21, 31, 41, 51, 61, 71])
output_arr = input_arr.reshape(2,7)
print(output_arr)

#   H  K SZE CS P SZO V
# [[10 20 30 40 50 60 70]
#  [11 21 31 41 51 61 71]]

# Így is írhatjuk, ezt érdemes megjegyezni:

output_arr = input_arr.reshape(-1,7)

# Nem számoljuk össze az elemekt, fő, hogy héttel osztható legyen a számuk.

#############################
