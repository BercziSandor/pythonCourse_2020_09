# 1.)

# Lecture_12\exercises_12.py 3. feladathoz térünk vissza, módosítjuk egy kicsit.

# Írjunk generátor-függvénnyel megvalósított iterátort, amely inicializáláskor egy
# iterálható obkektumot és egy egész számot kap paraméterként. Azokat az elemeket
# adja vissza a számmal elosztva a bemeneti objektum által szolgáltatott sorozatból,
# amelyek oszthatóak a számmal. A bemeneti sorozat lehet inhomogén; amely elemeken nem
# végezhető el a modulo művelet, azokat az iterátor adja ki változatlanul a kimenetre.

def modIterFunc_2(inputSeries, number):
    pass

m = modIterFunc_2([1, 'A', [10, 20], 66, 8, 12, (24, 36)], 6)

for e in m:
    print(e)

# 'A'
# [10, 20]
# 11.0
# 2.0
# (24, 36)

############################################
