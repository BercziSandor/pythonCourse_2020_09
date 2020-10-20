# Private adattagok kezelése 1.
# A getter-setter megoldás.

class LimiterClass:
    'klasszikus megoldás (getter-setter)'
    def __init__(self, upperLimit):
        self.__upper_limit = upperLimit
        self.__value = None

    def setValue(self, value):
        if value > self.__upper_limit:
            value = self.__upper_limit
        self.__value = value

    def getValue(self):
        return self.__value

lim = LimiterClass(10)
lim.setValue(20)
x = lim.getValue()

lim.setValue(9)
x = lim.getValue()
print(x) # 9

# A limit és az érték közvetlenül (majdnem) nem hozzáférhető. Ha kívülről
# közvetlenül beállíthatók lennének, akkor létre lehetne hozni inkonzisztens
# állapotot, pl. amikor a limit 100 és az érték 200.

#######################################

# Ha nem jöhet létre inkonzisztens állapot, akkor a setter függvény elhagyható,
# az attribútum nyugodtan public lehet (elhagyhatjuk a két alulvonást). Amikor
# a setter csak ennyit csinál:

#    def setValue(self, value):
#        self.__value = value

# akkor semmi szükség nincs rá.

#######################################
