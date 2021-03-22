# A Python program kapcsolata a környezetével.
# Környezeti változók, os.environ objektum, SET Windows parancs

# https://www.geeksforgeeks.org/python-os-environ-object/
# https://www.nylas.com/blog/making-use-of-environment-variables-in-python/

#########################################

# Amikor az operációs rendszer elindít egy programot, egy csomó információt átad
# neki a környezetéről úgynevezett környezeti változókban (environment variables).
# Egy Python program az os modul environ nevű objektumában tárolja ezeket. Ez egy
# dict-re hasonlító objektum, a megszokott módokon tudunk adatokat olvasni belőle:

from os import environ

print(environ['OS'])      # Windows_NT
print(environ.get('OS'))  # Windows_NT
print('OS' in environ)    # True
print(environ.get('xx'))  # None
print(environ.get('xx','sajnos, ilyen nincs')) # sajnos, ilyen nincs

#########################################

# Egy program indítása előtt be tudunk állítani környezeti változókat, Linux alatt
# export, Windows alatt SET paranccsal.

# SET valami=xyz
# python.exe test.py

# test.py tartalma:

from os import environ

print(environ['valami']) # xyz

# VIGYÁZAT! A SET parancsnál az egyenlőségjel egyik oldalára se tegyünk szóközt, mert
# az belekerül a változó nevébe, ill. értékébe.

# Természetesen programból (pl. egy C programból) is indítani tudunk Python programot és
# ott is be tudjuk állítani a megfelelő környezeti változókat.

#########################################

# A környezeti változók mindenhol elérhető globális változók. Néhány célszerű felhasználási
# területük:

# 1.)

# Működési fázis definiálása (fejlesztés, teszt, produkció). Ettől függően a program
# például máshonnan olvas bizonyos adatokat, másképpen állít be felhasználói jogosultságokat,
# mást és máshová jegyez fel logfájlokba.

# A főprogramban (vagy a csomag __init__.py moduljában:

from os import environ

my_proj_glob = {}
my_proj_glob['phase'] = environ['MY_PROJ_PHASE'].lower()

#...

def my_proj_dev_phase():
    return my_proj_glob['phase'] == 'dev'

# Bármelyik program modulban:

if my_proj_dev_phase():
    print('logfájlba írok')

# A programot indító szkriptben:

# SET MY_PROJ_PHASE=Dev

# Egy apró trükk: ahol kiolvassuk a környezeti változó értékét, ott adott írásmódúra
# (itt kisbetűssé) alakítjuk. Sok bosszúságtól megvéd!

#++++++++++++++++++++++++++++++++++++++++

# 2.)

# Biztonság növelése. Egyes kényes információkat, pl. egy titkosító kulcsot elhelyezhetünk
# környezeti változókban - ahelyett, hogy a program szövegébe írnánk ezeket. Ha a támadónak
# sikerül is megszereznie a szerver oldali program forrását, a titkosító kulcs ezáltal
# nem kerül a kezébe, ehhez az indító programot is fel kell törnie.

#++++++++++++++++++++++++++++++++++++++++

# 3.)

# Számos esetben függenek fájlelérési útvonalak attól, hogy milyen nevű felhasználó indítja
# a programot, ezt pedig a USERNAME környezeti változóban találja meg a program.

#++++++++++++++++++++++++++++++++++++++++

# 4.)

# Ha a program az operációs rendszer temp könyvtárát akarja használni, ennek a helyét
# a TEMP vagy a TMP környezeti változóban találja meg.

#########################################
