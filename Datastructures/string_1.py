# Sztringek (str) 1.

# https://www.python-course.eu/python3_sequential_data_types.php

# ' és " egyenrangü

x = 'abc'
y = "abc"
print(x, y, type(x))  # abc abc <class 'str'>

x = 'ab"c'  # ''-on belül lehet "
y = "ab'c"  # ""-on belül lehet '
print(x, y)  # ab"c ab'c

# Ha ''-on belül '-ot akarok írni:

x = 'McDonald\'s'
print(x)  # McDonald's

###################################

# Főleg több soros sztringekhez; több sor megjegyzésbe tevéséhez is praktikus;
# megőrzi a sorvégjeleket:

x = '''1. sor 'első'
2. sor "második"
'''
print(x)

# 1. sor 'első'
# 2. sor "második"

y = """1. sor 'első'
2. sor "második"
"""
print(x)
# 1. sor 'első'
# 2. sor "második"

###################################

# Konkatenálás

x = 'Py'
y = "thon"

print(x + y + " rocks")  # Python rocks

# Konstansok konkatenálása + jel nélkül is lehetséges.

x = "AA" 'BB'
print(x)  # AABB

###################################

# Ismételt összeadás helyett használhatunk szorzást:

x = 'AB' + 'AB' + 'AB'
print(x) # 'ABABAB'

x = 'AB' * 3
print(x) # 'ABABAB'

###################################

# Több sorba így írhatjuk:

x = "AA" \
    'BB'
print(x)  # AABB

# A \ után már semmi ne legyen!

x = "A\
A" \
'BB'
print(x)  # AABB

# Ez miért nem ugyanaz, mint az alábbi?

x = """AA
BB"""

###################################

# Sorvég-jel ('\n')és tabulátor ('\t') - mint C-ben, PHP-ben...

x = "a\t\tb\ncd"
print(x)

# a		b
# cd

###################################

# raw string, amikor a metakarakterek nincsenek kifejtve:

x = r"a\t\tb\ncd"
print(x)  # a\t\tb\ncd

# \ a sztringben: duplázni kell (vagy raw stringet alkalmazni):

x = 'c:\\Users'
print(x)  # c:\Users

x = r'c:\Users'
print(x)  # c:\Users

###################################

# Indexelés (az str típus indexelhető)

x = 'ABCD'
print(x[0], x[3], type(x[3]))  # A D <class 'str'>

# Egyetlen karakter típusa is str, nincs char típus

###################################

# iterálható, for ciklussal bejárható

x = "abc"
for e in x:
    print(e, end=' ')

# a b c

# Nem változtatható (immutable)

x = "abc"
x[0] = "A"

# Traceback (most recent call last):
#   File "test.py", line 54, in <module>
#     x[0] = "A"
# TypeError: 'str' object does not support item assignment

###################################

# Hossz lekérdezése:

x = "abc"
print(len(x))  # 3

# Tartalmazásvizsgálat: in operátor

x = 'ABC'
print('B' in x, 'BC' in x, 'D' in x)  # True True False

# Nemcsak egyetlen karaktert, hanem egynél hosszabb sztringet is kereshetünk így.

###################################

# Néhány gyakran használt metódus
# Kisbetű - nagybetű

x = "ABC"
y = x.lower()
z = y.upper()
print(x, y, z)  # ABC abc ABC

# Fehér karakterek levágása elejéről és végéről

x = "  A     "
y = x.rstrip()
z = x.lstrip()
w = x.strip()
print(x, y, z, w, sep='|', end='|\n')  # A     |  A|A     |A|
print(len(x), len(y), len(z), len(w))  # 8 3 6 1

###################################

# A metódusok láncba kapcsolhatók (mindig, nemcsak a sztringeknél)

x = "     ABC    "
y = x.strip().lower()
print(y, len(y))  # abc 3

# Egyéb típusok sztringgé alakítása: str() függvény

# print(1 + "A")    # hiba
print(str(1) + "A")  # 1A

###################################
