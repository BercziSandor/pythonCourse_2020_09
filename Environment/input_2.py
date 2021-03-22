# Beolvasás a sys modul segítségével
# sys.stdin mint iterátor
# sys.stdin.readlines() és read() metódusok

# A sys.stdin ugyanolyan fájlobjektumként kezelhető, mint az open() által visszaadott
# objektumok. for ciklusban ugyanúgy tudjuk a beírt sorokat olvasni vele, mint ahogy
# egy fájl sorait olvassuk:

import sys

for line in sys.stdin:
    print(line.rstrip('\n'))
    
# Ctrl-Z-vel jelezhetjük a bemenet végét, illetve Ctrl-C-vel is lehet, ez KeyboardInterrupt
# kivételt generál, amit persze elkaphatunk.

###############################################

# A readlines() metódus is ugyanúgy működik, egy list-be kerülnek be a sorok:

import sys

lines = sys.stdin.readlines()
print(lines)

###############################################

# A teljes bemenetet egyetlen sztringbe a read metódussal tudjuk beolvasni:

import sys

s = sys.stdin.read()
print(s)

###############################################

