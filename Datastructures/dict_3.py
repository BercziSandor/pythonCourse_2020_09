# Dictionary (szótár) 3.
# Szótárak egyesítése (merge); update metódus
# ChainMap objektum

# https://www.geeksforgeeks.org/chainmap-in-python/

# A gyakorlatban előforduló feladat: két (vagy több) szótárat egyesíteni akarunk úgy,
# hogy mindegyik kulcs szerepeljen az eredmény-szótárban. Egyező kulcsok esetén a másodiknak
# megadott szótár "győzzön", az ő értéke maradjon meg.

# Példa: Van egy default konfigurációs fájlom és egy másik, egy adott programhoz
# tartozó. Az utóbbinak felül kell írnia a default értékeket + át kell vennünk azon
# kulcs-érték párokat, amelyek csak a default szótárban szerepelnek.

# 1. módszer: update metódus.

dic_1 = {'A': 1, 'COMMON': 2}
dic_2 = {'C': 3, 'COMMON': 99}

dic_merged = {}
dic_merged.update(dic_1)
dic_merged.update(dic_2)

print(dic_merged) # {'A': 1, 'COMMON': 99, 'C': 3}

#######################################

# 2. módszer: a ** szótár-kibontás operátorral:

dic_merged = {**dic_1, **dic_2}
print(dic_merged) # {'A': 1, 'COMMON': 99, 'C': 3}

#######################################

# Ha nem akarunk létrehozni egy új szótárat, akkor használhatjuk a Chainmap objektumot:

from collections import ChainMap

chain = ChainMap(dic_2, dic_1) # fordított sorrendben vettük a szótárakat

print(chain) # ChainMap({'C': 3, 'COMMON': 99}, {'A': 1, 'COMMON': 2})

print(chain['COMMON']) # 99
print(chain['C'])      # 3
print(chain.get('nincsilyen')) # None

#######################################
