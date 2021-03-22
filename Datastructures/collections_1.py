# Ismerkedés a collections modullal
# Counter objektum

# https://www.geeksforgeeks.org/counters-in-python-set-1/
# https://www.guru99.com/python-counter-collections-example.html
# https://docs.python.org/3/library/collections.html
# https://pythonguides.com/python-counter/
# https://www.codegrepper.com/search.php?q=counter%20python
# https://www.w3resource.com/python-exercises/collections/python-collections-exercise-16.php
# https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-35.php
# https://search.zonealarm.com/Search?hp=false&q=python+counter+

############################################

# A konstruktorának átadott iterálható sorozatból kigyűjti, hogy melyik elem hányszor
# fordul elő. A Counter objektum hasonlít egy szótárra.

from collections import Counter

lst = ['a', 'b', 'c', 'a', 'b', 'b']
c = Counter(lst)
print(c)      # Counter({'b': 3, 'a': 2, 'c': 1})
print(c['a']) # 2

# Előfordulás szerint rendezetten adja ki az előfordulásokat.

s = 'abcabb'
c = Counter(s)
print(c)      # Counter({'b': 3, 'a': 2, 'c': 1})
print(c['a']) # 2

def gen():
    yield 'a'
    yield 'b'
    yield 'a'

c = Counter(gen())
print(c)      # Counter({'a': 2, 'b': 1})
print(c['a']) # 2

# A szótártól abban különbözik, hogy ha nem létező elemet kérdezünk le, akkor nem
# kivételt dob, hanem nullát ad vissza.

c = Counter('abcabb')
print(c['X']) # 0

############################################

# A konstruktornak átadhatunk egy szótárt is, amely az elemeket és az előforduldulásuk
# számát tartalmazza.

print(Counter({'A':3, 'B':5, 'C':2})) # Counter({'B': 5, 'A': 3, 'C': 2})

# vagy kulcsszavakat értékekkel:

print(Counter(A=3, B=5, C=2)) # Counter({'B': 5, 'A': 3, 'C': 2})

############################################

# A megszámolandó elemek persze nem feltétlenül sztringek.

lst = [100, 200, 300, 100, 200, 200]
print(Counter(lst)) # Counter({200: 3, 100: 2, 300: 1})

lst = [100, (1, 2), 300, 100, (1, 2), (1, 2)]
print(Counter(lst)) # Counter({(1, 2): 3, 100: 2, 300: 1})

############################################

# Üres objektumot is létre tudunk hozni:

c = Counter()
print(c) # Counter()

############################################

# Az update() metódus értelemszerűen hozzádja az új elemeket:

c = Counter()
print(c) # Counter()

c.update(['a', 'b', 'c', 'a', 'b', 'b'])
print(c) # Counter({'b': 3, 'a': 2, 'c': 1})

c.update('accaaacd')
print(c) # Counter({'a': 6, 'c': 4, 'b': 3, 'd': 1})

# A Counter objektum set-re is hasonlít!

############################################

# A set-hez hasonlóan két ilyen elemet ki lehet vonni egymásból:

c1 = Counter(A=4,  B=3, C=10)
c2 = Counter(A=10, B=3, C=4)

c1.subtract(c2)
print(c1) # Counter({'C': 6, 'B': 0, 'A': -6})

############################################

# A leggyakoribb elemek kiválasztása: most_common() metódus.

c_1 = Counter('abcabb')

m = c_1.most_common(2)
print(m) # [('b', 3), ('a', 2)]

c_2 = Counter(dict(m))
print(c_2) # Counter({'b': 3, 'a': 2})

############################################
