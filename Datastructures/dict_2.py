# Dictionary (szótár) 2.

# Keresés úgy, hogy az illető kulcs esetleg nincs benne a szótárban
# get, setdefault függvény

dic = {'A': 1, 'B': 2}

if 'C' in dic:
    x = dic['C']
else:
    x = 999

print(x) # 999

# Hátrány: kicsit hosszadalmas és ráadásul lassú is (ami csak nagyon nagy ismétlésszámnál
# számíthat), mert kétszer keresünk a szótárban.

# Más formában ugyanez:

x = dic['C'] if 'C' in dic else 999
print(x) # 999

try:
    x = dic['C']
except KeyError:
    x = 999

print(x) # 999

x = dic.get('C',999)
print(x) # 999

#######################################

# A feladat: ha nincs benne a szótárban az elem, akkor beleírjuk.

dic = {'A': 1, 'B': 2}

if 'C' in dic:
    x = dic['C']
else:
    dic['C'] = 999
    x = 999

print(x) # 999

try:
    x = dic['C']
except KeyError:
    dic['C'] = 999
    x = 999

print(x) # 999

x = dic.setdefault('C',999)
print(x) # 999

# Ez a legszebb (és leggyorsabb) megoldás.

#######################################
