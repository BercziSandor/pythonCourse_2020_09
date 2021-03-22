# Dictionary (szótár) 1.
# tuple kibontása változókba
# zip() függvény
# sorted() függvény

# https://www.python-course.eu/python3_dictionaries.php
# https://realpython.com/python-dicts/
# https://realpython.com/iterate-through-dictionary-python/
# https://www.python-course.eu/python3_zip_tutorial.php

###############################

# Kulcs-érték párokból áll. Üres szótár létrehozása:

dic = {}
dic = dict()
print(type(dic)) # <class 'dict'>

# Különféle  elemeket tartalmazhat, kulcs csak fix (immutable) típus lehet. Hosszát
# (a kulcs-elem párok számát) itt is a len() függvénnyel tudjuk lekérdezni.

dic = {'A': 1, 22: 'twentytwo', 3.5: [20, 20] }
print(dic, len(dic)) # {'A': 1, 22: 'twentytwo', 3.5: [20, 20]} 3

# A szótárban a kulcs szerinti keresés sokkal gyorsabb, mint egy listában való keresés;
# a listában sorban elő kell venni az elemeket, tehát a lista hosszával arányosan nő a
# keresési idő, míg a szótárak hash-táblákat használnak, amelyekben gyakorlatilag konstans
# a keresési idő.

# Látszik, hogy az int és a float típusok immutábilisak, mert lehetnek kulcsok. Nem így a lista:

dic = {[2,3]: 'A'}

# Traceback (most recent call last):
#   File "test.py", line 1, in <module>
#     dic = {[2,3]: 'A'}
# TypeError: unhashable type: 'list'

# vagy egy dict:

dic = {{}: 'A'}

# Traceback (most recent call last):
#   File "test.py", line 1, in <module>
#     dic = {{}: 'A'}
# TypeError: unhashable type: 'dict'

###############################

# Nem indexelhető, viszont iterálható:

dic = {'A': 1, 'B': 2}
for key in dic:
    print(key, '->', dic[key])
# A -> 1
# B -> 2

# Ugyanez lesz az eredmény a keys() metódussal is:

for key in dic.keys():
    print(key, '->', dic[key])

###############################

# Az elemek sorrendje NEM garantált a Python 3.7 verzió előtt; tehát nem biztos,
# hogy iterálásnál ugyanolyan sorrendben kapjuk meg a kulcsokat, mint ahogy azokat
# beleírtuk a szótárba. A 3.7-es verziótól kezdve garantált a sorrend; mindenesetre
# csak akkor építsünk erre a tulajdonságra, ha egészen biztosak vagyunk benne, hogy
# nem fog a programunk régebbi verziókon futni. Ha ez nem biztos, akkor használjuk
# inkább az OrderedDict típust.

# Korábbi verzióknál ha végzünk egy kísérletet egy adott szótárral és azt látjuk, hogy
# megmaradt a beviteli sorrend, az NEM jelenti azt, hogy egy másik, nagyobb szótárral
# is ezt fogjuk kapni!

###############################

# Rendezett tuple-ok listájának előállítása:

dic_1 = {'one': 1, 'two': 2, 'three': 3}
print(sorted(dic_1.items())) # [('one', 1), ('three', 3), ('two', 2)]

# Rendezett szótár előállítása:

dic_2 = dict(sorted(dic_1.items()))
print(dic_2) # {'one': 1, 'three': 3, 'two': 2}

# TERMÉSZETESEN a 3.7 előtti verzióknál NEM lesz garantálva a rendezettség.

###############################

# Ha az értékeken akarunk végigmenni, akkor a values() metódust hívjuk:

for value in dic.values():
    print(value)
# 1
# 2

###############################

# Az items() metódussal egy tuple-ban a kulcsot és az értéket is visszakapjuk:

dic = {'A': 1, 'B': 2}
for item in dic.items():
    print(item)
# ('A',1)
# ('B',2)

# A dict fontos tulajdonsága a listákkal összehasonlítva, hogy sokkal gyorsabb benne
# a keresés.

###############################

# Kitérő: tuple kibontása változókba.

tup = (10, 20)
x, y = tup
print(x, y) # 10 20

##############################

# Az items() által visszaadott  tuple-t kibonthatjuk:

for key, value in dic.items():
    print(key, value)
# A 1
# B 2

# Tartalmazásvizsgálat: in operátor. Kulcsot vizsgál!

dic = {'A': 1, 'B': 2}
print('A' in dic, 2 in dic) # True False

# Érték meglétének vizsgálata:

print(2 in dic.values()) # True

###############################

# Elem megváltoztatása:

dic['A'] = 999
for key, value in dic.items():
    print(key, value)

# A 999
# B 2

# Ha az illető kulcs nem létezik, akkor most létrejön.

dic = {'A': 1, 'B': 2}
dic['C'] = 999

for key, value in dic.items():
    print(key, value)

# A 1
# B 2
# C 999

# Ha nem létező kulccsal olvasnánk: KeyError.

x = dic['xxx']
# Traceback (most recent call last):
#   File "test.py", line 4, in <module>
#     x = dic['xxx']
# KeyError: 'xxx'

###############################

# Elem törlése:

dic = {'A': 1, 'B': 2}

del(dic['A'])

for key, value in dic.items():
    print(key, value)
# B 2

# Ha nem létező elemet akarunk törölni: KeyError.

# Így lehet elkerülni:

if 'ABC' in dic: del(dic['ABC'])

###############################

# Listák, tuple-ok zippzárszerű összefésülése: zip() függvény.

key_lst = ['A', 'B']
val_lst = [1, 2]
zip_obj = zip(key_lst, val_lst)
print(zip_obj)  # <zip object at 0x021BC698>

# Keletkezett egy zip objektum, ami egy generátor típusú iterátor: egyszer szolgáltatja
# valamilyen elemek sorozatát; ha még egyszer szeretnénk megkapni a sorozatot,
# akkor újból fel kell húzni az iterátort, mint egy lendkerekes kisautót. Később
# sok szó lesz az iterátorokról és azon belül a generátorokról, nagyon hasznos eszközök.

# Először járjuk végig az elemeit for ciklussal:

for tup in zip_obj:
    print(tup)

# ('A', 1)
# ('B', 2)

# Töltsük fel ismét a generátort, mert a for ciklus kiürítette:

zip_obj = zip(key_lst, val_lst)

# és csináljunk egy listát a tuple-okból:

lst = list(zip_obj)
print(lst) # [('A', 1), ('B', 2)]

# Töltsük fel ismét a generátort és állítsunk elő egy szótárat a tuple-okból:

zip_obj = zip(key_lst, val_lst)

dic = dict(zip_obj)
print(dic) # {'A': 1, 'B': 2}

###############################

# dict -> tuple-ok listája:

lst = list(dic.items())
print(lst) # [('A',1), ('B',2)]

# tuple-ok listája -> dict:

lst = [('A',1), ('B',2)]
dic = dict(lst)
print(dic)  # {'A': 1, 'B': 2}

###############################
