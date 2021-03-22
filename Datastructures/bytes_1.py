# A bytes adattípus
# bytes és sztring közötti konverzió
# Unicode és UTF-8 megjelenítése
# ISO-8859-2 kódolás
# bytes() konstruktor
# encode(), decode() metódusok
# ord() függvény
# decode() hibakezelése, az errors paraméter:
#  * strict
#  * ignore
#  * replace
#  * Unicode replacement character
# megvalósuló hibás átkódolások

# http://www.trytoprogram.com/python-programming/python-built-in-functions/bytes/
# https://www.journaldev.com/22747/python-bytes
# https://www.geeksforgeeks.org/byte-objects-vs-string-python/
# https://www.w3resource.com/python/python-bytes.php
# https://docs.python.org/3.8/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview
# https://docs.python.org/3.8/howto/unicode.html
# https://stackoverflow.com/questions/38564456/how-to-replace-invalid-unicode-characters-in-a-string-in-python

# A bytes adattípus 1 bájtos számok immutábilis sorozata; azaz minden eleme egy 0-255
# tartományba eső szám.

# Sztring formátumú konstanssal definiálhatunk egy bytes típusú elemet, feltéve, hogy
# csak ascii karakterek vannak benne. Ehhez egy b betűt kell írnunk a sztring-konstans elé:

x = b'abc'
print(x, type(x)) # b'abc' <class 'bytes'>

# Ha nem ascii karakterek is vannak a sztringben, akkor hibajelzést kapunk:

x = b'ábc' # SyntaxError

# Azért jön a hibajelzés, mert nem mondtuk meg, hogy az á betűnek milyen kódolására
# gondoltunk. Ezen a helyen nem is tudjuk megmondani.

# Persze hexadecimális konstansként beleírhatjuk az ékezetes betűt:

x = b'\xe1bc'
print(x, type(x)) # b'\xe1bc' <class 'bytes'>

#############################

# A bytes() konstruktor segítségével is létre tudunk hozni bytes típusú objektumot.

# 1. módszer: sztringből.

x = bytes('abc','UTF-8')
print(x, type(x)) # b'abc' <class 'bytes'>

# A második paraméter kötelező (encoding) - enélkül nem lehet kitalálni, hogy a sztringnek
# milyen kódolású ábrázolását akarjuk előállítani. Vegyünk például egy á betűt.

x = bytes('á','UTF-8')
print(x) # b'\xc3\xa1'

# Az á betű UTF-8 kódja két bájtos, egy C3 és egy A1 értékű bájtból áll.
# Az UTF-8 az ascii karaktereket 1 bájton ábrázolja, itt megegyezik az ascii-val; a többi
# szimbólumot 1, 2, 3 vagy 4 bájton. A magyar ékezetes karakterek 2 bájtosak.

# Viszont:

x = bytes('á','ISO-8859-2')
print(x)  # b'\xe1'

# Az ISO-8859-2 (Kelet-Európai) kódkészletben az á betű kódja egy E1 értékű bájt.

#----------------------------

# 2. módszer: számok iterálható sorozatából.

x = bytes([97, 98, 99]) # ('abc' - az 'a' betű ascii kóódja 97.)
print(x, type(x)) # b'abc' <class 'bytes'>

# A számoknak 0 és 255 közé kell esniük:

x = bytes([256]) # ValueError

#----------------------------

# 3. módszer: A bytes() konstruktornak egy számot adunk, ekkor ennyi darab 0 értékű
# bájtból álló sorozat keletkezik:

x = bytes(3)
print(x, type(x)) # b'\x00\x00\x00' <class 'bytes'>

# \x00: két hexadecimális 0, azaz egy 0 értékű bájt. Azért kell így megjeleníteni,
# mert nem ábrázolható karakter.

#############################

# Sztringből az encode() metódus segítségével is tudunk bytes objektumot csinálni:

x = 'á'.encode('UTF-8')
print(x) # b'\xc3\xa1'

# Az UTF-8 kódkészlet a default, nem kötelező kiírni:

x = 'á'.encode()
print(x) # b'\xc3\xa1'

# Természetesen más kódkészletet is megadhatunk:

x = 'á'.encode('ISO-8859-2')
print(x)  # b'\xe1'

#############################

# A bytes típusú objektum immutábilis:

x = bytes([97, 98])
x[0] = 98  # TypeError

#############################

# bytes objektum átalakítása sztringgé: decode() metódussal.

x = b'\xc3\xa1'    # á betű utf-8 kódja
s = x.decode('UTF-8')
print(s, type(s))  # á <class 'str'>

# UTF-8 itt is default, nem kell kiírni:

s = x.decode()
print(s, type(s))  # á <class 'str'>

#----------------------------

s = 'á' # a sztringben karakter, azaz egyetlen szám van

nums = [ord(e) for e in s]
print('len:', len(nums), nums) # len: 1 [225]

# ord(x) az x karakter Unicode kódja.
# 225 (hexa E1) az á betű Unicode kódja.

x = b'\xc3\xa1'    # á betű utf-8 kódja
# A bytes objektumban két darab szám van:

nums = [e for e in x]
print('len:', len(nums), nums) # len: 2 [195, 161]

# Az á betű UTF-8 kódja hexa c3 a1, decimálisan 195 161.

# A Unicode sztringben négy bájtos számok vannak, egy-egy elemnek lehet
# az értéke 255-nél sokkal nagyobb is. Nézzünk meg például egy ű betűt:

s = 'ű'
nums = [ord(e) for e in s]
print('len:', len(nums), nums) # len: 1 [369]

#----------------------------

#  decode() természetesen más kódkészletettel is működik:

x = b'\xe1'
s = x.decode('ISO-8859-2')
print(s, type(s))  # á <class 'str'>

#############################

# bytes átalakítása számok listájává:

x = 'áa'.encode()
lst = list(x)
print(lst) # [195, 161, 97]

# Ha hexadecimálisan akarjuk látni:

lst_hex = [hex(e) for e in lst]
print(lst_hex)  # ['0xc3', '0xa1', '0x61']

# Megjelenítésnél 0x utáni két hexa számjegy: 1 bájt.

#############################

# Hibakezelés

x = 'bácsi'.encode('ISO-8859-2')
print(x)  # b'b\xe1csi'

# Tévesen UTF-8 kódolásúnak hisszük, amikor megpróbáljuk visszaalakítani:

x = b'b\xe1csi'
s = x.decode('UTF-8') # UnicodeDecodeError

# Az errors paraméternek 'strict' a defaultja, tehát ekkor is ugyanaz történik:

s = x.decode('UTF-8', errors='strict')  # UnicodeDecodeError

# Miért jön a hibajelzés? A bájtsorozat első bájtja hexa e1, a második (a c betű
# kódja) hexa 63:

print(hex(ord('c'))) # 0x63

# és ezek együtt nem szerepelnek az UTF-8 karakterkombinációk között. Ha erről meg
# akarunk győződni, akkor írjuk be a keresőbe ezt:

# utf-8 hexa e1

# erre megkapjuk többek közt ezt az oldalt:

# https://www.utf8-chartable.de/unicode-utf8-table.pl?start=8064&number=128&names=-

# és itt láthatjuk, hogy valóban nincs olyan UTF-8 kód, amelynek az elején \xe1\x63 állna.

#--------------------------

# Beállíthatjuk úgy is, hogy decode() ignorálja azon bájtokat, amelyeket nem tud konvertálni:

x = b'b\xe1csi'
s = x.decode('UTF-8', errors='ignore')
print(s)  # bcsi

# Amikor a neten olyan szöveggel találkozunk,melyből hiányzanak az ékezetes betűk,
# akkor az így keletkezett.

#--------------------------

# Azt is előírhatjuk, hogy decode() helyettesítse valamivel a hibás karaktereket:

x = b'b\xe1csi'
s = x.decode('UTF-8', errors='replace')
print(s)  # b?csi

# Úgy tűnik, hogy egy kérdőjel került a problémás helyre, de gyanakszunk, hogy csak a
# terminál-ablak nem tudta megjeleníteni azt, ami valójában ott van és ő cserélte le
# kérdőjelre. Írassuk ki egyenként a sztring karaktereinek hexa kódját:

for e in s:
    print(hex(ord(e)), end=' ')
print()

# 0x62 0xfffd 0x63 0x73 0x69
# 'b'         'c'  's'  'i'

# Egy fffd értékű került bele a sztringbe. Ha tudni akarjuk, mi ez, akkor írjuk
# be a keresőbe, hogy:

# unicode fffd

# és többek közt ezt az oldalt fogjuk kapni:

# https://www.fileformat.info/info/unicode/char/fffd/index.htm

# Tehát ez egy REPLACEMENT CHARACTER. HTML-ben megjelenítve ez egy sötét, hegyére
# állított négyzetbe írt kérdőjel. Ezzel is találkozhattunk már weboldalakon és
# email-ekben és nem szoktunk örülni neki.

# Lecserélhetjük persze egy következő lépésben valami feltűnőbb jelre az átkódolhatatlan
# karaktereket, ha akarjuk:

x = b'b\xe1csi'
s = x.decode('UTF-8', errors='replace')
s2 = s.replace('\ufffd', '!*!')
print(s2) # b!*!csi

#############################

# Megvalósuló hibás átkódolások.

# Előfordulnak szituációk, amikor hibásan adunk meg kódtáblát és a program nem képes
# ezt észrevenni. Egy gyakori eset: UTF-8 kódolású szövegről azt hisszük, hogy valamilyen
# egybájtos kódolásúak. A legtöbb bájt jelent valamit az 1 bájtos kódtáblákban, ezért
# nem jelez a program hibát.

#############################
