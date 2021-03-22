# context manager bemutatása
# getattr(), callable() függvények

# Gyakran előforduló feladat, hogy egy erőforrást meg kell szerezni, aztán bizonyos
# műveletek elvégzése után fel kell szabadítani.

# * Megnyitunk egy fájlt, írunk/olvasunk, bezárjuk a fájlt.
# * Megnyitunk egy fájlt, egy pufferbe írunk, időnként a puffer tartalmát kiírjuk
#   a fájlba; lezárás előtt kiírjuk a fájl tartalmát, majd bezárjuk. A puffer két
#   szempontból lehet hasznos:
#     + Gyorsítás: ritkábban, nagyobb blokkokban írunk a lemezre.
#     + Tranzakció (mint egy adatbázisnál): amíg a lemezre írás nem történt meg, addig
#       meggondolhatjuk magunkat, törölhetjük a puffer tartalmát (rollback-szerűség).
#   Viszont: gondoskodni kell róla, hogy a fájl bezárásakor vagy írjuk ki a puffert
#   (commit), vagy, hiba esetén NE írjuk ki. Mindennek egy lezáró függvényben kell
#   megtörténnie.
#
# * Megnyitunk egy adatbázist, írunk bele, majd bezárjuk. Bezárás előtt a megkezdett
#   tranzakciókat vagy véglegesítjük, vagy visszagörgetjük.
# * Zárolunk egy vezérlési szálat (thread), aztán valamikor felszabadítjuk.
# * Megnyitunk egy hálózati kapcsolatot, majd használat után bezárjuk.

# A lezárásról könnyű megfeledkezni, különösen, ha kivétel is keletkezhet a végrehajtás
# közben.

############################################################

# Első módszer ennek az elkerülésére a try...finally használata.

try:
    print('megnyitom, amire szükségem van')
    print('csinálok valamit')
    raise Exception('váratlan kivétel')
except Exception as e:
    print('hopp, elkaptam')
finally:
    print('most pedig bezárom')

# megnyitom, amire szükségem van
# csinálok valamit
# hopp, elkaptam
# most pedig bezárom

# Ez akkor is működik, ha nincs except ág. Ilyenkor valahol a hívó kapja el a kivételt,
# de a lezárás itt megtörténik.

############################################################

# Elegánsabb és egyszerűbb a with utasítás használata. Fájl megnyitásán szemléltetjük.

with open('yyy.txt','r') as file_obj:
    line = file_obj.readline()

print(file_obj.closed) # True

# Nem zártuk be a fájlt, magától bezáródott.

# Megnyithatjuk a with blokk előtt is a fájlt (a valóságban persze hibakezelést is
# beleépítve):

file_obj = open('yyy.txt','r')
with file_obj:
    line = file_obj.readline()

print(file_obj.closed) # True

A fájl akkor is bezáródik, ha a with blokkban kivétel keletkezik:

file_obj = open('yyy.txt','r')

try:
    with file_obj:
        line = file_obj.readline()
        raise Exception  # hibát szimulálunk
except Exception:
    pass

print(file_obj.closed) # True

############################################################

# Látni fogjuk, hogy a with utasítás akkor használható, ha az illető objektumnak van
# __enter__ és __exit__ metódusa. Könnyen leellenőrizhetjük, hogy a fájl-objektumnak
# tényleg van ilyenje:

file_obj = open('yyy.txt','r')
d = dir(file_obj)
for f in ('__enter__', '__exit__'):
    if f in d:
        att = getattr(file_obj, f)
        if callable(att):
            print(f, 'létezik és hívható')

# __enter__ létezik és hívható
# __exit__ létezik és hívható

############################################################
