# Dekorátor demo: a numba előfordító használata.

# https://numba.pydata.org/

# A numba numpy tömbökön dolgozó függvények felgyorsítására szolgál.
# A függvény első hívásakor optimalizált gépi kódot állít elő (JIT, Just In Time
# fordító). A felgyorsítani kívánt függvény elé csak egy dekorátort kell tenni.

import numpy as np
import time
# from numba import njit  # numba bekapcsolás 1.

arr = np.random.random(size=10)

# @njit # numba bekapcsolás 2.
def slow_numeric_func(a, b, c, arr):  # értelmetlen demo-függvény; nem vektorizálható
    outflow = np.zeros((arr.size), dtype=np.float64)
    state_in = 0
    state_out = 0
    for i in range(arr.size):
        state_out = (1 - c) * state_in + a * arr[i]
        outflow[i] = (1 - a - b) * arr[i] + c * state_in
        state_in = state_out
    return outflow

###############################################

# Sokszor felhívjuk a lassú függvényt:

def test(n):
    for i in range(n):
        slow_numeric_func(0.2, 0.6, 0.1, arr)

###############################################

slow_numeric_func(0.3, 0.8, 0.2, arr) # numba bekapcsolva: itt készül el az előfordított kód
                                      # ezt NEM akarjuk beletenni az időmérésbe; csak egyszer
                                      # kell megcsinálni

###############################################

N = 200000
start = time.time()
test(N)
t = time.time() - start
print(f'Idő: {t}')

###############################################

# Egy adott környezetben a kétféleképpen mért idő 4.46 és 0.218 sec volt, tehát
# a javulás 4.46 / 0.218 = 20.46-szoros. Ha kiderül, hogy egy adott függvényen
# nem javít lényegesen a numba, akkor egyszerűen elvesszük a dekorátort és kész.

###############################################
