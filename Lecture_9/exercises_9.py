# 1.)

# Egy numpy tömbnek minden olyan elemét el kell osztani 7-tel, amely osztható 7-tel.

arr_1 = np.array([[10, 22, 21], [35, 14, 40]])
print(arr_1)
# [[10 22 21]
#  [35 14 40]]

# ???

print(arr_1)
# [[10 22  3]
#  [ 5  2 40]]

############################################

# 2.)

# Írjunk dekorátort, amely olyan függvényekre alkalmazható, melyeknek a visszatérő
# értéke list, tuple vagy str. A dekorált függvvény kimenete legyen az eredeti fordítottja.

@reverse_decorator
def func_1(p1, p2):
    return p1 + p2

print(func_1('AB', 'CD')) # DCBA

@reverse_decorator
def func_2(p):
    return p.lower()

print(func_2('ABCD')) # dcba

############################################

# 3.)

# Készítsünk dekorátort, amelyet olyan függvényekre lehet alkalmazni, amelyek számokból
# álló listát adnak vissza. A dekorált függvény kimenetén azon elemek legyenek 0-ák,
# amelyek abszolút értéke 0.01-nél kisebb.

@round_deco
def f_1():
    return [10, -0.005, 0.2, 3, 0.0004]

print(f_1()) # [10, 0, 0.2, 3, 0]

############################################

# 4.)

# Írjuk meg a fenti dekorátor paraméterezett változatát. A paraméter legyen a küszöbérték,
# amely alatt nullát ad vissza a dekorált függvény.

@round_deco_param(0.01)
def f_1():
    return [10, -0.005, 0.2, 3, 0.0004]

print(f_1()) # [10, 0, 0.2, 3, 0]

############################################

# 5.)

# Írjunk generátor függvényt, amely paraméterként egy egész számokat szolgáltató
# iterátort kap és visszaadja ezen számok közül a hattal nem oszthatóakat hárommal megszorozva.

def gen_func_1(numbers):
    pass

lst = [10, -1, -12, 2]
g = gen_func_1(lst)
for e in g:
    print(e, end=' ')
print()

# 30 -3 6

############################################

# 6.)

# Írjunk generátor függvényt, amely paraméterként egy egész számokat szolgáltató
# iterátort kap és visszaadja minden számot kétszer: egyszer változatlan és egyszer
# ellenkező előjellel.

def gen_func_2(numbers):
    pass

lst = [10, 20, -30]
g = gen_func_2(lst)
for e in g:
    print(e, end=' ')
print()

# 10 -10 20 -20 -30 30

############################################
