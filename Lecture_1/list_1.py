# Listák 1. És egy kevés sztring.

x = [10, 20, 30]
print(x, type(x), len(x))  # [10, 20, 30] <class 'list'> 3

# A hosszat ugyanúgy a len() függvénnyel kérdezzük le, mint a sztringeknél.

# Különféle típusú elemeket tartalmazhat

x = [10, 'John', 32.5]  # [10, 'John', 32.5]
print(x)

# Nemcsak alaptípusokat tartalmazhat, hanem listát és egyéb összetett típusokat is.

lst = [1, ['A', 2], 'B']  # a második elem egy lista
print(lst, len(lst))  # [1, ['A', 2], 'B'] 3

# Üres lista készítése

x = []
y = list()
print(x, y)  # [] []

# Indexelhető

x = [10, 'John', 32.5]
print(x[0], x[len(x) - 1])  # 10 32.5

# Iterálható, for ciklussal bejárható

for e in x:
    print(e, end=' ')  # 10 John 32.5
print()

# Nem pythonikus for ciklus - működik, de szószátyár és ezért utáljuk.
# Az i változóra semmi szükség nincs!

for i in range(len(x)):   # hivatalból üldözendő!
    print(x[i], end=' ')
print()  # 10 John 32.5

# Módosítható

x[1] = 'Jane'
print(x)  # [10, 'Jane', 32.5]

# Új elem hozzáfűzése (append)

x.append('new item')
print(x)  # [10, 'Jane', 32.5, 'new item']

# Elem törlése (del)

del(x[1])
print(x)  # [10, 32.5, 'new item']

# A sztringeknél nincs append metódus. Miért?

# Teljes lista törlése

x = []

# Ekkor x egy ÚJ, üres listára mutat! Lássuk:

x = [1, 2, 3]
id_1 = id(x)

x = []
id_2 = id(x)
print(id_1, id_2)  # 7202696 7202136

# id(x): az x változó által megjelölt elem memóriacíme decimálisan.
# Látható, hogy a két memóriacím nem egyezik; 7202696 címen van
# az eredeti lista, rá már egyetlen változó sem mutat, a futtató
# rendszer ezt észreveszi és felszabadítja a memóriát.

#####################

# Teljes lista törlése és a változó megsemmisítése.
# Ritkán csináljuk: Ha nagyon nagy a lista és kevés a
# memória --> mikor már nem kell, töröljük.
# Egyébként a futtató rendszer úgyis automatikusan felszabadítja
# a memóriát, amikor már egy változó sem mutat az illető elemre.

del(x)  # megszüntetjük az x nevet
print(x)

# Traceback (most recent call last):
#   File "test.py", line 51, in <module>
#     print(x)
# NameError: name 'x' is not defined

# Csak a NÉV szűnik meg a del()-től!!!

x = [1, 2, 3]
y = x
print(y)  # [1, 2, 3] y ugyanarra a memóriacímre mutat, mint x

del(x)    # megszüntetjük az x nevet
print(y)  # [1, 2, 3] y memgmaradt
del(y)
print(y)  # de most maár nincs

# Traceback (most recent call last):
#   File "test.py", line 57, in <module>
#     print(y)
# NameError: name 'y' is not defined
