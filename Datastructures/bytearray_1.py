# A bytearray adattípus

# http://www.trytoprogram.com/python-programming/python-built-in-functions/bytearray/
# https://www.journaldev.com/22703/python-bytearray
# https://www.geeksforgeeks.org/python-bytearray-function/
# https://www.w3resource.com/python/python-bytes.php
# https://docs.python.org/3.8/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview
# https://docs.python.org/3.8/howto/unicode.html
# https://stackoverflow.com/questions/9099145/where-are-python-bytearrays-used
# https://stackoverflow.com/questions/22192196/use-cases-for-bytearray
# https://stackoverflow.com/questions/38564456/how-to-replace-invalid-unicode-characters-in-a-string-in-python

# A bytearray adattípus 1 bájtos számok vátoztatható sorozata; azaz minden eleme egy 0-255
# tartományba eső szám.

#############################

# A bytearray() konstruktor segítségével tudunk létrehozni ilyen típusú objektumot.

# 1. módszer: sztringből.

x = bytearray('abc','UTF-8')
print(x) # bytearray(b'abc')

# A második paraméter kötelező (encoding) - enélkül nem lehet kitalálni, hogy a sztringnek
# milyen kódolású ábrázolását akarjuk előállítani. Vegyünk például egy á betűt.

x = bytearray('á','UTF-8')
print(x) # bytearray(b'\xc3\xa1')

# Az á betű UTF-8 kódja két bájtos, egy C3 és egy A1 értékű bájtból áll.
# Az UTF-8 az ascii karaktereket 1 bájton ábrázolja, itt megegyezik az ascii-val; a többi
# szimbólumot 1, 2, 3 vagy 4 bájton. A magyar ékezetes karakterek 2 bájtosak.

# Viszont:

x = bytearray('á','ISO-8859-2')
print(x) # bytearray(b'\xe1')

# Az ISO-8859-2 (Kelet-Európai) kódkészletben az á betű kódja egy E1 értékű bájt.

#----------------------------

# 2. módszer: számok iterálható sorozatából.

x = bytearray([97, 98, 99])
print(x) # bytearray(b'abc')

# A számoknak 0 és 255 közé kell esniük:

x = bytearray([256]) # ValueError

#----------------------------

# 3. módszer: A bytearray() konstruktornak egy számot adunk, ekkor ennyi darab 0 értékű
# bájtból álló sorozat keletkezik:

x = bytearray(3)
print(x) # bytearray(b'\x00\x00\x00')

# \x00: két hexadecimális 0, azaz egy 0 értékű bájt. Azért kell így megjeleníteni,
# mert nem ábrázolható karakter.

#############################

# A bytearray típusú objektum mutábilis, változtatható:

x = bytearray([97, 98])
x[0] = 98
print(x) # bytearray(b'bb')

x.append(97)
print(x) # bytearray(b'bba')
x.append(ord('a'))
print(x) # bytearray(b'bbaa')
del(x[-1])
print(x) # bytearray(b'bba')

#############################

# bytearray objektum átalakítása sztringgé: decode() metódussal.

x = bytearray(b'\xc3\xa1')    # á betű utf-8 kódja
s = x.decode('UTF-8')
print(s, type(s))  # á <class 'str'>

# UTF-8 a default, nem kell kiírni:

s = x.decode()
print(s, type(s))  # á <class 'str'>

#----------------------------

# A sztringben egyetlen szám van:

nums = [ord(e) for e in s]
print('len:', len(nums), nums) # len: 1 [225]

# 225 (hexa E1) az á betű Unicode kódja.

# A bytearray objektumban két darab szám volt:

nums = [e for e in x]
print('len:', len(nums), nums) # len: 2 [195, 161]

# Az á betű UTF-8 kódja C3 A1, decimálisan 195 161.

# A Unicode sztringben négy bájtos számok vannak, egy-egy elemnek lehet
# az értéke 255-nél sokkal nagyobb is. Nézzünk meg például egy ű betűt:

s = 'ű'
nums = [ord(e) for e in s]
print('len:', len(nums), nums) # len: 1 [369]

#----------------------------

# Természetesen más kódkészletettel is működik:

x = bytearray(b'\xe1')
s = x.decode('ISO-8859-2')
print(s, type(s))  # á <class 'str'>

#############################

# bytearray átalakítása számok listájává:

x = bytearray('áa','UTF-8')
lst = list(x)
print(lst) # [195, 161, 97]

# Ha hexadecimálisan akarjuk látni:

lst_hex = [hex(e) for e in lst]
print(lst_hex)  # ['0xc3', '0xa1', '0x61']

# Megjelenítésnél 0x utáni két hexa számjegy: 1 bájt.

#############################

# Hibakezelés

x = bytearray('bácsi', 'ISO-8859-2')
print(x) # bytearray(b'b\xe1csi')

# Tévesen UTF-8 kódolásúnak hisszük, amikor megpróbáljuk visszaalakítani:

s = x.decode('UTF-8') # UnicodeDecodeError

# Az errors paraméternek 'strict' a defaultja, tehát ekkor is ugyanaz történik:

s = x.decode('UTF-8', errors='strict')  # UnicodeDecodeError

# Beállíthatjuk úgy is, hogy ignorálja azon bájtokat, amelyeket nem tud konvertálni:

s = x.decode('UTF-8', errors='ignore')
print(s)  # bcsi

# Azt is előírhatjuk, hogy helyettesítse a hibás karaktereket:

s = x.decode('UTF-8', errors='replace')
print(s)  # b?csi

# Úgy tűnik, hogy egy kérdőjel került a problémás helyre, de nem:

s2 = s.replace('\ufffd', '!*!')
print(s2) # b!*!csi

# Egy FFFD értékű REPLACEMENT CHARACTER került bele a sztringbe. HTML-ben megjelenítve
# ez egy sötét, hegyére állított négyzetbe írt kérdőjel. Mint látható, lecserélhetjük
# valami feltűnőbb jelre, ha akarjuk.

#############################
