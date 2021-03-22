# Részleges adatrejtés I.: alulvonás a név elején.

from other_module import *

other_func()   # other_func vagyok
print(other_x) # 100

# _f_local()      # hiba
# print(_x_local) # hiba

# other_module tartalma:

def other_func(): print('other_func vagyok')
other_x = 100

def _f_local(): print('_f_local vagyok')
_x_local = 99

# from other_module import _f_local működik, de nyilván kerülendő.

################################

# Részleges adatrejtés II.: __all__ lista

other_func()   # other_func vagyok
print(other_x) # 100

# f_local()      # hiba
# print(x_local) # hiba

# other_module tartalma:

__all__ = ['other_func', 'other_x']

def other_func(): print('other_func vagyok')

other_x = 100

def f_local(): print('f_local vagyok')
x_local = 99

# from other_module import f_local működik, de nyilván kerülendő.

################################

# Mindkét megoldásnak dokumentációs értéke van és mindkettőt alkalmazhatjuk egyszerre.
# Az alulvonás előnye, hogy a függvény deklarációjára ránézve már látszik, hogy itt
# egy lokális függvényről van szó. Ha nem használunk alulvonást, akkor ez csak úgy derül
# ki, hogy megnézzük, szerepel-e a függvény neve az __all__ listában.

# Az __all__ lista előnye egyrészt, hogy a modulelejét megnézve már látjuk, hogy mely
# objektumok vannak a külvilág számára szánva. A másik előny, hogy más változókon
# keresztül nem tudnak kiszivárogni az elrejteni szánt dolgok.

# other_module tartalma:

def other_func(): print('other_func vagyok')

def _f_local(): print('_f_local vagyok')

ez_is_f_local = _f_local  # hoppá

# Az importáló program:

from other_module import *

ez_is_f_local() # _f_local vagyok

# Ha viszont other_module tartalmaz __all__ listát:

__all__ = ['other_func']

# akkor már nem fog kilátszani _f_local:

ez_is_f_local() # NameError: name 'ez_is_f_local' is not defined

################################
