# numpy tömb memória- és időtakarékosabb létrehozása
# Az nbytes attribútum
# dtypes explicit megadása tömb létrehozásánál

# Ha nem list vagy tuple a forrás, hanem valamely más iterálható objektum, akkor
# ennek az elemeit először el kell helyezni egy listában vagy tuple-ban és ebből
# lehet létrehozni a tömböt.

import numpy as np

s = {1, 2, 3, 1, 2, 3}
arr = np.array(list(s)) # vagy np.array(tuple(s))
print(arr) # [1 2 3]

# Nagy adatmennyiségeknél ezek a megoldások a szükségesnél lassúbbak és több
# memóriát fogyasztanak. A list (tuple) létrehozása időbe telik és ez egy (rövid)
# ideig együtt létezik a memóriában a forrással (jelen esetben az s set-tel) és
# a tömbbel.

# Hatékonyabb, ha először létrehozunk egy megfelelő méretű tömböt, aztán egyenként
# felülírjuk az elemeit. Tegyük fel, hogy a forrásban csak egész számok vannak:

s = {1, 2, 3, 1, 2, 3}
arr = np.array([0] * len(s))
for i, k in enumerate(s):
    arr[i] = k
print(arr, arr.dtype) # [1 2 3] int32

# Ha a forrásban más típusú elemek is vannak és a tömbbe ezeknek is változatlanul
# be kell kerülniük (ami általában rossz ötlet), akkor célszerűen a tömböt mindjárt
# a megfelelő típussal hozzuk létre.

s = {'ABC', 2, 3, 1, 2, 3}
arr = np.array([''] * len(s))
for i, k in enumerate(s):
    arr[i] = k
print(arr, arr.dtype) # ['1' '2' '3']

##############################################

# Az nbytes attribútum a tömbelemek által elfoglalt memóriaméretet adja meg. Hasonlítsuk
# össze ezt a többi méret-információval:

import numpy as np
import sys

lst = [1, 2, 3, 4, 5, 6]
x = np.array(lst)
print(x.size, x.nbytes, x.__sizeof__(), sys.getsizeof(x)) # 6 24 72 72

lst = [1, 2, 3, 4, 5, 6] * 10
x = np.array(lst)
print(x.size, x.nbytes, x.__sizeof__(), sys.getsizeof(x)) # 60 240 288 288

# Elemenként 4 bájtra van szükség; a másik két méret a tömb segédinformációit
# (shape, dtype, stb.) is tartalmazza.

##############################################

# Egy tömb létrehozásakor megadhatjuk explicit módon, hogy milyen típusa legyen
# az elemeknek. Ez például akkor hasznos, ha tudjuk, hogy csak kis egész számok
# vannak a bemeneten, ezért nem lesz szükség 4 bájtra elemenként.

arr_1 = np.array([10, 20, 30, 40, 50])
print(arr_1.dtype, arr_1.nbytes)  # int32 20

arr_2 = np.array([10, 20, 30, 40, 50], dtype='int8')
print(arr_2.dtype, arr_2.nbytes)  # int8 5

##############################################
