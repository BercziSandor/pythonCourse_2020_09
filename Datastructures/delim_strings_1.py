# Delimitált sztringek kezelése

# Sztring szétválasztása valamilyen szeparátor (delimiter) szerint:

str_1 = 'a|b|c'
lst = str_1.split('|')
tup = tuple(str_1.split('|'))
print(lst, tup) # ['a', 'b', 'c'] ('a', 'b', 'c')

# Ha a bemenet üres sztring, akkor váratlan az eredmény:

str_1 = ''
lst = str_1.split('|')
print(lst)  # ['']

# Ha ehelyett üres listát akarunk:

if len(str_1) == 0:
    lst = []
else:
    lst = str_1.split('|')

print(lst)

# Ha a sztring végén is van delimiter:

str_1 = 'a|b|c|'
lst = str_1.split('|')
print(lst) # ['a', 'b', 'c', '']

# Adatkonverzióknál ez gyakran okoz gondot. Megoldás:

if len(str_1) == 0:
    lst = []
else:
    if str_1[-1] == '|':
        lst = str_1[:-1].split('|')
    else:
        lst = str_1.split('|')

#########################################

# Lista --> delimitált sztring

lst = ['a', 'b', 'c']
str_ = '|'.join(lst)
print(str_) # a|b|c

# Ha lezáró delimiter is kell:

1. megoldás

lst = ['a','b','c']

str_ = '|'.join(lst) + '|'
print(str_) # a|b|c|

#########################################

# Amivel itt még nem foglalkoztunk: kezelni kell azt a helyzetet is, amikor
# a mezőkben előfordulhat a delimitáló sztring.

#########################################

