# Listák 3.

# tartalmazásvizsgálat: in operátor
# str --> list

x = ['A', 'B', 'C']
print('B' in x, 'D' in x)  # True False

# Így csak egyetlen elemet tudunk keresni, egynél hosszabb rész-listát nem.

print(['B', 'C'] in x)  # False

# Akkor lenne True a kimenet, ha a lista pl. ilyen lenne:

x = ['A', ['B', 'C'], 'D']

print(['B', 'C'] in x)  # True

# ['B', 'C'] EGYETLEN elem!

# Ha nem számít a keresett elemek sorrendje, sem az, hogy egymás mellett legyenek,
# hanem csak az, hogy mindegyiket tartalmazza-e a lista:

x = ['A', 'B', 'C']
searched = ['B', 'C']

found = True
for e_s in searched:
    if e_s not in x:
        found = False
        break

print(found)  # True

# Ha számít a sorrend is, az kicsit bonyolultabb, később visszatérünk rá.

##################

# Sztring átalakítása listává:

x = 'ABC'
y = list(x)
print(y)  # ['A', 'B', 'C']

##################
