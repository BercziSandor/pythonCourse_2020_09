# https://www.python-course.eu/python3_blocks.php
# https://www.python-course.eu/python3_conditional_statements.php
# https://www.python-course.eu/python3_loops.php
# https://www.python-course.eu/python3_for_loop.php
# https://www.python-course.eu/python3_print.php

# Deklaráció nincs (elég baj az), a változó ott definiálódik, ahol
# először értéket kap

x = 1  # itt definiálódik x

# Típusellenőrzés sincs (ez is elég baj), ugyanazon változónevet ezután
# hozzárendelhetünk egy másik típusú változóhoz:

x = 'A'

# Feltételes utasítás: if

x = 5
if x < 4:
    print('kisebb')
else:
    print('nem kisebb')

if x > 10:
    print('nagy')
elif x < 1:
    print('pirinyó')
elif x < 2:
    print('kicsi')
else:
    print('közepes')

# Blokkot kezdő sor (for, while, if, def class...) végén kettőspontnak kell lenni.
# Egy blokkon belül egyformának kell lennie az indentálásnak:

x = 5
if x < 4:
    print('kisebb')
   print('négynél')

#   File "test.py", line 4
#     print('négynél')
#                     ^
# IndentationError: unindent does not match any outer indentation level

##########################

# Egy sorba lehet több utasítást is írni pontosvesszővel elválasztva:

print(1); print(2)

# de általában ezt az olvashatóság érdekében kerülni szoktuk.

# A kettőspont után is írhatunk utasítást (ezt is ritkán tesszük):

x = 10
if x < 20: print(1);

##########################

# Ha egy utasítás nagyon hosszú, akkor folytathatjuk a következő sorban; ilyenkor
# a sor végére \-t kell tenni:

x = 1
y = 1
if x == 1 and \
y == 1:
  print(x)

# A \ után már ne legyen semmi, egy szóköz sem!

# Adatszerkezet belsejében nem kell \:

x = [1,
2]
print(x) # [1, 2]

# Ez a sztringek belsejére nem vonatkozik:

x = 'A
B' # szintaktinai hiba

##########################

# Szintaktikai hibák rejtve tudnak maradni, amíg nem megy rájuk a vezérlés;
# ez talán a legnagyobb baj.

x = 5
if x < 4:
    xxxprint('kisebb')   # hoppá
else:
    print('nagyobb')

# --> gondos tesztelés szükséges.

##########################

# while ciklus

x = 3
while x >= 0:
    print(x)
    x -= 1

# 3
# 2
# 1
# 0

##########################

# print variációk

# Ha azt akarjuk, hogy a print utasítás ne sorvégjelet tegyen a végére:

x = 3
while x > 0:
    print(x, end=' ')
    x -= 1
print()   # 3 2 1

x = 1
y = 10
print(x, y)  # 1 10

# Ha azt akarjuk, hogy a kiírt elemek közé ne egy szóközt tegyen:

print(x, y, sep=';')  # 1;10

# Ha a print zárójelek nélkül áll: Python 2 kód.

# A print utasítás a standard kimenetre ír. A standard hibakimenetre így tudunk írni:

import sys

print('Hiba történt', file=sys.stderr)

##########################

# Számsorozat előállítására szolgáló objektum: range; és for ciklus

for i in range(4):
    print(i, end=' ')
print()              # 0 1 2 3

# Az alapértelmezett range kezdőérték nulla; a paraméterként megadott végértéknél
# eggyel kisebb lesz az utolsó kiadott érték.

# Kezdőértéket is megadhatunk:

for i in range(1, 5):
    print(i, end=' ')
print()              # 1 2 3 4

# Lépésközt is:

for i in range(2, 7, 2):
    print(i, end=' ')
print()              # 2 4 6

# ami persze lehet negatív is:

for i in range(5, 2, -1):
    print(i, end=' ')
print()              # 5 4 3

# Ilyenkor is a lezáró érték ELŐTTI elem az utolsó.

# A range tényleg egy objektum (mint a Pythonban MINDEN):

x = range(4)
print(x)  # range(0,4)

##########################

# Ha egy kifejezést leírunk és nem rendeljük hozzá egy változóhoz, akkor nem történik semmi.

x = 3
x + 7 # nem hiba

##########################
