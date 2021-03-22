# Listák 2. (És egy kevés sztring.)
# + (konkatenálás) kontra append()
# += operátor
# lst += [valami] kontra lst = lst + [valami]
# szorzás ismételt összeadás helyett
# inkrementáló operátor sztringeknél

# https://stackoverflow.com/questions/58892927/how-is-python-statement-x-x1-implemented

x = [1, 2, 3]
y = x + [4, 5]
print(y)  # [1, 2, 3, 4, 5]

# Hiba, mert összeadni csak azonos típusokat lehet:

y = x + 4

# Traceback (most recent call last):
#   File "test.py", line 11, in <module>
#     y = x + 4
# TypeError: can only concatenate list (not "int") to list

#############################################

# Az előző feladat megoldására való az append() metódus:

x = [1, 2, 3]
x.append(4)
print(x)  # [1, 2, 3, 4]

#############################################

# Persze az eredeti változó is mutathat a megnövelt listára, ha az eredeti
# listára már nincs szükség:

x = [1, 2, 3]
x = x + [4, 5]
print(x)  # [1, 2, 3, 4, 5]

# A változó neve ugyanaz, de a lista most már új címen van!

#############################################

# += operátor (addition assignment, inkrementálás operátor, összeadás rekurzív operátor)

x = [1, 2, 3]
x += [4, 5]
print(x)  # [1, 2, 3, 4, 5]

# A változó neve ugyanaz és a lista a régi címen van.

#############################################

# x = x + [4, 5] és x += [4, 5] MAJDNEM ugyanazt csinálja.

x = [1, 2, 3]
id_1 = id(x)

x = x + [4, 5]
id_2 = id(x)
print(id_1, id_2)  # 42788744 42788184

# A két memóriacím nem egyforma; keletkezett egy új lista.
# Az eredetire már nem mutat egy változó sem, felszabadítódik.
# Olyan, mintha ezt csináltuk volna:

x = [1, 2, 3]
y = x + [4, 5]  # y: átmeneti segédváltozó
x = y
del(y)   # megszüntetjük az y nevet

#--------------------------------------

# Nézzük meg most a += operátort.

x = [1, 2, 3]
id_1 = id(x)
x += [4, 5]
id_2 = id(x)
print(id_1, id_2)  # 5302152 5302152

# A művelet az eredeti listán, helyben hajtódott végre, nem
# keletkezik új lista. Ez memóriatakarékosabb és valamivel
# gyorsabb (ami ritkán, nagyon nagy listáknál és/vagy sokszor végrehajtott
# ciklusok belsejében számít).

# Olyankor van viszont jelentősége a különbségnek, ha
# más változó is mutat az eredeti listára.

# Egyik eset:

x = [1, 2, 3]
y = x
print(id(x), id(y))  # 7136640 7136640

# egyformák a memóriacímek, egyetlen lista van, két változó mutat rá

x = x + [4, 5]
print(x, y)           # [1, 2, 3, 4, 5] [1, 2, 3]

# y az eredetire mutat!

# Másik eset:

x = [1, 2, 3]
y = x

x += [4, 5]
print(x, y)            # [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]

# mindkettő az új listára a mutat

# Ha az y változót is használjuk a továbbiakban, akkor nagyon nem mindegy,
# melyik módon növeljük meg a listát!

#############################################

# Nézzük meg az inkrementáló operátort sztringeknél.

x = 'ABC'
id_1 = id(x)

x += 'DE'
id_2 = id(x)

print(id_1, id_2)  # 4838240 6378752

# Itt megváltozott a memóriacím, mivel a sztring immutábilis típus. Ha az eredeti
# memóriacímen keletkezne az eredmény, akkor az eredeti sztring megváltozott volna.

#############################################

# Szorzást használhatunk az ismételt összeadás helyett:

x = [1, 2] + [1, 2] + [1, 2]
print(x) # [1, 2, 1, 2, 1, 2]

x = [1, 2] * 3
print(x) # [1, 2, 1, 2, 1, 2]

#############################################
