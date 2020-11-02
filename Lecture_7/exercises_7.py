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
