# Egy belső függvény hozzáfér az őt tartalmazó függvény paramétereihez:

def func(funcParam):
    def inner():
        print(f'funcParam = {funcParam}')

    inner()

func(55) # funcParam = 55

#######################################

# A külső függvény visszaadhat a belső függvényre mutató referenciát visszatérő értékként:

def func():
    def inner():
        print('helló világ')

    print(inner)  # <function func.<locals>.inner at 0x0217B780>

    return inner

f = func()
print(f) # <function func.<locals>.inner at 0x0217B780>
f()      # helló világ

# Az f() hívás valójában inner() meghívása.

#######################################

# Most jön a csavar: a belső függvény emlékszik a tartalmazó függvény paramétereire.

def func(funcParam):
    def inner():
        print(f'funcParam = {funcParam}')

    return inner

f = func(55)
f() # funcParam = 55

# Ezt hívják (lexical) closure-nek.

# Mire lehet jó?

# A belső függvény ugyanúgy megjegyzi a kezdetben kapott paramétereket, mint egy
# objektum. Ezért ezt bizonyos esetekben objektum definiálása helyett használjuk,
# amitől egyszerűbb lesz a programunk (ld. később).

#######################################
