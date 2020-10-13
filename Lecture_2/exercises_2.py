# 1. Alkalmazottak neve és fizetése:

employees = [("James", 285000), ("Cecilia", 120000), ("Zach", 48000), ("Ann", 1258000)]

# Állítsunk elő egy listát a fizetés szerint rendezve. Várt eredmény:

# [('Zach', 48000), ('Cecilia', 120000), ('James', 285000), ('Ann', 1258000)]

###########################

# 2. Állítsuk elő a nevek listáját ábécé szerint csökkenő sorrendben. Várt eredmény:

# ['Zach', 'James', 'Cecilia', 'Ann']

###########################

# 3. Egy változó értéke legyen True, ha a listában minden fizetés különböző, illetve False,
# ha van legalább két egyforma fizetés. Várt eredmény: True.

###########################

# 4. Készítsünk egy listát azoknak a nevéből, akiknek a fizetése < 150000. Várt eredmény:

# ['Cecilia', 'Zach']

###########################

# 5. Adott egy lista és egy tuple:

lst = [ 10, 11, 5, 6, 7, 4 ]
tup = ( 10, 11, 7, 4 )

# Állítsunk elő egy tuple-t, amely lst azon elemeinek négyzetét tartalmazza, melyek nem fordulnak elő tup-ban.

# Várt eremény: (25, 36)

# Listcomp nélkül:

tmp_lst = []
for e in lst:
    if e not in tup:
        tmp_lst.append(e * e)

tup_2 = tuple(tmp_lst)
print(tup_2)

###########################

# 6. Adott az exercise_6.txt fájl. Tegyük bele egy listába mindazon sorok hosszát, amelyekben előfordul
# kisbetű-nagybetű függetlenül az 'aaa' sztring. A hosszban ne legyen benne a sorvégjel.

# Várt eredmény: [10, 22]

###########################
