# numpy tömbök bemutatása
# shape, ndim, dtype, slicing

# https://www.w3schools.com/python/numpy_intro.asp
# https://www.w3schools.com/python/numpy_array_slicing.asp
# https://medium.com/better-programming/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d
# http://jalammar.github.io/visual-numpy/
# https://stackoverflow.com/questions/49751000/how-does-numpy-determine-the-array-data-type-when-it-contains-multiple-dtypes
# https://numpy.org/doc/stable/reference/arrays.dtypes.html
# https://www.geeksforgeeks.org/data-type-object-dtype-numpy-python/

import numpy as np

# Egy dimenziójú tömb (vektor):

arr_1 = np.array([10, 20, 30])
print(arr_1.ndim, arr_1.shape) # 1 (3,)

##################################

# Két dimenziós, egysoros tömb:

arr_1 = np.array([ [10, 20, 30] ])
print(arr_1.ndim, arr_1.shape) # 2 (1, 3)

##################################

# Két dimenziós, egyoszlopos tömb:

arr_1 = np.array([
  [10],
  [20],
  [30]
]
)

# Persze így is írható:

arr_1 = np.array([ [10], [20], [30] ])

print(arr_1.ndim, arr_1.shape) # 2 (3,1)

##################################

# Kétsoros, három oszlopos tömb:

arr_1 = np.array([
  [10, 20, 30],
  [40, 50, 60]
]
)

# Leírhatjuk így is:

arr_1 = np.array([ [10, 20, 30], [40, 50, 60] ])

print(arr_1.ndim, arr_1.shape) # 2 (2, 3)

##################################

# Adattípusok

# Csupa egész szám van a tömbben:

arr_1 = np.array([10, 20, 30])
print(arr_1.dtype, arr_1.dtype.type) # int32 <class 'numpy.int32'>

##################################

# Sztring is van a tömbben::

arr_1 = np.array([10, 20, '30'])
print(arr_1.dtype, arr_1.dtype.type) # <U11 <class 'numpy.str_'>

# Ez az eset viszonylag gyakran előfordul, pl. fejléces táblázatoknál, vagy
# szövegként beírt számoknál.

# Az U betű azt jelenti, hogy Unicode kódolású sztring, a 11 azt, hogy legfeljebb 11
# karakteres, a < jel azt, hogy little endian (a legkisebb helyiértékű bájt van legelöl).
# Nem tudom, milyen heurisztika szerint számították ki, hogy itt (Windows alatt, ennél a
# numpy verziónál) a méret pont 11 karakter legyen.
# Egy 15 karakteres sztringnél 13 lesz az érték:

arr_1 = np.array([10, 20, '1235678901235'])
print(arr_1.dtype) # <U13

# Nincs nagy jelentősége - a lényeg: ha egyetlen sztring van a tömbben, akkor már az egész
# tömb is sztring típusú lesz; ami azt jelenti, hogy MINDEGYIK eleme sztring típusú:

print(arr_1[0].dtype) # <U2

# ami azt jelenti, hogy numerikus műveletet nem végezhetünk velük:

print(arr_1[0] + 2) # TypeError

# A sztringet az astype() metódussal számmá kell alakítanunk:

print(arr_1[0].astype(int) + 2, arr_1[0].astype(float) + 2) # 2 2.0

##################################

# Általánosabb esetben, egyéb típusoknál:

arr_1 = np.array([10, 20, {3}])
print(arr_1.dtype, arr_1.dtype.type) # object <class 'numpy.object_'>

###########################################

# A slicing ugyanúgy megy, mint az egydimenziós listáknál, az egyes dimenziókhoz
# tartozó kifejezések vesszővel vannak elválasztva. A hiányzó kifejezés itt is a
# default-ot jelenti. Ha egy dimenzióra teljesen hiányzik a kifejezés, akkor
# azon dimenzió szerint az összes elemet kell venni.

arr_1 = np.array([
  [10, 20, 30],
  [40, 50, 60]
]
)

arr_2 = arr_1[:,:] # teljes másolat: összes sor, összes oszlop

print(arr_2)
# [[10 20 30]
# [40 50 60]]

# Ugyanez másként:

arr_2 = arr_1[:]   # összes sor, oszlopokról hallgatunk --> tehát az összes
arr_2 = arr_1[:,]  # összes sor, oszlopokról semmit nem specifikálunk --> az összes

##################################

# Az első dimenzió (a sorok) helye nem lehet üres, ez:

arr_2 = arr_1[,1]

# szintaktikai hiba. Itt az ellipsis jelölést használhatjuk:

arr_2 = arr_1[...,1]
print(arr_2) # [20 50]

##################################

# Egy teljes sor kiválasztása többféle módon leírható.
# Egy dimenziós tömbbé alakítva:

print(arr_1[0])    # [10 20 30]
print(arr_1[0,])   # [10 20 30]
print(arr_1[0,:])  # [10 20 30]
print(arr_1[0,::]) # [10 20 30]

# A második változat a legolvashatóbb (bár ez szubjektív). Nekem azért ez tetszik
# legjobban, mert rövid, de látszik belőle, hogy két dimenziós tömbről van szó. Az
# első alakról nem tudjuk eldönteni, hogy egy- vagy kétdimenziós-e a tömb.

# Az, hogy indegyik esetben egy dimenziós tömbként kapjuk meg az eredményt, már a
# fenti kiíratásból is látszik (egyetlen szögletes zárójelpárban vannak az elemek).

print(arr_1[0,].shape) # (3,)

# Egy teljes sor kiválasztása egy soros kétdimenziós tömbként:

print(arr_1[0:1])    # [[10 20 30]]
print(arr_1[0:1,])   # [[10 20 30]]
print(arr_1[0:1,:])  # [[10 20 30]]
print(arr_1[0:1,::]) # [[10 20 30]]

print(arr_1[0:1].shape) # (1, 3)

##################################

# Összes sor, második oszloptól végig:

print(arr_1[:,1:])
# [[20 30]
#  [50 60]]

##################################

# A teljes első oszlop egydimenziós tömbbé alakítva:

arr_2 = arr_1[:,0]
print(arr_2, arr_2.shape) # [10 40] (2,)

# Az első oszlop egyoszlopos két dimenziós tömbbé alakítva:

arr_2 = arr_1[:,0:1]
print(arr_2, arr_2.shape)

# [[10]
#  [40]] (2, 1)

# Utolsó oszlop egydimenziós tömbbé alakítva:

arr_2 = arr_1[:,-1]
print(arr_2, arr_2.shape) # [30 60] (2,)

# Utolsó oszlop egyoszlopos két dimenziós tömbbé alakítva:

arr_2 = arr_1[:,-1:]
print(arr_2, arr_2.shape)
# [[30]
#  [60]] (2, 1)

##################################

# Explicit típuskonverziók

arr_1 = np.array([10, 20, '30'])
arr_2 = arr_1.astype(int)
print(arr_2) # [10 20 30]

arr_1 = np.array([10, 20, 'xyz'])
arr_2 = arr_1.astype(int) # hiba

###########################################

# A slice másik objektum, de AZ EREDETI tömbre mutató referenciákat tartalmaz,
# azaz NEM másolat:

import numpy as np

arr_1 = np.array([1, 2, 3])
arr_2 = arr_1[:]
print(id(arr_1), id(arr_2)) # 7999064 66477016
arr_2[0] = 99
print(arr_1)  # [99  2  3]

# A Python list-nél nem így van:

lst_1 = [1, 2, 3]
lst_2 = lst_1[:]
lst_2[0] = 99
print(lst_1) # [1, 2, 3]

# Itt a slice másolat.

##################################

# Ha másolatot akarunk létrehozni a numpy array-nél, akkor a copy() metódust kell meghívni:

arr_1 = np.array([1, 2, 3])
arr_2 = arr_1.copy()
arr_2[0] = 99
print(arr_1) # # [1  2  3]

##################################

