# A Python program kapcsolata a környezetével.
# sys.argv: indítási paraméterek (command line parameters) elérése

# A modul indítási paramétereit a sys modul argv elemében (egy listában) találjuk
# meg. Ennek az első eleme mindig a szkript elérési útvonala úgy, ahogy azt indításkor
# megadtuk.

# A test.py nevű szkript tartalma:

import sys

print(sys.argv)

# Ha az indítása így történt (egy alkönyvtárból):

# [útvonal\]python.exe ..\test.py

# akkor a kimenet ez lesz:

# ['..\test.py']

#########################################

# Indítsuk most a szkriptet a saját könyvtárából, paraméterekkel

# python.exe test.py AA "BB CC" 'DD EE'

# A kimenet:

# ['test.py', 'AA', 'BB CC', "'DD", "EE'"]

# Látható, hogy az idézőjelek (") közé tett szavakat egyetlen argumentumnak tekinti,
# de az aposztrofoknak (') nincs ilyen szerepük.

# Ha egy paraméteren belül idézőjelet akarunk elhelyezni, akkor azt meg kell dupláznunk:

# python.exe test.py "BB ""CC"

# ['test.py', 'BB "CC']

#########################################

# Általában az alább felsorolt módokon szoktunk hívási paramétereket átadni egy
# programnak. Az egyszerűség kedvéért hibakezelést nem tettem a példákba, noha
# az ezen a helyen (mint oly sokszor) ELENGEDHETETLEN.

# 1.) Pozícionális. A paraméter jelentését az határozza meg, hogy hányadik a listában.

# python.exe test.py 2 3

import sys

x = sys.argv[1]
y = sys.argv[2]

print('x:', x, 'y:', y) # x: 2 y: 3

# Ennek persze hátránya, hogy könnyű eltéveszteni.

#----------------------------------------

# 2.) Kulcsszóval.

# python.exe test.py x 2 y 3

import sys

i = 1
while i < len(sys.argv):
    if sys.argv[i] == 'x':
        x = sys.argv[i + 1]
    elif sys.argv[i] == 'y':
        y = sys.argv[i + 1]

    i += 2

print('x:', x, 'y:', y) # x: 2 y: 3

#----------------------------------------

# 3.) Kulcsszóval, a kulcsszót - jellel jelezzük. Így olvashatóbb, jobban látszik,
# hogy melyik paraméter a kulcsszó.

# python.exe test.py -x 2 -y 3

import sys

i = 1
while i < len(sys.argv):
    if sys.argv[i] == '-x':
        x = sys.argv[i + 1]
    elif sys.argv[i] == '-y':
        y = sys.argv[i + 1]

    i += 2

print('x:', x, 'y:', y) # x: 2 y: 3

# Találkozhatunk ennek az egybeírt változatával is:

# python.exe test.py -x2 -y3

# Ennek az a hátránya, hogy rosszabbul olvasható.

#----------------------------------------

# 4.) Kulcsszóval, a kulcsszót -- jellel jelezzük.

# python.exe test.py --ezaziksz 2 --ezazipszilon 3

import sys

i = 1
while i < len(sys.argv):
    if sys.argv[i] == '--ezaziksz':
        x = sys.argv[i + 1]
    elif sys.argv[i] == '--ezazipszilon':
        y = sys.argv[i + 1]

    i += 2

print('x:', x, 'y:', y) # x: 2 y: 3

# Ezt általában akkor szokták használni, amikor egy paraméternek lehet rövid írásmóddal
# (egy kötöjel után) vagy hosszú írásmóddal (két kötőjel után) megadni az értékét.
# A hosszabb paraméternév (jó esetben) könnyebben megjegyezhető, de többet kell gépelni.

#----------------------------------------

# 5.) Vegyes: pozícionális paraméterek után kulcsszó paraméterek.

#########################################

# A kulcsszavaknál fontos specifikálni, hogy kisbetű-nagybetű érzékenyek-e. Ha létezik
# x és X kulcsszó is, ami nem célszerű, mert könnyen elhibázható, akkor erre hangsúlyosan
# fel kell hívni a figyelmet. Ha nem akarjuk megkülönböztetni a kétféle írásmódot, akkor
# célszerű mindkettőt megengedni:

# if sys.argv[i].lower() == '-x':...

#########################################

# A paraméterek másik felosztása: kötelező - opcionális. Az opcionális paramétereknek
# van egy default értékük, ha a parancssorban ezeket nem specifikáljuk, akkor a
# default beállítás marad érvényben.

#########################################

# Általánosan elterjedt konvenció, hogy ha a programot paraméter nélkül, -h vagy
# --help paraméterrel hívjuk fel, akkor kiírja a használati utasítását. Hibás
# paramétermegadásnál szintén ez a teendő; ilyenkor célszerű a standard hiba kimenetre
# írni az üzenetet:

print('Hiba!!!!!', file=sys.stderr)

#########################################

# A parancssori paraméterek kezelése meglepően bonyolult feladat. Próbáljunk meg
# például egy paraméter-kezelő függvényt írni egy olyan programhoz, amelynek csak három
# kötelező és négy opcionális paramétere van. Ennek a problémának a megoldását szolgálja
# az argparse modul, melyről később lesz szó.

#########################################
