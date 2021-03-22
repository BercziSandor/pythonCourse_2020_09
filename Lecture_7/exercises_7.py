# 1.)

# Alkalmazottak neve és fizetése:

employees = [("James", 285000), ("Cecilia", 120000),
             ("Zach", 48000), ("Ann", 1258000)]

# Állítsuk elő a nevek listáját ábécé szerint csökkenő sorrendben!

# Az alábbi megoldás jó eredményt ad; egyszerüsítsük le!

names_reversed = list(dict(sorted(employees, key=lambda x: x[0], reverse=True)).keys())
print(names_reversed) # ["Zach","James", "Cecilia", "Ann"]

############################################

# 2.)

# Adott egy lista és egy tuple:

lst = [10, 11, 5, 6, 7, 4]
tup = (10, 11, 7, 4)

# Állítsunk elő egy tuple-t, amely lst azon elemeinek négyzetét tartalmazza, melyek
# nem fordulnak elő tup-ban.

# A következő megoldás jó eredményt szolgáltat:

res = []
for e in set(lst).difference(tup):
    res.append(e*e)

print(res) # [25, 36]

# A. Adjunk meg olyan bemenő adatokat, amelyekkel nem jó eredményt szolgáltat ez a megoldás.

# B. Adjunk jó megoldást.

############################################

# 3.)

# Adott egy függvény, amelynek a lines nevű paramétere sztringek listáját tartalmazza,
# search_list pedig keresendő sztringek listája. A kimenet lines azon elemeinek listája,
# amelyekben a keresett sztringek bármelyike előfordul.

def find_any(lines, search_list):
    out_lst = []
    for line in lines:
        for searched in search_list:
            if searched in line:
                out_lst. append(line)

    return out_lst

lines = ['AA BB CC', 'DD EE FF', 'GG HH II']
s_list = ('AA', 'EE', 'XX')

result = find_any(lines, s_list)
print(result) # ['AA BB CC', 'DD EE FF']

# A.

# Ezekkel az adatokkal jó eredményt szolgáltat a függvény. Adjunk meg olyan adatokat,
# amelyekkel hibás lesz a kimenet.

# B.

# Javítsuk ki!

############################################

# 4.)

# Írjunk hasonló függvényt, mint az előző feladatban, de ez azokat a sorokat adja
# vissza, amelyekben mindegyik keresett sztring előfordul.

def find_all(lines, search_list):
    pass

lines = ['AA BB CC', 'AA EE FF', 'GG HH II']
s_list = ('AA', 'EE')

result = find_all(lines, s_list)
print(result) # ['AA EE FF']

############################################

# 5.)

# Ez egy kicsit bonyolultabb, állapotokat kell megjegyezni benne.

# Írandó egy generátor függvény, amely két iterálható sorozatot kap paraméterként. Mindkét
# sorozat rendezett számsorozat (vagy lehet üres is). A generátornak össze kell fésülnie
# a két sorozatot egyetlen rendezett sorozattá.

def merge_func(series_1, series_2):
    pass

# Tesztesetek:

lst_1 = [10, 20, 30, 40, 40, 40]
lst_2 = [15, 25, 30, 50]

for x in merge_func(lst_1, lst_2):
    print(x, end=' ') # 10 15 20 25 30 30 40 40 40 50
print()

lst_1 = []
lst_2 = [15, 25, 30, 50]

for x in merge_func(lst_1, lst_2):
    print(x, end=' ') # 15 25 30 50
print()

lst_1 = [10, 20, 30, 40, 40]
lst_2 = [15, 25, 25, 50]

lst = [x for x in merge_func(lst_1, lst_2)]
print(lst) # [10, 15, 20, 25, 25, 30, 40, 40, 50]

############################################
