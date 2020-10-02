# Függvény-objektumok 1.

# A Pythonban a függvények is objektumok.

# Többek közt van memóriacímük és méretük.

def func_1():
    print('func_1!!')

def func_2():
    lst = [1, 2, 3, 4, 5, 6, 10000000]
    print('func_2 lst =',lst)

import sys

print(func_1)  # <function func_1 at 0x0058D660>

# Figyelem - zárójel nélkül! Nem hívtuk meg a függvényt.

print(sys.getsizeof(func_1),sys.getsizeof(func_2))  # 72 72

# Ez a függvény-objektum mérete, NEM a kódé!

# Ha func_1 egy objektum, akkor le tudjuk kérdezni a tulajdonságait.

d = dir(func_1)  # visszaadja az objektum összes attribútumát és metódusát egy listában
print(d)

# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__',
# '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__']

# Lekérdezhetjük a két függvény-objektum méretét:

print(func_1.__sizeof__(), func_2.__sizeof__())  # 56 56

# A sys.getsizeof() azért mond nagyobb számot, mert ő hozzászámolja a garbage collector működéséhez szükséges segéd-információ
# méretét is, ami az 'igazi' objektum mellett van tárolva.

# Nem meglepő módon van neki __call__ metódusa, hívjuk ezt meg:

func_1.__call__()  # func_1!!

# Amikor meghívjuk func_1-et, akkor tulajdonképpen a func_1 objektum __call__ metódusát hívjuk meg.

# Van neki neve, be tud mutatkozni és meg tudja mondani, milyen osztály példánya ő:

# print(func_1.__name__, func_1.__class__)) # func_1 <class 'function'>

# Tanítsuk meg hazudni:

func_1.__name__ = 'James Bond'
print(func_1.__name__)  # James Bond

# Ha func_1 egy objektum, akkor másik változó is mutathat rá:

f = func_1
f()               # func_1!!
print(f.__name__) # James Bond

#################################

# Egy függvénydeklaráció:

def func(x):
    return 2 * x

# két dolgot csinál:

# 1. Nemcsak LEÍRJA, milyennek kell lennie egy ilyen függvényobjektumnak, hanem
#    rögtön létre is hoz egyet. Ez tehát egy konstruktor, ami le is fut.
# 2. Hozzá is rendel egy változónevet (func) az újszülötthöz.

#################################

# Ha a függvény egy objektum, akkor át lehet adni egy másik függvénynek paraméterként:

def func_1():
    print('func_1: jelentkezem')
    return 42

def func_2(funcObj):
    print('func_2: felhívom a paraméterként kapott függvényt')
    x = funcObj()
    print('x:',x)

func_2(func_1)
# func_2: felhívom a paraméterként kapott függvényt
# func_1: jelentkezem
# x: 42

#############################

# Szimuláljunk egy rajzoló függvényt:

def plotter(xValues,func):
    for x in xValues:
        print(x, func(x))  # felrajzolás helyett csak kiírja

# Paraméterként a független változók sorozatát kapja és a függvényt, amely
# előállítja az y értéket

x_values = (1, 2, 3, 4)

def double(param):
    return 2 * param

def square(param):
    return param * param

plotter(x_values,double)
print('---------')
plotter(x_values,square)

# 1 2
# 2 4
# 3 6
# 4 8
# ---------
# 1 1
# 2 4
# 3 9
# 4 16

#############################

# Maga a rajzoló függvény is lehet paraméter. Legyen egy függvényünk, ami valami
# bonyolult algoritmus segítségével állít elő adatokat. Paraméterként kap egy
# rajzoló függvényt, amelyet felhív, hogy az elkészült adatokat ábrázolja.

def data_creator(plotFunc):
    data   = [(1,4),(2,6),(3,10)]  # ezt számolja ki
    plotFunc(data)

def plotter_1(xyPairs):
    for x in xyPairs:
        print(x[0], '*', x[1])

def plotter_2(xyPairs):
    for x in xyPairs:
        print(x[0], '->', x[1]

data_creator(plotter_1)
print('-----------')
data_creator(plotter_2)

# 1 * 4
# 2 * 6
# 3 * 10
# -----------
# 1 -> 4
# 2 -> 6
# 3 -> 10

# Az adatokat előállító data_creator függvénynek nem kell tudnia, hogy milyen rajzoló függvények
# léteznek; ha holnap valaki ír egy újabbat, akkor azt is át lehet neki adni, számára a plotter
# függvény fekete doboz.

# A paraméterként kapott függvény olyan, mint egy telefonszám. A fogadó függvény tudja, hogy amikor
# adatmegjelenítésre van szükség, akkor ezt a számot kell felhívnia és a telefonba csak be kell diktálnia
# az adatokat, a rajzolást a vonal másik végén majd elintézik. Nem véletlen, hogy ezeket a függvényeket
# callback függvényeknek hívják.

#############################

# Egy függvény paraméterként nem csak adatot tud kapni, hanem eljárást, működést, algoritmust is.
# Persze ugyanezt meg lehet valósítani "hagyományos" objektumokkal is: a plotter függvényt egy objektum
# hívja fel, az objektumot adjuk át paramézerként pl. a data_creator függvénynek. Ez egy
# kicsit bonyolultabb, az objektum csak segédváltozó, pusztán arra szolgál, hogy felhívja
# a kívánt függvényt. Amikor egy objektumnak egyetlen szolgáltatása (metódusa) van, akkor
# világosabb és egyszerűbb helyette egy függvényt alkalmazni.

#############################

# Függvényt paraméterként C-ben is tudunk átadni függvénypointer segítségével - csak annak a
# szintaktikája bonyolultabb.
