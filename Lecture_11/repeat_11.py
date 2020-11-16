# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# 1.)

def func(param):
    if param > 10:
        raise ValueError('dobok egy kivételt')

    print('nem dobok')

for x in (5, 15):
    try:
        func(x)
    except Exception:
        print('elkaptam egy kivételt')
    finally:
        print('eléneklem a finálét')

######################################

# 2.)

class MyException_1(Exception): pass

class MyException_2(MyException_1): pass

def func():
    raise MyException_1('dobok egy kivételt')

try:
    func()
except MyException_2:
    print('elkaptam egy kivételt')
finally:
    print('itt a vége')

######################################

# 3.)

companies = {
'CoolCompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
'CheapCompany' : {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}}

bad_comps = [x for x in companies if any(y<9 for y in companies[x].values())]

# Fogalmazzuk meg szóban is, mit csinál!

######################################

# 4.)

lst = [-1, None, 10, 100]
print(max(lst))

######################################

# 5.)

# A.

lst = [-1, None, 10, 100]

g = [ x for x in lst if x ]
print(max(g))

# B.

# Adjunk meg olyan adatokat, amelyekkel rossz eredményt ad.

# C.

# Javítsuk ki.

######################################

# 6.)

def func_1(param):
    for e in param:
        yield(e if e < 20 else 20)

def func_2(param):
    for e in param:
        if e % 3 == 0:
            yield -e
        else:
            yield e

lst = [18, 20, 21]

# A.

g_1 = func_1(lst)
g_2 = func_2(g_1)

for i in g_2:
    print(i)

# B.
g_1 = func_2(lst)
g_2 = func_1(g_1)

for i in g_2:
    print(i)

######################################
