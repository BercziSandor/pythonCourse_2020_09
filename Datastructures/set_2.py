# Halmazokon végzett beépített műveletek

# https://realpython.com/python-sets/

# A halmazelmélet összes alapművelete meg van valósítva.

set_1 = {'A', 'B', 'C', 'D'}
set_2 = {'B', 'C', 'E', 'F'}

# Elem-tartalmazás

print('A' in set_1) # True

########################################

# Metszet:

print(set_1 & set_2) # {'C', 'B'}

# Vagy az intersection() metódussal:

print(set_1.intersection(set_2)) # {'C', 'B'}

# A metódusnak tetszőleges iterálható sorozatot adhatunk paraméterként, végig fogja
# azt járni, halmazt képez az elemeiből és elkészíti a metszetet:

print(set_1.intersection(['A', 20, 30]))    # 'A'
print({3, 4, 5, 6}.intersection(range(5)))  # {3, 4}

# Ám ugyanezt NEM tehetjük meg az & operátoros alaknál:

print(set_1 & ['A', 20, 30]) # TypeError: unsupported operand type(s) for |: 'set' and 'list'

########################################

# Unió:

print(set_1 | set_2) # {'A', 'D', 'C', 'E', 'F', 'B'}

# vagy:

print(set_1.union(set_2)) # {'A', 'D', 'C', 'E', 'F', 'B'}

# A union() metódusnak tetszőleges iterálható sorozatot adhatunk paraméterként:

print(set_1.union(['D', 'D', 'X'])) # {'X', 'C', 'A', 'B', 'D'}
print(set_1.union(range(3)))        # {0, 1, 2, 'C', 'D', 'B', 'A'}

dic = {'A': 1, 'B': 2}
print(set_1.union(dic))          # {'B', 'D', 'A', 'C'}
print(set_1.union(dic.values())) # {1, 2, 'A', 'B', 'D', 'C'}

# Ám ugyanezt NEM tehetjük meg a | operátoros alaknál:

print(set_1 | ['D', 'D', 'X']) # TypeError: unsupported operand type(s) for |: 'set' and 'list'

########################################

# Különbség (set_1-ben benne vannak és set_2-ben nem):

print(set_1 - set_2)           # {'D', 'A'}
print(set_1.difference(set_2)) # {'D', 'A'}

########################################

# Szimmetrikus különbség (csak az egyikben vannak benne):

print(set_1 ^ set_2)                     # {'F', 'D', 'A', 'E'}
print(set_1.symmetric_difference(set_2)) # {'F', 'D', 'A', 'E'}

########################################

# Halmaz-tartalmazás (subset, superset):

set_1 = {'A', 'B', 'C', 'D'}
set_2 = {'A', 'B'}

print(set_2 <= set_1, set_1 >= set_2) # True True
print(set_1 <= set_1, set_1 >= set_1) # True True

# vagy ugyanez az issuperset(), issubset() metódusokkal:

contains = set_1.issuperset(set_2)
print(contains) # True

contains = set_2.issubset(set_1)
print(contains) # True

########################################

# A "valódi" tartalmazást, amikor a két halmaz nem egyforma, csak a < és > operátorokkal
# tudjuk ellenőrizni, metódus erre nincs.

print(set_2 < set_1, set_1 > set_2) # True True
print(set_1 < set_1, set_1 > set_1) # False False

########################################

# Mindegyik művelet elvégezhető kettőnél több halmazon is egy lépésben, például:

set_1 = {'A', 'B', 'C', 'D'}
set_2 = {'A', 'B', 'C'}
set_3 = {'A', 'B'}

print(set_1 & set_2 & set_3)            # {'B', 'A'}
print(set_1.intersection(set_2, set_3)) # {'B', 'A'}

########################################
