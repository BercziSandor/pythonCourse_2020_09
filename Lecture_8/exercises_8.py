# 1.)

# Adott egy feladat megoldása:

import numpy as np

a1 = np.array([10, 20, 30, 40])
a2 = np.array([90, 40, 70, 80])

lst = []
for i, x in enumerate(a1):
    if a2[i] == 2 * x:
        lst.append(x)

a = np.array(lst)

# Egy kollégánk, akit különösen utálunk, előáll büszkén ezzel az egyszerűsített
# megoldással:

a1 = np.array([10, 20, 30, 40])
a2 = np.array([90, 40, 70, 80])

a = np.array([x for i, x in enumerate(a1) if a2[i] == 2 * x])

# Rontsuk el az örömét! Állítsuk elő az a tömböt még egyszerűbben.

############################################

# 2.)

# Be kell olvasni egy szövegfájl sorait, el kell távolítani a sorvégjeleket és
# minden sor elejére oda kell írni a sorszámot, 1-gyel kezdve. Az így keletkezett
# sztringeket el kell helyezni egy listában.

# A. Listcomp nélkül.

# B. Listcomp segítségével.

############################################

# 3.)

# Két szövegfájl sorait (sorvégjel nélkül) kell '|' jellel elválasztva összefűzni
# és egy listában elhelyezni. Ha az egyik fájlban több sor van, akkor ezeket a többlet
# sorokat nem kell figyelembe venni. Listcomp-pal oldjuk meg a feladatot.

############################################

# 4.)

# Egy szövegfájlban ; karakterrel delimitált sorok vannak, pl.:

Budapest ; 10
 Debrecen; 20
Budapest; 30
Szolnok; 40

# A fájlban lehetnek üres sorok is. Létre kell hozni egy szótárat, amelyben az első
# mezőben található szavak a kulcsok, a hozzájuk tartozó számok összege az értékek.
# Az első mezőben lehetnek a szó előtt és után fehér karakterek, ezeket el kell távolítani.
# A fentebbi adatokkal a szótár:

# {'Budapest': 40, Debrecen: 20, Szolnok: 40}

############################################

# 5.)

# Egy két dimenziós tömbben  numerikus értékek vannak:

import numpy as np

arr = np.array([
[10, 20, 30, 7],
[12, 9, 17, 22],
[4, 8, 14, 11]
])

# egy listában pedig az egyes sorokhoz tartozó címkék:

names = ['Budapest', 'Debrecen', 'Szolnok']

# Létre kell hozni egy szótárt, amelyben csak azon címkék szerepelnek kulcsként,
# amelyekhez tartozó sorban van 15-nél nagyobb elem; az értékek pedig ezen elemek listája:

# {'Budapest': [20, 30], 'Debrecen': [17, 22]}

############################################
