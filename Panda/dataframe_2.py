# DataFrame hiányzó értékek kiegészítése (index alignment)

# Hasonlóan működik, mint a Series-nél; az oszlopok és a sorok egyaránt kiegészülnek
# a hiányzó elemekkel.

import pandas as pd

A = pd.DataFrame([[2, 4], [6, 8], [10, 12]], columns=['a','b'])
print(A)

#     a   b
# 0   2   4
# 1   6   8
# 2  10  12

B = pd.DataFrame([[1, 3, 5], [7, 9, 11]], columns=['a', 'b','c'])
print(B)

#    a  b   c
# 0  1  3   5
# 1  7  9  11

print(A + B)

#       a     b   c
# 0   3.0   7.0 NaN
# 1  13.0  17.0 NaN
# 2   NaN   NaN NaN

#################################################

# Ha az operátor(+) helyett a megfelelő objektum metódust (add) használjuk, akkor meg
# tudunk adni a NaN helyett más "kitöltő" elemet.

print(A.add(B, fill_value=1000))

#         a       b       c
# 0     3.0     7.0  1005.0
# 1    13.0    17.0  1011.0
# 2  1010.0  1012.0     NaN

# Az egyetlen NaN érték azért marad meg, mert 'c' oszlop 2 indexű elem egyik mátrixban sincs.

#################################################
