# Paraméterek változtatása

def func(param):
    param += 10
    print('param in func:', param)

x = 100
print('x before func:', x)
func(x)
print('x after func:', x)

# x before func: 100
# param in func: 110
# x after func: 100

# x NEM változott meg a külső programrészben. A függvényhívásnál a változó másolatát
# helyezi el a futtató rendszer a stack-en és adja át a függvénynek. Valahogy így
# lehet szemléltetni:

x = 100
print('x before func:', x)
x_temp = x   # egy másik változó is mutat a 100-as értékre
func(x_temp)
del(x_temp)
print('x after func:', x)

# Mi a helyzet, ha a paraméter nem immutábilis, hanem például egy lista?

def func(param):
    param += [10]
    print('param in func:', param)

x = [100]
print('x before func:', x)
func(x)
print('x after func:', x)

# x before func: [100]
# param in func: [100, 10]
# x after func: [100, 10]

####################################

# Mi történik, ha a függvényben nem a += műveletet használjuk?

def func(param):
    param = param + [10]  # !!!
    print('param in func:', param)

x = [100]
print('x before func:', x)
func(x)
print('x after func:', x)

# x before func: [100]
# param in func: [100, 10]
# x after func: [100]  !!!!

# A külső programrészben NEM változott a lista. Azért, mert ez az utasítás:

#   param = param + [10]

# egy új memóriacímre helyezte a listát. Írassuk ki a memóriacímeket, az talán
# segít a megértésben:

def func(param):
    print('param id in func 1:', id(param))
    param = param + [10]
    print('param id in func 2:', id(param))

x = [100]
print('x id before func:', id(x))
func(x)
print('x id after func:', id(x))

# x id before func: 6219816
# param id in func 1: 6219816
# param id in func 2: 6276640
# x id after func: 6219816

# A függvény megkapta az x változó címének a másolatát param névvel. Belül létrehozott
# egy új listát, új címen. A param változó most egy új címre mutat.
# A külső x változó ettől még mindig az eredeti listára, az eredeti memóriacímre fog mutatni.

# Tanulság: ha egy nem immutábilis adatszerkezetet, pl. egy listát adunk át paraméterként, attól
# az még nem lesz változó paraméter, értékparaméter marad - kivéve egyes eseteket (a += esetét).

####################################

# Hogyan tudunk változó paramétereket csinálni?

# Be kell csomagolni őket egy változtatható adatszerkezetbe. Ez lehet pl. lista:

def func(paramLst):
    paramLst[0] = 99
    paramLst[1] = [10, 20]

x = [100, [200]]
print('x before func:', x) # x before func: [100, [200]]
func(x)
print('x after func:', x)  # x after func: [99, [10, 20]]

# Persze ez nem a legjobb megoldás, tudni kell, hogy melyik pozíció mit jelent.
# dict SOKKAL jobb:

def func(paramDict):
    paramDict['my_number'] = 99
    paramDict['my_list'] = [10, 20]

x = {'my_number': 100, 'my_list': [200]}
func(x)
print(x) # {'my_number': 99, 'my_list': [10, 20]}

####################################
