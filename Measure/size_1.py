# Objektumok mérete
# __sizeof__() metódus, sys.getsizeof() függvény
# pympler.asizeof() függvény

# https://docs.python.org/3/library/sys.html#sys.getsizeof
# https://stackoverflow.com/questions/449560/how-do-i-determine-the-size-of-an-object-in-python
# https://pympler.readthedocs.io/en/latest/library/asizeof.html
# https://pympler.readthedocs.io/en/latest/tutorials/tutorials.html
# https://blog.xoxzo.com/2018/08/08/asizeof-usage/

import sys

lst = []
print(lst.__sizeof__(), sys.getsizeof(lst)) # 20 36

# A sys.getsizeof() azért mond nagyobb számot, mert ő hozzászámolja a garbage collector
# működéséhez szükséges segéd-információ méretét is, ami az 'igazi' objektum mellett van tárolva.

# Egy üres lista 20 bájtot igényel, plusz 16-ot a gc-nek.

lst = [10]
print(lst.__sizeof__(), sys.getsizeof(lst)) # 24 40

# Beletettünk a listába egy négy bájtos mutatót egy elemre, ami most éppen egy
# 10 értékű integer.

# Nem meglepő módon két elemű listánál megint 4 bájttal nő a lista mérete:

lst = [10, 20]
print(lst.__sizeof__(), sys.getsizeof(lst)) # 28 44

##########################################

# Győződjünk meg róla, hogy a lista mérete tényleg a mutató méretével nőtt és
# nem az elem méretével.

x = 2 ** 100
print(x)                                # 1267650600228229401496703205376
print(x.__sizeof__(), sys.getsizeof(x)) # 26 26

# Ez tehát egy 26 bájtos  szám; hogy itt miért nincs gc infó tárolva, azt egyelőre nem
# tudom. Valószínűleg a programban deefiniált konstansokat másképp kezeli.
# Tegyük ezt bele a listába:

lst = [1267650600228229401496703205376]
print(lst.__sizeof__(), sys.getsizeof(lst)) # 24 40

# Ugyanezért ha egy akármilyen hosszú listát teszünk bele egy listába, akkor is
# csak 4 bájttal nő a mérete:

lst = [10]
print(lst.__sizeof__(), sys.getsizeof(lst)) # 24 40

lst = [[10, 20, 30, 40, 50, 60, 70, 80]]
print(lst.__sizeof__(), sys.getsizeof(lst)) # 24 40

##########################################

# A teljes memóriafoglalást a pympler modul segítségével tudjuk meghatározni.

from pympler import asizeof
import sys

lst = [10]
print(lst.__sizeof__(), sys.getsizeof(lst), asizeof.asizeof(lst)) # 24 40 56

lst = [[10, 20, 30, 40, 50, 60, 70, 80]]
print(lst.__sizeof__(), sys.getsizeof(lst), asizeof.asizeof(lst)) # 24 40 240

# Tipp: a pympler modul sokkal pontosabb információt ad.

##########################################

# Függvény-objektumok méretét is le tudjuk kérdezni:

def func_1():
    print('func_1!!')

def func_2():
    lst = [1, 2, 3, 4, 5, 6, 10000000]
    print('func_2 lst =',lst)

print(func_1.__sizeof__(), func_2.__sizeof__())  # 56 56

import sys

print(sys.getsizeof(func_1),sys.getsizeof(func_2))  # 72 72

# Ez a függvény-objektum mérete, NEM a kódé!

##########################################
