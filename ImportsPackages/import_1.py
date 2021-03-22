# https://realpython.com/python-modules-packages/
# https://docs.python.org/3/reference/import.html
# https://docs.python.org/3/tutorial/modules.html
# https://www.youtube.com/watch?v=CqvZ3vGoGs0

# Import variációk

# 1. eset: Az importálandó fájlok ugyanabban a könyvtárban vannak, mint az importáló szkript.

# module_1.py:

def func_1():
    print('I am module_1 func_1')

##************

# 1. módszer:

import module_1

# module_1. előtaggal tudunk hivatkozni az ott definiált elemekre:

module_1.func_1() # I am module_1 func_1

# 2. módszer:

import module_1 as m_1

m_1.func_1() # I am module_1 func_1

# 3. módszer:

from module_1 import func_1

func_1() # I am module_1 func_1

# 4. módszer:

from module_1 import func_1 as f_1

f_1() # I am module_1 func_1

# 5. módszer - általában kerülendő a lehetséges névütközések miatt.

from module_1 import *

func_1() # I am module_1 func_1

###################################

# Mi történik, ha két azonos nevű objektumot importálunk?

from module_1 import func_1
from module_2 import func_1

func_1() # I am module_2 func_1

# Az utolsó import érvényesül. Ha legalább az egyiket átnevezzük, akkor persze
# megoldódik a probléma:

from module_1 import func_1
from module_2 import func_1 as f_1

func_1() # I am module_1 func_1

# Az 5. módszer azért rossz, mert ott nem tudunk átnevezni.

###################################

# A modulok is objektumok.

# A dir() függvénnyel lekérdezhetők a szolgáltatásaik.

import module_1

print(dir(module_1)) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'func_1']

# Ezt nem szoktuk csinálni, csak szemlélteti, hogy a modul is egy objektum:

import module_1

module_1.func_1() # I am module_1 func_1

del(module_1)     # !!! ilyet ne tegyünk !!!
module_1.func_1()

# Traceback (most recent call last):
#   File "test.py", line 5, in <module>
#     module_1.func_1()
# NameError: name 'module_1' is not defined

###################################

# A függvények megjegyzik, hogy melyik modulból származnak:

from module_1 import func_1

print(func_1.__module__) # module_1

###################################

# Kipróbálásra ajánlom:

import this

# és

import antigravity

###################################

