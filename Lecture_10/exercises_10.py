# 1.)

# Írjunk dekorátort, amely olyan függvényekre alkalmazható, melyeknek a visszatérő
# értéke int vagy float típusú. Ha az eredeti függvény visszatérő értéke nagyobb,
# mint 10, akkor a dekorált függvény visszatérő értéke legyen 10.

@limit_decorator
def func(a, b):
    return a + b

x = func(2, 20)
print(x)  # 10

############################################

# 2.)

# Írjuk meg a fenti dekorátor paraméterezett változatát. A paraméter legyen a küszöbérték,
# amely felett ezt adja vissza a dekorált függvény.

@limit_decorator_param(10)
def func(a, b):
    return a + b

x = func(2, 20)
print(x)  # 10

############################################

# 3.)

# A feladat az, hogy egy bemeneti számsorozatból ki kell szűrni a hattal oszthatóakat
# és a kimenetre ki kell adni a megmaradó számok háromszorosát kétszer: egyszer saját,
# egyszer ellenkező előjellel. A megoldáshoz az exercises_8.py 5. és 6. feladatában
# megtervezett generátorokat használjuk!

lst = [10, -1, -12, 2]

# ???
# 30 -30 -3 3 6 -6

############################################

# 4.)

# Írjunk dekorátort, amelyet olyan függvényeken akarunk alkalmazni, amelyeknek egyetlen
# paramétere van. A dekorátor a tesztelést hivatott segíteni; a kimenete legyen egy tuple,
# melynek első tagja a függvény paramétere, a második pedig a függvény visszatérő értéke.

@out_decor
def func_1(number):
    return 2 * number

lst = [10, 20, 30, 40]

for e in lst:
    print(func_1(e), end=' ')
print()

# (10, 20) (20, 40) (30, 60) (40, 80)

############################################
