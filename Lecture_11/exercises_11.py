# 1.)

# Írjunk függvényt, amely egy numpy tömböt és egy függvényt kap paraméterként.
# Végrehajtja a függvényt a tömbön és egy dict-ben adja vissza

# a visszatérési értéket,
# azt, hogy hány elemű volt a tömb,
# hány NaN érték volt benne,
# egy státuszjelzést arról, hogy sikerült-e a művelet és
# ha kivétel keletkezett, akkor annak a típusát - tehát kapjon el minden kivételt.

def func_with_stat(numbers, func):
    pass

arr = np.array([10, 20, 30, np.NaN])
ret = func_with_stat(arr, np.nansum)
print(ret) # {'status': True, 'ret_val': 60.0, 'exc_type': None, 'n_total': 4, 'n_nan': 1}

ret = func_with_stat(arr, sum)
print(ret) # {'status': True, 'ret_val': nan, 'exc_type': None, 'n_total': 4, 'n_nan': 1}

arr = np.array([10, 20, 30, None])
ret = func_with_stat(arr, np.nansum)
print(ret) # {'status': False, 'ret_val': None, 'exc_type': <class 'TypeError'>, 'n_total': 4, 'n_nan': None}

############################################

# 2.)

# Írjunk dekorátort, amelyet olyan függvényekre lehet alkalmazni, melyek egy egydimenziós
# numpy tömböt kapnak paraméterként. A paraméter-tömbben a függvény felhívása előtt
# cserélje a None értékeket np.NaN-ra.

import numpy as np

def nan_decor(funcToBeDecorated):
    pass

@nan_decor
def func(param):
    return 2 * param

arr_1 = np.array([10, None, 20, 30])
print(func(arr_1)) # [20, nan, 40, 60]

############################################

# 3.)

# Írjunk iterátor-osztályt, amely inicializáláskor egy iterálható obkektumot és egy
# egész számot kap paraméterként. Azokat az elemeket adja vissza a bemeneti objektum
# által szolgáltatott sorozatból, amelyek oszthatóak a számmal.

class ModuloIter:
    def __init__(self, inputSeries, number):
        pass

m = ModuloIter(range(19), 6)
for e in m:
    print(e)

# 0
# 6
# 12
# 18

############################################
