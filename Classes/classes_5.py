# Private adattagok kezelése 2.
# A property dekorátoros megoldás.

# classes_3.py-ban láttunk egy kis osztályt, ami limitálta az általa tárolt értéket.
# Az értéket (kvázi) private adattagként tárolta, hogy közvetlenül ne lehessen módosítani.

# Szeretnénk a kontrollt megtartani (tehát a tárolt értéket limitálni) és mégis olyan
# szintaktikával hozzáférni az adattaghoz, mintha public lenne. A Pythonban erre lehetőséget
# nyújt a property dekorátor. A dekorátorokról szó lesz később, egyelőre fogadjuk el ezt a
# szintaktikát.

class LimiterClass_2:
    'property dekorátoros megoldás'
    def __init__(self, upperLimit):
        self.__upper_limit = upperLimit
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, newValue):
        if newValue > self.__upper_limit:
            newValue = self.__upper_limit
        self.__value = newValue

lim = LimiterClass_2(10)
lim.value = 20
x = lim.value
print(x) # 10

########################################

# Ez a szintaktika akkor lehet nagyon hasznos, amikor public adattagot használunk
# egy osztályban és később kiderül, hogy private-té kellene tenni, mert be kell
# építeni valami ellenőrzést. Már sokan használják az osztályt, ezért roppant fájdalmas
# lenne áttérni a getter-setter interfészre - ilyenkor segít a property dekorátor.

# Ezen kívül az olvashatóságot is nagyban javítja a getter-setter megoldáshoz képest.
# Melyik szebb?

# x.setValue(y.getParam1() - 2 * z.getParam2())

# x.value = y.param1 - 2 * z.param2

########################################
