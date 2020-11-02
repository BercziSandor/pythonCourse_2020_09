# Lecture_7\exercises_7.py megoldásai

# 1.)

# A dict-té alakítás felesleges, ráadásul 3.7-es verzió előtt hibás is lehet az eredmény,
# mert a dict-ből kiolvasásnál nincs definiálva a sorrend.

names_reversed = [ e[0] for e in sorted(employees, key=lambda x: x[0], reverse=True)]
print(names_reversed) # ["Zach","James", "Cecilia", "Ann"]

####################################

# 2.)

# A.

# Ha az lst-ben vannak többször előforduló elemek, ezek a kimeneten csak egyszer
# fognak szerepelni:

lst = [10, 11, 5, 6, 7, 4, 6] # 6 kétszer van
tup = (10, 11, 7, 4)

# [25, 36]

# B.

res = [e*e for e in lst if e not in tup]

# [25, 36, 36]

####################################
