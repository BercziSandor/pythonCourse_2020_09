# Változók hatásköre 2.
# Egymásba ágyazott, belső függvények
# global kontra nonlocal

# https://realpython.com/inner-functions-what-are-they-good-for/

# Függvényen belül is lehet definiálni függvényt. Ezt sok hasznos dologra fogjuk tudni használni.
# Első előny: információrejtés. Ha a belső függvény csak segédművelet, amit kívül nem
# használunk, akkor jobb, ha a függvényen kívül nem is látszik.

# A változót belülről kifelé haladva keresi a futtató rendszer.

def func():
    def inner():
        x = 'x inner' # x itt definiálódott
        print(x)

    x = 'x func local'
    inner()

x = 'x global'
func() # x inner

######################################

def func():
    def inner():
        print(x)

    x = 'x func local'
    inner()

x = 'x global'
func() # x func local

######################################

def func():
    def inner():
        print(x)

    inner()

x = 'x global'
func() # x global

######################################

def func():
    def inner():
        print(x)         # itt használom
        x = 'x inner'    # de csak itt definiálom

    inner()

x = 'x global'
func() # hiba, először használom, aztán definiálom

######################################

def func():
    def inner():
        global x

        print(x)
        x = 'x inner'

    inner()

x = 'x global'
func() # x global
print('x func() után:', x) # x func() után: x inner

######################################

# A global-nak deklarált változókat a tartalmazó függvényben NEM keresi.

def func():
    def inner():
        global x

        print(x)

    x = 'x func local'  # nem ezt találja meg
    inner()

x = 'x global'
func() # x global

######################################

# A nonlocal-nak deklarált változókat a legkülső függvényen kívül (modul szinten) nem keresi.

# Ez rendben van:

def func():
    def inner():
        nonlocal x

        print(x)

    x = 'x func local'
    inner()

x = 'x global'
func() # x func local

# De ez nem működik:

def func():
    def inner():
        nonlocal x

        print(x)  # itt használná

    inner()

x = 'x global'
func() # hiba

# x hiába van modul-szinten definiálva, ott már nem keresi.

# Ez sem működik:

def func():
    def inner():
        nonlocal x

        print(x)  # itt használná

    inner()

    x = 'x func local' # de csak itt definiálódik

x = 'x global'
func() # hiba

# A felhasználáskor még nem volt definiálva x.

######################################

# A belső függvény a tartalmazó függvénynek a bemenő paramétereit is látja.

def func(outerParam):
    def inner():
        print('inner:',outerParam)

    inner()

x = 'x global'
func('func parameter') # func parameter

# Ezt sok helyen fogjuk használni.

##################
