# Adatszerkezetek egymásba alakítása

# list <--> tuple

lst = [1, 2, 3, 4]
tup = tuple(lst)
print(tup)   # (1, 2, 3, 4)

lst = list(tup)
print(lst)   # [1, 2, 3, 4]

#########################################

# Sztring --> lista, tuple

str_1 = 'ABCD'
lst = list(str_1)
tup = tuple(str_1)
print(lst, tup)  # ['A', 'B', 'C', 'D'] ('A', 'B', 'C', 'D')

#########################################

# Lista --> sztring 1. kísérlet

lst = [1, 2, 3, 4]
str_1 = str(lst)
print(str_1) # [1, 2, 3, 4] nem az igazi

# Sztringek listája --> sztring

lst = ['A', 'B', 'C']
str_1 = ''.join(lst)
print(str_1)  # ABC

# Nem (csak) sztringek listája --> sztring

# 2 lépésban:

lst = [1, 2, 3, 4]
lst_2 = [str(i) for i in lst]
print(lst_2)  # ['1', '2', '3', '4']

str_1 = ''.join(lst_2)
print(str_1)  # 1234

# Egyszerre a két lépés:

str_1 = ''.join([str(i) for i in lst])
print(str_1)  # 1234

#########################################

# List, tuple --> set

lst = [1, 1, 2, 2, 2, 3]
set_1 = set(lst)
print(set_1)  # {1, 2, 3}

tup = (1, 1, 2, 2, 2, 3)
set_1 = set(tup)
print(set_1)  # {1, 2, 3}

#########################################

# set --> list, tuple

set_1 = {1, 2, 3}
lst = list(set_1)
tup = tuple(set_1)
print(lst,tup)  # [1, 2, 3] (1, 2, 3)

#########################################

# dict inicializálása set-ből

set_1 = {1, 2, 3}
dic = {key:0 for key in set_1}
print(dic)  # {1: 0, 2: 0, 3: 0}

#########################################

# dict kulcsok --> set

dic = {'A': 10, 'B': 20, 'C': 30}
set_1 = set(dic.keys())
print(set_1)  # {'B', 'A', 'C'}

#########################################

# dict értékek --> set

dic = {'A': 10, 'B': 20, 'C': 30}
set_1 = set(dic.values())
print(set_1)  # {10, 20, 30}

#########################################

# dict kulcsok, értékek --> list, tuple

dic = {'A': 10, 'B': 20, 'C': 30}
lst = list(dic.values())
tup = tuple(dic.keys())
print(lst,tup)   # [10, 20, 30] ('A', 'B', 'C') a sorrend nem garamtált

#########################################

# dic.keys() helyett a listává alakításnál használhatjuk magát dic-et is:

dic = {'A': 10, 'B': 20, 'C': 30}

lst = list(dic)
print(lst)  # ['A', 'B', 'C']

# Ez azért van így, mert dic.keys dic iterátora.

#########################################

# Értékpárok listája --> dict

lst = [('A',10), ('B',20), ('C',30)]
dic = dict(lst)
print(dic) # {'A': 10, 'B': 20, 'C': 30}

#########################################

# Két lista összefésülése kételemű tuple-ok listájává

lst_1 = ['A', 'B', 'C']
lst_2 = [10, 20, 30]
lst = list(zip(lst_1, lst_2))
tup = tuple(zip(lst_1, lst_2))
print(lst) # [('A', 10), ('B', 20), ('C', 30)]
print(tup) #(('A', 10), ('B', 20), ('C', 30))

#########################################

# Két lista összefésülése dict-be

lst_1 = ['A', 'B', 'C']
lst_2 = [10, 20, 30]
dic = dict(zip(lst_1, lst_2))
print(dic)  # {'A': 10, 'B': 20, 'C': 30}

#########################################

# dict --> kulcsok listája, értékek listája
# (Úgy, hogy az azonos index elemek összetartozzanak.)

# NEM (mindig) jó megoldás:

dic = {'A': 10, 'B': 20, 'C': 30}

key_lst = list(dic.keys())
val_lst = list(dic.values())
print(key_lst,val_lst)  # ['A', 'B', 'C'] [10, 20, 30]

# Nincs garantálva, hogy keys() és values() ugyanabban
# a sorrendben adja ki az elemeket! Nagyon gonosz
# hibát tud okozni.

# Jó megoldás

# 1. lépés: elempárok listáját csinálunk a szótárból:

dic = {'A': 10, 'B': 20, 'C': 30}
lst_pairs = list(dic.items())
print(lst_pairs)  # [('A', 10), ('B', 20), ('C', 30)]

# 2. lépés: szétszedjük két listára:

key_lst = [e[0] for e in lst_pairs]
val_lst = [e[1] for e in lst_pairs]
print(key_lst)  # ['A', 'B', 'C']
print(val_lst)  # [10, 20, 30]

# Vagy "hagyományos" for ciklussal:

key_lst = []; val_lst = []
for key, value in dic.items():
    key_lst.append(key)
    val_lst.append(value)

print(key_lst,val_lst)

#########################################

# TETSZŐLEGES iterátorból így csinálunk listát, ill. tuple-t:

# list(it)
# tuple(it)

# Végighalad az iterálható elemen és elhelyezi a kapott egységeket
# egy list-ben vagy egy tuple-ban.

# A list és a tuple olyan iterálható elemek, amelyek önmaguk iterátorai is.

# python_intro.html-ben van ez a kis iterálható osztály,
# ami egyben az iterátor is:

class StupidCounter:
    def __init__(self):
        self.count = 0

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count > 3:
            raise StopIteration

        ret_val = self.count
        self.count += 1
        return ret_val

c = StupidCounter()
lst = list(c)
print(lst)  # [0, 1, 2, 3]

#########################################
