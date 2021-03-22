# set (halmaz) 1.

# https://www.python-course.eu/python3_sets_frozensets.php
# https://realpython.com/python-sets/

# Minden elemet csak egyszer tartalmaz; csak fix, immutábilis típusok lehetnek az elemei.

set_1 = { 1, 2, 3 }
set_1.add(2)
print(set_1, type(set_1)) # {1, 2, 3} <class 'set'>

lst_1 = [1, 1, 2, 2, 3, 3]
set_1 = set(lst_1)
print(set_1)  # {1, 2, 3}

# Nem megy:

set_1 = {}    # dict-nek gondolja
set_1.add(3)  # AttributeError: 'dict' object has no attribute 'add'

############################################

# A set-ben is ugyanolyan gyors a keresés, mint a dict-ben.

############################################

# list --> set:

set_1 = set([1, 2, 3, 1, 2, 3]) # # {1, 2, 3}

# tuple --> set:

set_1 = set((1, 2, 3, 1, 2, 3)) # # {1, 2, 3}

# dict kulcsok --> set:

dict_1 = {'A': 1, 'B': 1}
set_1 = set(dict_1)        # {'A', 'B'}
set_1 = set(dict_1.keys()) # {'A', 'B'}

# dict értékek --> set:

dict_1 = {'A': 1, 'B': 1}
set_1 = set(dict_1.values()) # {1}

############################################

# Visszafelé:

set_1 = {'A', 'B'}
lst = list(set_1)  # ['B', 'A']
tup = tuple(set_1) # ('B', 'A')

############################################
