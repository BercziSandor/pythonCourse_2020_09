# 1.)

# Classes\classes_3.py-ban található ez az osztály:

class LimiterClass:
    'klasszikus megoldás (getter-setter)'
    def __init__(self, upperLimit):
        self.__upper_limit = upperLimit
        self.__value = None
        self.__x__ = 7

    def setValue(self, value):
        if value > self.__upper_limit:
            value = self.__upper_limit
        self.__value = value

    def getValue(self):
        return self.__value
        
# Meg kell változtatni az osztályt; setValue()-nek legyen egy opcionális paramétere
# False default értékkel. Ha ez a paraméter True, akkor dobjon a metódus ValueError
# kivételt, amikor a beállítandó érték nagyobb a felső határnál.

############################################

