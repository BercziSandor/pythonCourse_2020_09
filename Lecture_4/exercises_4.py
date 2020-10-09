# 1.

# exercises_3.py 5. feladata ez volt:

# Írjunk egy függvényt, amely paraméterként tetszőleges számú iterálható sorozatot
# kap és egy olyan listát ad vissza, amely az egyes sorozatok maximumait tartalmazza.
# Ha egy listát sem kap bemenetként akkor adjon vissza üres listát.
# A bemeneti sorozatok biztosan nem üresek.

# És a megoldás:

def listofmax(*iterables):
    return [ max(series) for series in iterables ]

# A kikötés a nem üres sorozatokra azért szükséges, mert a max() függvény üres
# sorozatnál ValueError kivételt dob.

print(max([]))

# Traceback (most recent call last):
#   File "test.py", line 1, in <module>
#     print(max([]))
# ValueError: max() arg is an empty sequence

# Ez teljesen logikus: nem létező adatnak nincs maximuma.

# Írjunk most olyan függvényt amelyik ugyanezt csinálja, de ha valamelyik sorozat üres,
# akkor ott None legyen a kimeneti listában; tehát meg van engedve üres sorozat.

#################################

# 2.

# Python 2-ben a print utasításnál nem kellett zárójelet alkalmazni, ez például
# szintaktikailag helyes:

# print 2, 'abc'

# Ugyanez Python 3-ban szintaktikai hiba. Ha viszont paraméterek nélkül leírom:

print

# ez nem okoz szintaktikai hibát. Miért?

#################################

# 3. Alkalmazottak neve és fizetése:

employees = [("James", 285000), ("Cecilia", 120000), ("Zach", 48000), ("Ann", 1258000)]

# tuple-listában akarjuk kiíratni, de úgy, hogy a 130000-nél nagyobb fizetésűek fizetése
# helyett az jelenjen meg, hogy 'titkos'.
# Várt eredmény:

# [('James', 'titkos'), ('Cecilia', 120000), ('Zach', 48000), ('Ann', 'titkos')]

# A.) Comprehension segítségével
# B.) Hagyományos módon, comprehension nélkül.

#################################

# 4.)

# A sum() függvény üres sorozatra 0-t ad vissza, ami szerintem nem logikus, mert
# nem lehet megkülönböztetni a 0 összegű sorozatot az ürestől:

x = sum([10, -10])
y = sum([])
print(x, y)  # 0 0

# (Persze ez a konvenció egyes esetekben megkönnyíti a programozást. De azért
# nem igazán tetszik.)

# Írjunk függvényt, amely paraméterként tetszőleges számú iterálható sorozatot
# kap és egy olyan listát ad vissza, amely az egyes sorozatok összegét tartalmazza.
# Ha egy listát sem kap bemenetként akkor adjon vissza üres listát. Az üres listák
# összegeként adjon vissza None-t.

lst_1 = [1, 2, -3]
tup_2 = [10, 20, 30]
set_3 = {100, 200, 300}
lst_empty = []

print(listofsum(lst_1, tup_2, set_3, lst_empty)) # [0, 0, 600, None]
print(listofsum()) []

# A. Listcomp segítségével.
# B. Hagyományos módon.

#################################

# 5.)

# Elő kell állítani egy listát egy bemeneti iterálható sorozatból; az int vagy float
# típusú elemeket kell kigyűjteni.

lst = [ 'abc', 2, 3.5, (4, 5), ['A', 'Z'], -20 ]

# Várt eredmény:

# [2, 3.5, -20]

# A. Listcomp segítségével.
# B. Hagyományos módon.

#################################

# 6.

# Adott egy pozitív számokból álló lista. Elő kell állítani egy másik
# listát, amely sztringgé alakítva tartalmazza az elemeket, vezető nullákkal kiegyészítve
# 4 hosszra. A 4 és annél nagyobb hosszúságú elemek maradjanak változatlanok.

lst = [ 2, 30, 100, 3000, 40000 ]

# Várt eredmény:

# ['0002', '0030', '0100', '3000', '40000']

# A. Listcomp segítségével.
# B. Hagyományos módon.

#################################

# 7.

# Írunk egy függvényt, amely a paraméterében adja vissza az eredményt és a státuszt is.

def stupid_func(param, resultDict):
    resultDict = {'status': False, 'result': None}

    if param < 0:
        return

    resultDict['status'] = True
    resultDict['result'] = 10 * param

    return

# Teszt:

result_dict = {'status': False, 'result': None}
stupid_func(2, result_dict)
print(result_dict)  {'status': False, 'result': None}

# Váratlan az eredmény, 20-at vártunk volna.

# A. Mi az oka?
# B. Javítsuk ki!

#################################
