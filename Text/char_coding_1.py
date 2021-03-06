# Sztringek tárolása (ábrázolása) Pythonban
# Hexa konstansok megadása, hex() és ord() függvény
# Hexa numerikus konstansok
# Hexa konstansok írása sztringbe
# chr() függvény

# Pythonban minden sztring minden karaktere Unicode kódolással van tárolva. A Unicode-ban
# minden karakternek megfelel egy egész szám (kódpont); jelenleg kb. 1 millió különböző
# jelhez van rendelve Unicode kódérték, ezért 3 bájton ábrázolni lehetne az összeset.
# Pythonban 4 bájtos integer érték tárol egy-egy karaktert.

# Amikor a program karaktereket ír a terminálablakba, egy fájlba, egy adatbázisba, akkor
# rendszerint nem Unicode kódolást használ. Ugyanez persze a beolvasásra is igaz. A problémákat
# (nyilván) a konverziók okozzák.

#===========================================

# Az á betű kódja például hexa E1:

s = 'á'
print(s, ord(s), hex(ord(s))) # á 225 0xe1

# Hexa e1 = 14 * 16 + 1 = 225 decimális

# Az ű betűé hexa 171:

s = 'ű'
print(s, ord(s), hex(ord(s))) # ű 369 0x171

# Hexa 171 = 1 * 16 * 16 + 7 * 16 + 1 = 369

# Az ord() függvény egy karakter (Unicode) kódját adja meg decimális formában.

#===========================================

# Numerikus konstansként hexa értéket úgy tudunk megadni, hogy az elejére 0x-et írunk.
# A betűk lehetnek kisbetűk vagy nagybetűk:

print(0XE, 0xe, 0x11, 0x100, 0x1000) # 14 14 17 256 4096

#===========================================

# Sztringbe is szoktunk hexa konstansokat írni - erre olyankor van szükségünk, amikor
# nincs a klaviatúrán a megjeleníteni kívánt karakter.

# Egy bájtos karaktert úgy tudunk a sztringbe írni, hogy \x után leírjuk a két hexa karaktert:

s = '\xe1'
print(s)  # á

# A hexa karakter lehet nagybetű is:

print('\xE1')  # á

# Az x-nek kisbetűnek kell lennie, a \X-nek nincs semmi speciális jelentése:

print('\Xe1')  # \Xe1

# Persze a sztring lehet hosszabb is:

print('\xe1s') # ás

# A \x utáni két karakternek hexadecimális karakternek kell lennie. Ezek hibásak:

s = '\xem' # m nem hexa karakter
s = '\x1'  # hiányzik a második hexa karakter

# A második példában '\x01'-et kell írnunk, ha 1 értékű bájtot szeretnénk megadni (ami
# egyébként egy vezérlő karakter).

# Másik módszer: numerikus konstanst a chr() függvény segítségével alakítunk egy
# karakteres sztringgé:

s = chr(0xe1)
print(s)  # á

# Így csak egyetlen karaktert tudunk megadni.

################################

# Két bájtos értéket úgy tudunk a sztringbe írni, hogy \u után leírjuk a négy hexa karaktert:

s = '\u0171'
print(s)  # ű

# A \u utáni két karakternek hexadecimális karakternek kell lennie. Ezek hibásak:

s = '\u017m' # m nem hexa karakter
s = '\017'   # hiányzik a negyedik hexa karakter

# Az u betűnek kicsinek kell lennie - rögtön látni fogjuk, hogy a nagy U-nak más a jelentése.

# Másik módszer: numerikus konstanst a chr() függvény segítségével alakítunk sztringgé:

s = chr(0x171)
print(s)  # ű

################################

# Négy bájtos értéket úgy tudunk a sztringbe írni, hogy \U után leírjuk a nyolc hexa karaktert:

s = '\U000000e1' # nem sok értelme van, de működik
print(s)  # á

s = '\U00000171' # ez hasonlóan
print(s)  # ű

################################

# \N-t követően kapcsos zárójelek között beírhatjuk a karakter szabványos Unicode megnevezését:

s = '\N{LATIN SMALL LETTER A WITH ACUTE}'
print(s, ord(s), hex(ord(s)))  # á 225 0xe1

# Ezt a megnevezést pl. itt találhatjuk meg:

https://www.fileformat.info/info/unicode/char/00e1/index.htm

################################

# Ha a Python szkriptet nem UTF-8 kódolással mentjük el, akkor
# az első sorban egy kommentben meg kell adni a kódolást:

# coding=ISO-8859-2

################################

# Az ékezetes karakterek a Python szkript fájlban valamilyen kódolással vannak elmentve,
# pl. UTF-8-ban. Amikor a Python értelmező beolvassa a fájlt, akkor a sztringek
# karaktereit átalakítja Unicode kódolásúra.

# Legyen pl. egy ő betű az UTF-8 kódolású szkript fájlban.

#       ő                        ő
#   A fájlban               A Python kódban
#     2 bájt     ===>    1 négy bájtos integer
#   0xc5 0x91                  0x151
#     UTF-8                   Unicode

# Ha ugyanez a forrásfájl ISO-8859-2 kódolással van elmentve:

#       ő                        ő
#   A fájlban               A Python kódban
#     1 bájt     ===>    1 négy bájtos integer
#      0xf5                    0x151
#   ISO-8859-2                Unicode

################################
