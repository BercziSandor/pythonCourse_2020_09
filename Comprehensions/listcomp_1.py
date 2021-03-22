# List comprehension 1.

# Listák elkészítéséhez szolgáló  szintaktikus variáció.

# Példácska: készítsünk listát a számok tízszereséből 0-tól 4-ig:

lst = []
for x in range(5):
    lst.append(10*x)

print(lst) # [0, 10, 20, 30, 40]

# Ugyanez list comprehension-nel:

lst = [10*x for x in range(5)]
print(lst) # [0, 10, 20, 30, 40]

# A szögletes zárójel elmondja, hogy egy listát kell készíteni.
# A 10*x kifejezés megadja, hogy mi legyen az elemek értéke

####################################

# Legegyszerűbb alak:

# values = [expression for item in collection]

# ami ezzel ekvivalens:

# values = []
# for item in collection:
#     values.append(expression)

# Amikor megszokjuk, sokkal olvashatóbbnak fogjuk látni a listcomp alakot.

####################################

# Feltétel a for ciklusban

# Most csak a páros számok tízszereséből akarunk listát készíteni.

# Hagyományos alak:

lst = []
for x in range(5):
    if x % 2 == 0:
        lst.append(10*x)

print(lst) # 0 20 40

# Listcomp:

lst = [10*x for x in range(5) if x % 2 == 0]
print(lst) # 0 20 40

# Lehet, hogy így olvashatóbbnak találjuk:

lst = [10*x for x in range(5)
                if x % 2 == 0]

# Vagy esetleg így:

lst = [10*x
       for x in range(5)
           if x % 2 == 0]

# A feladat megoldása hagyományos módon:

# values = []
# for item in collection:
#     if condition:
#         values.append(expression)

# listcomp-pal:

# values = [expression
#           for item in collection
#               if condition]

####################################
