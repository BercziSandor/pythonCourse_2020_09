# package
# __init__.py függvény 2.: automatikus import; __all__ lista

# https://realpython.com/python-modules-packages/

# Az __init__.py modulban elhelyezhetünk importálást is.

# __init__.py tartalma:

print(f'__init__.py, package neve: {__name__}') # szemléltetéshez

import pkg_2.pack_module_1, pkg_2.pack_module_2

# pack_module_1.py tartalma:

def func_1():
    print('func_1')

# pack_module_2.py tartalma:

def func_2():
    print('func_2')

# A főprogram:

import pkg_2  # __init__.py révén importálódik pack_module_1, pack_module_2

pkg_2.pack_module_1.func_1()
pkg_2.pack_module_2.func_2()

# __init__.py, package neve: pkg_2
# func_1
# func_2

################################

# Az import *-ot package esetében is kerülni szoktuk a név-ütközések esélyének minimalizálása
# érdekében. Az __init__.py-ban érdemes elhelyezni egy __all__ listát, csakúgy, mint a modulokban.
# import * esetében ez korlátozza az importált modulok körét + dokumentációs értéke is van.
# Az egyes modulokon belül is persze érdemes használni a __all__ listát.

# Ha nincs az __init__.py-ban __all__ lista, akkor az import * semmit nem importál.

# # __init__.py tartalma legyen most:

__all__ = ['pack_module_1']

# pack_module_1.py tartalma:

def func_1():
    print('func_1')

# pack_module_2.py tartalma:

def func_2():
    print('func_2')

# A főprogram:

from pkg_3 import *

pack_module_1.func_1() # func_1
pack_module_2.func_2() # hiba

print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', 'pack_module_1']

################################
