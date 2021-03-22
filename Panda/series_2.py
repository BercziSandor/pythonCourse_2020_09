# Series hiányzó értékek kiegészítése (index alignment)

import pandas as pd

A = pd.Series([2, 4, 6, 8])
B = pd.Series([1, 3, 5])

print(A)

# 0    2
# 1    4
# 2    6
# 3    8
# dtype: int64

print(A + B)

# 0     3.0
# 1     7.0
# 2    11.0
# 3     NaN
# dtype: float64

# A NaN miatt float lett a típus!

# Másik példa:

A = pd.Series([2, 4, 6], index=[0, 1, 2])
print(A)

# 0 2
# 1 4
# 2 6        6 + 3
# dtype: int64

B = pd.Series([1, 3, 5], index=[1, 2, 3])

print(A + B)

# 0 NaN      B-ben nincs 0 index
# 1 5        4 + 1
# 2 9        6 + 3
# 3 NaN      A-ban nincs 3 index
# dtype: float64

# A NaN miatt most is float lett a típus!

#################################################

# Ez a működés NAGYON más, mint a numpy-nál. Ott, ha broadcast-tal nem lehet megfelelő
# alakra hozni a két operandust és valamelyik indexnek nincs párja, akkor hibajelzést kapunk.

import numpy as np

A = np.array([2, 4, 6, 8])
B = np.array([1, 3, 5])
print(A + B)

# Traceback (most recent call last):
#   File "test.py", line 5, in <module>
#     print(A + B)
# ValueError: operands could not be broadcast together with shapes (4,) (3,)

#################################################

# Ha az operátor(+) helyett a megfelelő objektum metódust használjuk, akkor meg tudunk adni
# a NaN helyett más "kitöltő" elemet.

A = pd.Series([2, 4, 6, 8])
B = pd.Series([1, 3, 5])

print(A.add(B))

# 0     3.0
# 1     7.0
# 2    11.0
# 3     NaN
# dtype: float64

print(A.add(B, fill_value=0))

# 0     3.0
# 1     7.0
# 2    11.0
# 3     8.0  8 + NaN ==> 8 + 0
# dtype: float64

#################################################
