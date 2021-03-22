# package
# __init__.py függvény 1.: package-globális változók kezelése

# https://realpython.com/python-modules-packages/
# http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html

# A logikailag összetartozó modulokat érdemes külön könyvtárakba csoportosítani.
# Package: olyan könyvtár, amely összetartozó modulokat tartalmaz. A példában egy
# pkg nevű könyvtár lesz abban a könyvtárban, ahol az indító szkript van.

# Importálhatjuk az egész könyvtárat is:

import pkg

# ez nem hiba, de ettől még nem fogjuk tudni elérni a könyvtárban lévő modulokat.

################################

# El szoktak helyezni egy __init__.py nevű modult a package-ként szolgáló könyvtárban
# (korábbi Python verzióknál ez kötelező volt), ez lefut, amikor a könyvtárat vagy
# bármelyik benne lévő modult importáljuk. Ebben a package számára globális változókat
# és inicializáló kódot szoktak elhelyezni.

# pkg könyvtárban __init__.py tartalma:

print(f'__init__.py, package neve: {__name__}') # szemléltetéshez

pkg_globals = {'db_url': 'https://valahol/valami', 'max_db_users': 10}

# pack_module_1 tartalma:

from pkg import pkg_globals  # az __init__.py-ban lévő objektumokra hivatkozni tud

def func_1():
    print('func_1 pkg_globals:', pkg_globals)

# test.py tartalma:

from pkg.pack_module_1 import func_1

func_1()

# __init__.py, package neve: pkg
# func_1 pkg_globals: {'db_url': 'https://valahol/valami', 'max_db_users': 10 }

################################

# Akárhányszor importálunk valamit pkg-ból, __init__.py CSAK EGYSZER fog lefutni.

# pack_module_2 tartalma:

from pkg import pkg_globals  # az __init__.py-ban lévő objektumokra hivatkozni tud

def func_2():
    print('func_2 pkg_globals:', pkg_globals)

# test.py tartalma:

from pkg.pack_module_1 import func_1
from pkg.pack_module_2 import func_2

func_1()
func_2()
print('főprogram pkg_globals:', pkg_globals)

# __init__.py, package neve: pkg
# func_1 pkg_globals: {'db_url': 'https://valahol/valami', 'max_db_users': 10 }
# func_2 pkg_globals: {'db_url': 'https://valahol/valami', 'max_db_users': 10 }
# főprogram pkg_globals: {'db_url': 'https://valahol/valami', 'max_db_users': 10 }

################################

# Ha valamelyik modulban modul-szinten megváltoztatunk egy globális változót (ami
# rossz stílus, kerülendő), attól még a többi modul importálásakor az eredeti
# értékek maradnak meg. Megváltoztatjuk pack_module_1-et:

from pkg import pkg_globals  # az __init__.py-ban lévő objektumokra hivatkozni tud

pkg_globals = {}  # nem szép dolog

def func_1():
    print('func_1 pkg_globals:', pkg_globals)

# A kimenet most ez lesz:

# __init__.py, package neve: pkg
# func_1 pkg_globals: {}
# func_2 pkg_globals: {'db_url': 'https://valahol/valami', 'max_db_users': 10 }
# főprogram pkg_globals: {'db_url': 'https://valahol/valami', 'max_db_users': 10 }

# Ez azért fontos, mert az importálás sorrendjétől nem függenek az egyes modulok
# kezdeti értékei.

################################

# Egy másik gyakori megoldás, hogy a package-globális változókat nem __init__.py-ba
# teszik, hanem az erre a célra létrehozott modulba, pl. pkg_globals.py nevűbe.

################################

