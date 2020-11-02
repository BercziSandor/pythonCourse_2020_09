# shape, ndim, dtype, slicing, where

# https://www.w3schools.com/python/numpy_intro.asp
# https://www.w3schools.com/python/numpy_array_slicing.asp

import numpy as np

# Egy dimenziójú mátrix (vektor):

arr_1 = np.array([10, 20, 30])
print(arr_1.ndim, arr_1.shape) # 1 (3,)

# Egysoros mátrix:

arr_1 = np.array([[10, 20, 30]])
print(arr_1.ndim, arr_1.shape) # 2 (1, 3)

# Egyoszlopos mátrix:

arr_1 = np.array([
  [10],
  [20],
  [30]
]
)
print(arr_1.ndim, arr_1.shape) # 2 (3,1)

# Persze általában inkább így lesz leírva:

arr_1 = np.array([ [10], [20], [30] ])

# Kétsoros, három oszlopos mátrix:

arr_1 = np.array([
  [10, 20, 30],
  [40, 50, 60]
]
)
print(arr_1.ndim, arr_1.shape) # 2 (2, 3)

# Leírhatjuk így is:

arr_1 = np.array([ [10, 20, 30], [40, 50, 60] ])

# Adattípusok

arr_1 = np.array([10, 20, 30])
print(arr_1.dtype, arr_1.dtype.type) # int32 <class 'numpy.int32'>

# Vegyes adattípusoknál:

arr_1 = np.array([10, 20, '30'])
print(arr_1.dtype, arr_1.dtype.type) # <U11 <class 'numpy.str_'>

# Az U betű azt jelenti, hogy Unicode kódolású sztring.
# Ez viszonylag gyakran előfordul, pl. fejléces táblázatoknál, vagy szövegként beírt számoknál.

# Általánosabb esetben:

arr_1 = np.array([10, 20, {3}])
print(arr_1.dtype, arr_1.dtype.type) # object <class 'numpy.object_'>

###########################################

# A slicing ugyanúgy megy, mint az egydimenziós listáknál, az egyes dimenziókhoz tartozó
# kifejezések vesszővel vannak elválasztva. A hiányzó kifejezés itt is a default-ot jelenti.
# Ha egy dimenzióra teljesen hiányzik a kifejezés, akkor azon dimenzió szerint az összes
# elemet kell venni.

arr_1 = np.array([
  [10, 20, 30],
  [40, 50, 60]
]
)

arr_2 = arr_1[:,:] # teljes másolat

print(arr_2)
# [[10 20 30]
# [40 50 60]]

# Ugyanez másként:
arr_2 = arr_1[:]
arr_2 = arr_1[:,]

# Az első dimenzió (a sorok) helye nem lehet üres, ez:

arr_2 = arr_1[,1]

# szintaktikai hiba. Itt az ellipsis jelölést használhatjuk:

arr_2 = arr_1[...,1]
print(arr_2) # [20 50]

# Csak az első sor többféle módon leírható:
print(arr_1[0], arr_1[0,:], arr_1[0,::]) # [10 20 30] [10 20 30] [10 20 30]

# Az első változat a legolvashatóbb (bár ez szubjektív).

# Csak az első oszlop:
print(arr_1[:,0]) # [10 40]

# Összes sor, második oszloptól végig:
print(arr_1[:,1:])
# [[20 30]
#  [50 60]]

# Összes sor, utolsó oszlop:
print(arr_1[:,-1:])
# [[30]
#  [60]]

# Utolsó oszlop egyetlen sorrá alakítva:

print(arr_1[:,-1]) # [30 60]

###########################################

# Explicit típuskonverziók

arr_1 = np.array([10, 20, '30'])
arr_2 = arr_1.astype(int)
print(arr_2) # [10 20 30]

arr_1 = np.array([10, 20, 'xyz'])
arr_2 = arr_1.astype(int) # hiba

###########################################
