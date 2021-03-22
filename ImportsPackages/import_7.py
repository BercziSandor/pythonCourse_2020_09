# Modulok felbontása több fájlra.

# Kiinduló állapot: van egy modulunk két függvénnyel.

# module_AB tartalma:

def func_A():
    print('func_A')

def func_B():
    print('func_B, hívom func_A-t')
    func_A()

# Egy másik modul használja ezt a két függvényt így:

from module_AB import func_A, func_B

func_A()
func_B()

# func_A
# func_B, hívom func_A-t
# func_A

# vagy így:

import module_AB

module_AB.func_A()
module_AB.func_B()

# vagy így:

from module_AB import *

func_A()
func_B()

#########################################

# Szeretnénk a két függvényt két külön modulban elhelyezni úgy, hogy kifelé ez ne látsszon.

# Létrehozunk egy module_AB könyvtárt, ebben három fájl lesz.

# module_A.py tartalma:

def func_A():
    print('func_A')

# module_B.py tartalma:

from .module_A import func_A

def func_B():
    print('func_A')

# __init_.py tartalma:

from .module_A import func_A
from .module_B import func_B

# module_AB-t eltávolítjuk. Ezek után a függvényeket  változatlan formában tudjuk
# használni, így:

from module_AB import func_A, func_B

func_A()
func_B()

# func_A
# func_B, hívom func_A-t
# func_A

# vagy így:

import module_AB

module_AB.func_A()
module_AB.func_B()

# vagy így:

from module_AB import *

func_A()
func_B()

#########################################
