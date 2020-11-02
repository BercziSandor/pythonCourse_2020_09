# https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python

# Műveletek vektorizálásának gyorsító hatása

# Egy numerikus tömb elemeinek reciprokát akarjuk elhelyezni egy másik tömbben.

# Első megoldás: elemenként képezzük a reciprokokat. A nullával osztás lehetőségét
# most kizárjuk.

import numpy as np

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output

val_arr = np.array([2, 5, 10])
rec_arr = compute_reciprocals(val_arr)
print(rec_arr) # [0.5 0.2 0.1]

# Második megoldás: mátrixművelettel.

rec_arr = 1 / val_arr
print(rec_arr)

print(rec_arr) # [0.5 0.2 0.1]

# A második megoldás átláthatóbb, egyszerűbb.

#############################

# Hasonlítsuk össze a sebességeket.

import time

np.random.seed(0)  # hogy megismételhető legyen
size_ = 100_000
values = np.random.randint(1, 10, size=size_)

start = time.perf_counter()
compute_reciprocals(values)
finish = time.perf_counter()
t_1 = finish - start
print(f'finish - start: {t_1:.5f} (egyenként)')

start = time.perf_counter()
output = 1.0 / values
finish = time.perf_counter()
t_2 = finish - start
print(f'finish - start: {t_2:.5f} (mátrixművelettel)')
print(f't_1/t_2 = {t_1/t_2:.1f}')

# finish - start: 0.28207 (egyenként)
# finish - start: 0.00067 (mátrixművelettel)
# t_1/t_2 = 423.4

# A konkrét számok persze környezet-függőek és futtatásról futtatásra is változnak.

# A lényeg: a mátrixos megoldás több százszor gyorsabb is, nemcsak szebb.

# Az eredeti megoldásnál a Python minden lépésnél megkeresi, hogy hol található az adott
# objektumhoz tartozó függvény kódja; a mátrixos megoldásnál nincs szükség, az egész
# művelet a Numpy belsejében, C-ben megírt optimalizált rutinokban zajlik le.

#############################
