# Ismerkedés a generátor függvényekkel

# A generátor-függvény tartalmaz legalább egy yield utasítást.
# Iterátort szolgáltat; minden next() hatására ott folytatja, ahol a
# yield-del abbahagyta.

def my_first_gen():
    print('my_first_gen start')
    yield(1)
    yield(2)
    yield(3)

it = my_first_gen() # semmit nem ír ki!!
print(it) # <generator object my_first_gen at 0x021B0330>

x = next(it) # my_first_gen start
print(x) # 1

x = next(it)
print(x) # 2

x = next(it)
print(x) # 3

#x = next(it) # StopIteration

it = my_first_gen()
for e in it:
    print(e, end=' ')
print()

# my_first_gen start
# 1 2 3

####################################

class Miez:
    def __init__(self, value):
        self.__value = value
        self.__index = len(self.__value) - 1

    def __iter__(self):
        self.__index = len(self.__value) - 1
        return self

    def __next__(self):
        if self.__index < 0:
            raise StopIteration

        index = self.__index
        self.__index -= 1

        return self.__value[index].lower()

m = Miez('PYTHON')
for e in m:
    print(e, end='')
print()
# nohtyp

####################################

# Most ugyanezt generátor-függvénnyel valósítjuk meg.

def miez(param):
    index = len(param) - 1
    while index >= 0:
        yield param[index].lower()
        index -= 1

m = miez('PYTHON')
print(m)
# <generator object miez at 0x021B9630>

for e in m:
    print(e, end='')
print()
# nohtyp

####################################

# Költői kérdés: Melyik megoldás egyszerűbb?

####################################
