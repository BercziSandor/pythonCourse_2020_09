# Változók hatásköre 1.

# https://www.python-course.eu/python3_global_vs_local_variables.php

def func():
    print(x)

x = 'global!'
func()   # global!
# a függvény belsejében látszik a globális változó

# a globális változókat egyébként kerüljük, amennyire csak lehet!

##################

def func():
    x = 'local x'

    print(x)

x = 'global!'
func()   # local x
print(x) # global!

# Belülről kifelé keresi a futtató rendszer a változó értékét.
# Ha a függvényben definiálva van, akkor nem keres tovább.
# Ekkor a globális változó nyilván megtartja előző értékét.

##################

def func():
    print(x)

    x = 'local x'

x = 'global!'
func()   # hibajelzés

# Traceback (most recent call last):
#   File "test.py", line 34, in <module>
#     func()   # hibajelzés
#   File "test.py", line 28, in func
#     print(x)
# UnboundLocalError: local variable 'x' referenced before assignment

# A fordító-futtató rendszer látja, hogy a függvény belsejében definiálva van
# x, ezért lokálisnak veszi, a függvényen kívül nem fogja keresni. Itt viszont
# az ELŐTT akarjuk kiíratni, mielőtt értéket kapott volna.

# Jó módszer: az összes lokális változónak a függvény ELEJÉN adjunk értéket, mímeljük
# a deklarációt. Adhatunk None (definiálatlan) értéket is.

def func():
    x = None
    print(x)

    x = 'local x'

x = 'global!'
func()   # None

# A hiba jelen esetben megmarad, csak áttekinthetőbb a függény, ránézésre
# jobban látszik (talán), hogy mi a baj.

##################

# Ha azt akarjuk, hogy a globális változót használja a függvény, akkor ezt jelezzük
# számára a global kulcsszóval.

def func():
    global x

    print(x)

    x = 'local x'

x = 'global!'
func()    # global!
print(x)  # local x

# Ekkor persze a függvényen belüli módosítások kívül is látszani fognak!
# Pont ez a baj a globális változókkal: nehéz megtalálni, hogy utoljára
# ki és hol módosította őket.

##################
