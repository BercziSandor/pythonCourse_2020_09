# Feltételvizsgálat eredménye --> logikai változó

# Nem szükséges if...else használata:

x = 10
if x > 5:
    y = True
else:
    y = False

# egyszerűbb és olvashatóbb így:

y = x > 5

##########################################

# Elemek logikai értelmezése

# Pythonban logikailag értelmezve hamisnak számít a nulla numerikus érték, minden
# üres iterálható sorozat és a None (ún. Falsy értékek); a többi igaznak számít.

lst = [0, 0.0, None, [], '', set(), dict()]
for e in lst:
    if e:
        print(e,' True')
    else:
        print(e,'False')

# 0 False
# 0.0 False
# None False
# [] False
#  False
# set() False
# {} False

lst = [-1, [2], '0', {1}, {'a': 1}]

for e in lst:
    if e:
        print(e,' True')
    else:
        print(e,'False')

# -1  True
# [2]  True
# 0  True   sztring!
# {1}  True
# {'a': 1}  True

# Ezért rá lehet kérdezni így is pl. arra, hogy üres-e egy lista:

lst = []
if not lst:
    print('üres')
else:
    print('nem üres')

# üres

# Ez tömör és elegáns, de jobban szeretem az explicit megfogalmazást:

if len(lst) == 0:
    print('üres')
else:
    print('nem üres')

# 1. Jobban olvasható.
# 2. Nem mosódhat egybe olyan esetekkel, amikor az lst változó pl. None vagy 0.

# Ha előfordulhat, hogy lst None, 0 vagy lista, akkor általában a különböző esetekben
# mást és mást kell csinálni.

lst = []
if lst is None:
    print('None, csinálok valamit')
elif lst == 0:
    print('Nulla, csinálok mást')
elif len(lst) == 0:
    print('Üres lista, csinálok megint mást')
else:
    print('Nem üres lista, csinálok végképpp mást')

# Üres lista, csinálok megint mást.

# Ha így írjuk:

if not lst:
    print('Csinálok valamit')
else:
    print('Nem üres lista, csinálok mást')

# akkor ugyanaz fog történni, ha lst None, 0 vagy üres lista - amennyiben tényleg
# ezt akartuk, akkor rendben van. Csak nem biztos, hogy ezt akartuk. Én már találkoztam
# olyan esettel, amikor így volt lekérdezve egy változó értéke, pedig meg kellett volna
# különböztetni a nulla esetét a None-tól, másfelé kellett volna ágaznia a programnak.

# Egyébként általában nem célszerű egy változó típusával jelezni a különböző eseteket;
# pl. egyik eset: nulla, másik eset: None. Nehezen olvasható, könnyen elrontható.

# Aki ilyen programszervezési alapelvekről akar olvasni egy keveset, annak ajánlom,
# hogy írjon egy programot. Csak ennyit kell tartalmaznia:

import this

# Lesz meglepi. :)

##########################################

# Logikai kifejezések kiértékelésének sorrendje, rövidre zárás
# (lazy evaluation, short-circuit evaluation)

# Hasonlóan más nyelvekhez, a kifejezések balról jobbra értékelődnek ki és
# a kiértékelődés befejeződik, amikor már biztosan nem változhat az eredmény.

# or műveletnél megáll a kiértékelés, ha egy tényező True:

x = 1
if x > 0 or 1 / 0:
    print('ezt megúsztam')

# ezt megúsztam

# and műveletnél megáll a kiértékelés, ha egy tényező False:

x = 1
if not (x > 10 and 1 / 0):
    print('ezt is megúsztam')

# ezt is megúsztam

##########################################

# Olyankor is hasznosítani lehet a rövidrezárós megoldást, ha az egyik feltételben
# lassú függvényt kell használnunk, pl. geokoordinátákat kell lekérdeznünk. Ilyenkor
# a lassú függvényt  hátrább rakjuk a sorban, így egyes esetekben meg sem kell ezeket
# hívni.

# result = quick_func() or slow_func()

# Amikor quick_func() True értéket ad vissza, akkor slow_func() hívására nem kerül sor.

##########################################

# Értékadásokban is szoktuk alkalmazni a rövidrezárós megoldást. Például egy függvényhívás
# szolgáltat egy SQL lekérdezést, de egyes esetekben a függvény nem tudja ezt meghatározni,
# ilyenkor None-t vagy üres sztringet ad vissza. Ebben az esetben egy default lekérdezést
# akarunk a változónkba tölteni.

# query = get_query() or 'SELECT * FROM minden'

##########################################
