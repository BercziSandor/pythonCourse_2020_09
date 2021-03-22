# https://docs.python.org/3/reference/import.html
# https://realpython.com/python-modules-packages/

# Import variációk

# 2. eset: Az importálandó fájlok más a könyvtárban vannak, mint az importáló szkript.

# module_1.py legyen pl. az importáló szkript könyvtára alatti ImportsPackages könyvtárban.

# module_1.py:

def func_1():
    print('I am module_1 func_1')

##************

# 1. módszer:

import ImportsPackages.module_1  # ponttal van elválasztva!

ImportsPackages.module_1.func_1() # I am module_1 func_1

# Ez persze általában elég körülményes és nehezen olvasható.

# 2. módszer:

import ImportsPackages.module_1 as m_1

m_1.func_1() # I am module_1 func_1

# 3. módszer:

from ImportsPackages.module_1 import func_1

func_1() # I am module_1 func_1

# 4. módszer:

from ImportsPackages.module_1 import func_1 as f_1

f_1() # I am module_1 func_1

# 5. módszer - általában kerülendő a lehetséges névütközések miatt.

from ImportsPackages.module_1 import *

func_1() # I am module_1 func_1

###################################
