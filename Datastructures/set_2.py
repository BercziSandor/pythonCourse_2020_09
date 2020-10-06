# Halmazokon végzett beépített műveletek

# A halmazelmélet összes alapművelete meg van valósítva.

set_1 = {'A', 'B', 'C', 'D'}
set_2 = {'B', 'C', 'E', 'F'}

# Elem-tartalmazás

print('A' in set_1) # True

# Metszet:

print(set_1 & set_2) # {'C', 'B'}

# Különbség (set_1-ben benne vannak és set_2-ben nem):

print(set_1 - set_2) # {'A', 'D'}

# Szimmetrikus különbség (csak az egyikben vannak benne):

print(set_1 ^ set_2) # {'E', 'F', 'A', 'D'}

# Unió:

print(set_1 | set_2) # {'C', 'A', 'B','D', 'F', 'E'}

set_1 = {'A', 'B', 'C', 'D'}
set_2 = {'A', 'B'}

# Halmaz-tartalmazás (subset, superset)

print(set_2 <= set_1, set_1 >= set_2) # True True

# vagy ugyanez másképp:

contains = set_1.issuperset(set_2)
print(contains) # True

contains = set_2.issubset(set_1)
print(contains) # True

