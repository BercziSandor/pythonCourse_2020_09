# numpy aggregátor műveletek (sum...) és a kitöltetlenség
# NaN és None kezelése
# NaN-safe numpy műveletek

import numpy as np

# Először a sum függvényt vizsgáljuk.

arr = np.array([10, 20, np.NaN])

print(sum(arr))       # nan - volt legalább egy NaN --> az eredmény is NaN
print(np.sum(arr))    # nan
print(np.nansum(arr)) # 30  - csak a kitöltött elemeket veszi figyelembe

############################

# A None hibát okoz minden esetben --> None-ra szűrnünk kell a művelet előtt.
# Nincs None-safe művelet.

arr = np.array([10, 20, None])

print(sum(arr))       # hiba
print(np.sum(arr))    # hiba
print(np.nansum(arr)) # hiba

# Persze a NaN-ra is érdemes lehet szűrni, mert lehet, hogy valahány százaléknyi NaN-tól
# kezdve nem értelmezhető az eredmény. Ha egy 1000 elemű listából 998 kitöltetlen (NaN),
# akkor nem nagyon van értelme statisztikát csinálni.

#############################

# Üres listánál nulla a sum eredménye, ami szerintem nem a leglogikusabb megoldás,
# inkább definiálatlannak (None vagy NaN) kellene lennie.

arr = np.array([])

print(sum(arr))       # 0
print(np.sum(arr))    # 0.0
print(np.nansum(arr)) # 0.0

#############################

# Néhány eset, amely nulla összeget produkál:

arr = np.array([10, 9, -9, -10])
print(np.nansum(arr))  # 0

arr = np.array([0, 0, 0, 0])
print(np.nansum(arr))  # 0

arr = np.array([np.NaN, np.NaN, np.NaN, np.NaN])
print(np.nansum(arr))  # 0.0

arr = np.array([np.NaN, 0, 0, np.NaN])
print(np.nansum(arr))  # 0.0

arr = np.array([])
print(np.nansum(arr))  # 0.0

#############################

# A mean függvény:

arr = np.array([10, 20, np.NaN])

print(np.mean(arr))    # nan - volt legalább egy NaN --> az eredmény is NaN
print(np.nanmean(arr)) # 15.0 - a kitöltetlen elemek mintha nem is léteznének

# Látszik, hogy a kitöltetlenséget miért nem célszerű nullával jelezni (azaz a
# kitöltetlen elemeket adott ponton csendesen nullává alakítani):

arr = np.array([10, 20, 0]) # NaN-ból nullát csináltunk

print(np.mean(arr))    # 10.0 (nem NaN)
print(np.nanmean(arr)) # 10.0 (nem 15.0)

# A nullává konvertálás pl. Excel-táblából vagy CSV fájlból való importálásnál történhet
# meg. Ebben a pillanatban elveszítettük azt az információt, hogy mekkora az adatok
# kitöltöttsége.

#############################

# Alacsony kitöltöttségű sorozatnak is lehet az átlagát venni, csak ezt akkor megfelelően
# értelmezni (kommentálni) kell.

arr = np.array([20, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 10])

print(np.nanmean(arr)) # 15.0

# NEM igaz az alábbi kijelentés (csak politikusok számára ajánlott):

# A 11 elemű minta átlaga 15.
# Másképpen: 11 megkérdezett által adott értékelés átlaga 15.

# Helyesen:

# A 11 elemű minta 2 eleme volt kitöltve, ezek átlaga 15.
# Másképpen: 11 megkérdezettből 2 válaszolt, az ő általuk adott értékelés átlaga 15.

# Sokszor érdemes megnézni, hogy az adataok hányad része van kitöltve.

if len(arr) == 0:
    nonempty_perc = 0
else:
    nonempty_perc = len(arr[np.isnan(arr) == False]) / len(arr)

print(nonempty_perc) # 0.1818

#############################
