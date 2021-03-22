# 1.)

# Írjunk dekorátort, amelyet számsorozatot szolgáltató függvényekre lehet alkalmazni.
# Ha az elemek között van 50-nél nagyobb, akkor  dobjon ValueError kivételt.

def limit_decor(funcToBeDecorated):
    pass

@limit_decor
def func(param):
    return [2 * e for e in param]

try:
    lst = None
    lst = func([10, 20, 30])
except ValueError as ex:
    print(ex) # túl nagy! 60 > 50

############################################

# 2.)

# Írjuk meg a fenti dekorátor paraméterezett változatát, a paraméter legyen
# a határérték.

def limit_decor_param(limit): pass

@limit_decor_param(55)
def func(param):
    return [2 * e for e in param]

try:
    lst = None
    lst = func([10, 20, 30])
except ValueError as ex:
    print(ex)  # túl nagy! 60 > 55

############################################

# 3.)

# A feladat ugyanaz, mint Lecture_11\exercises_11.py 3. feladatában:

# Írjunk iterátort, amely inicializáláskor egy iterálható obkektumot és egy
# egész számot kap paraméterként. Azokat az elemeket adja vissza a bemeneti objektum
# által szolgáltatott sorozatból, amelyek oszthatóak a számmal.

# de most osztály helyett generátor-függvénnyel oldjuk meg a feladatot.

def modIterFunc(inputSeries, number):
    pass

m = modIterFunc(range(19), 6)

for e in m:
    print(e)

# 0
# 6
# 12
# 18

############################################
