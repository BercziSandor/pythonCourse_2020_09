# set és dict comprehension

# a set és a dict adatszerkezeteknél teljesen ugyanazon logikával épül fel
# a comprehension, mint a listánál.

# Adott egy lista, a páros elemeinek a tízszeresét vegyük fel egy halmazba.

# Hagyományos megoldás:

lst_1 = [1, 1, 2, 2, 3, 4, 4, 4]
set_ = set()
for x in lst_1:
    if x % 2 == 0:
        set_.add(10*x)

print(set_)  # {40, 20}

# Comprehension:

set_ = {10*x
       for x in lst_1
           if x % 2 == 0}
print(set_)  # {40, 20}

# Általánosan megfogalamazva a hagyományos alak:

# result_set = set()
# for item in collection:
#     if condition:
#         result_set.add(expression)

# Comprehension:

# result_set = { expression for item in collection if condition }

# A collection persze nem feltétlenül lista, lehet bármely iterálható sorozat.

#################################

# Nem meglepő módon dictionary comprehension is létezik.

# Adott egy szótár:

dic_1 = {'A': 10, 'B': 20, 'C': 30}

# Egy másik szótárba gyűjtsük ki azokat az elemeket, ahol az érték nagyobb 15-nél.

# Hagyományos megoldás:

dic_2 = dict()
for key, value in dic_1.items():
    if value > 15:
        dic_2[key] = value

print(dic_2) # {'B': 20, 'C': 30}

# Comprehension:

dic_2 = {key: value
         for key, value in dic_1.items()
         if value > 15}
print(dic_2) # {'B': 20, 'C': 30}

#################################
