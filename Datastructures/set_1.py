# set (halmaz) 1.

# Minden elemet csak egyszer tartalmaz; csak fix, immutábilis típusok lehetnek az elemei.

set_1 = { 1, 2, 3 }
set_1.add(2)
print(set_1, type(set_1)) # {1, 2, 3} <class 'set'>

lst_1 = [1, 1, 2, 2, 3, 3]
set_1 = set(lst_1)
print(set_1)  # {1, 2, 3}

# Nem megy:

#set_1 = {}  # dict-nek gondolja
#set_1.add(3)









