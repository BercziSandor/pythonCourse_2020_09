# Olyan osztály készítése, amely iterálható és egyben saját iterátora is.

class MyRange():
    'An iterable AND iterator class'
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.pos = self.start

    def __iter__(self):
        self.pos = self.start # alaphelyzetbe állunk

        return self    # mert az objektum az iterátor is

    def __next__(self):
        if self.pos >= self.end:
            raise StopIteration

        ret_val = self.pos
        self.pos += 1

        return ret_val

# A MyRange típusú objektumokkal mindent lehet csinálni, amit általában az iterálhatóakkal.

r = MyRange(2,5)

# next()-tel végiglépegetünk:

it = iter(r) # előállítunk egy iterátort

x = next(it)
print(x) # 2

x = next(it)
print(x) # 3

x = next(it)
print(x) # 4

x = next(it)
# Traceback (most recent call last):
#   File "test.py", line 34, in <module>
#     x = next(it)
#   File "test.py", line 15, in __next__
#     raise StopIteration
# StopIteration

# for ciklussal bejárjuk:

for e in r:
    print(e, end=' ')
print()

# 2 3 4

# enumerate-tel bejárjuk:

for i, e in enumerate(r):
    print(i,e, end=';')
print()

# 0 2;1 3; 2 4;

# Vesszük az elemek összegét és maximumát:

s = sum(r)
m = max(r)
print(s,m) # 9 4

# Listát csinálunk belőle:

lst = list(r)
print(lst) # [2, 3, 4]

# Ez a mi kis range objektumunk nem csak egész számokat tud kezelni:

r = MyRange(2.5,5.5)
for e in r:
    print(e, end=' ')
print()

# 2.5 3.5 4.5

###############################################

# Egyszerű számláló helyett persze akármilyen bonyolult algoritmust is rejthet
# az iterálónk; ha az __iter__ és __next__ metódusokat megvalósítja, akkor ugyanúgy
# lesz kezelhető, mint például egy lista.

###############################################
