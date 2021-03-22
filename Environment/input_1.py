# Beolvasás konzolról, input() függvény
# standard bemenet átirányítása
# programok pipeline-ba kapcsolása

# Az input függvénynek megadhatunk egy paramétert, ezt fogja kiírni a képernyőre.
# A beolvasásnak RETURN vet véget. A beolvasott érték mindig sztring típusú:

x = input('kérek egy számot: ')  # beírom: 22<ENTER>
print(x, type(x)) # 22 <class 'str'>

# Az input() függvény segítségével nem tudunk több sort egyszerre bevinni.

###############################################

# Ha Ctrl-C-t adunk be, akkor a program KeyboardInterrupt kivételt generál, amit
# persze el is kaphatunk:

while True:
    try:
        x = input('mondj valamit: ')
        print('azt mondtad:', x)
    except KeyboardInterrupt:
        print('búcsúzom')
        break

###############################################

# A standard bemenetet átirányíthatjuk úgy, hogy egy fájlból jöjjön a bemenet:

# A szkriptünk tartalma:

while True:
    try:
        x = input()
        print(x)
    except EOFError:
        print('búcsúzom')
        break

# Indítása:

python.exe test.py < in.txt

###############################################

# Ha egy program a standard kimenetére ír és egy másik a standard bemenetéről olvas,
# akkor ezeket | jellel összekapcsolhatjuk. Egyszerű szemléltetésként az indító szkript
# írjon echo utasítással valamit a kimenetére, amit a Python szkriptünk beolvas:

echo hello | python.exe test.py

###############################################

