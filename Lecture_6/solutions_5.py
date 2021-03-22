# Lecture_5\exercises_5.py megoldásai

# 1.

class LimiterClass:
    'klasszikus megoldás (getter-setter)'
    def __init__(self, upperLimit, lowerLimit=None):
        if lowerLimit is not None:
            if lowerLimit > upperLimit:
                lowerLimit = upperLimit

        self.__upper_limit = upperLimit
        self.__lower_limit = lowerLimit
        self.__value = None

    def setValue(self, value):
        if value > self.__upper_limit:
            value = self.__upper_limit

        if self.__lower_limit is not None:
            if value < self.__lower_limit:
                value = self.__lower_limit

        self.__value = value

    def getValue(self):
        return self.__value

# A teszteléshez írjunk egy segédfüggvényt, amelyik a setValue metódust teszteli.
# Kap egy érték-listát, ezeket kell beállítani és egy várt értékek listáját.
# Összehasonlítja a várt és a tényleges értékeket és jelzi a különbségeket.

def check_limiter(limitObj, values, expectedValues):
    for value, expected in zip(values, expectedValues):
       lim.setValue(value)
       x = lim.getValue()
       msg = f'setting value: {value} received: {x} expected: {expected}'
       if x == expected:
           msg = 'OK ' + msg
       else:
           msg = '*** FALSE *** ' + msg + f' received: {x}'

       print(msg)

lim = LimiterClass(10)  # a régi fajta konstruktor
values = (20, 9)
expect_values = (10, 9)
check_limiter(lim, values, expect_values)

# OK setting value: 20 received: 10 expected: 10
# OK setting value: 9 received: 9 expected: 9

lim = LimiterClass(10, 0) # új fajta hívás
values = (20, 3, -1)
expect_values = (10, 3, 0)
check_limiter(lim, values, expect_values)

# OK setting value: 20 received: 10 expected: 10
# OK setting value: 3 received: 3 expected: 3
# OK setting value: -1 received: 0 expected: 0


lim = LimiterClass(10, 20) # felső határ < alsó határ
values = (20, 3, -1)
expect_values = (10, 10, 10)
check_limiter(lim, values, expect_values)

# OK setting value: 20 received: 10 expected: 10
# OK setting value: 3 received: 10 expected: 10
# OK setting value: -1 received: 10 expected: 10

# FONTOS TANULSÁG: tesztelésnek csak azt lehet nevezni, amikor rendelkezésre állnak
# a várt eredmények és ezeket összehasonlítjuk a kapottakkal. Minden más csak pótcselekvés,
# játszadozás, hivatalból üldözendő felforgató tevékenység.

# Amikor összeírjuk a várt eredményeket, akkor a SPECIFIKÁSCIÓT kell nézni, nem a programot.
# Az a jó, ha a programozás ELŐTT már kitalálunk teszteseteket. Programozás közben
# ezekhez hozzá írunk továbbiakat.

####################################

# Miért kapunk itt hibajelzést?

lim = LimiterClass(10)
values = (20)
expect_values = (10)
check_limiter(lim, values, expect_values)

# Traceback (most recent call last):
#   File "test.py", line 41, in <module>
#     check_limiter(lim, values, expect_values)
#   File "test.py", line 26, in check_limiter
#     for value, expected in zip(values, expectedValues):
# TypeError: zip argument #1 must support iteration

####################################

# 2.

# A függvény tuple-ként kapja meg a paramétereit és a lista vagy tuple utolsó
# eleme után állhat vessző. Egy elemű tuple esetén pedig egyenesen közelező. (Kivéve,
# ha függvény paraméterlistájáról van szó.)

####################################
