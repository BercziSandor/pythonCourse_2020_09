# Változók hatásköre 2.
# Egymásba ágyazott, belső függvények

# Függvényen belül is lehet definiálni függvényt. Ezt sok hasznos dologra fogjuk tudni használni.
# Első előny: információrejtés. Ha a belső függvény csak segédművelet, amit kívül nem
# használunk, akkor jobb, ha a függvényen kívül nem is látszik.

# A változót belülről kifelé haladva keresi a futtató rendszer.

def func():
    def inner():
        x = 'x inner'
        print(x)

    x = 'x func local'
    inner()

x = 'x global'
func() # x inner

def func():
    def inner():
        print(x)

    x = 'x func local'
    inner()

x = 'x global'
func() # x func local

def func():
    def inner():
        print(x)

    inner()

x = 'x global'
func() # x global

def func():
    def inner():
        print(x)
        x = 'x inner'

    inner()

x = 'x global'
func() # hiba, először használom, aztán definiálm

def func():
    def inner():
        global x

        print(x)
        x = 'x inner'

    inner()

x = 'x global'
func() # x global

def func():
    def inner():
        global x

        print(x)

    x = 'x func local'
    inner()

x = 'x global'
func() # x global

# A global-nak deklarált változókat a tartalmazó függvényben NEM keresi.

def func():
    def inner():
        nonlocal x

        print(x)

    inner()
    x = 'x func local'

x = 'x global'
func() # hiba

# A nonlocal-nak deklarált változókat a legkülső függvényen kívül (modul szinten) nem keresi.

##################

def func(param):
    def inner():
        print('inner:',param)

    x = 'x func local'

    inner()

x = 'x global'
func('func parameter') # func parameter

# A belső függvény a tartalmazó függvénynek a bemenő paramétereit is látja.


