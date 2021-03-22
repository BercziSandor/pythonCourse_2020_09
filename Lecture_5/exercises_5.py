# 1.)

# Classes\classes_3.py-ban található ez az osztály:

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

# Ezt nagy sikerrel adta el a gyártó Nonprofi Kft - számos helyen importálják
# Python programokba és használják. Felmerül az igény továbbfejlesztésre: el kellene
# látni az osztályt alsó határral is, aminél kisebb érték nem tárolható benne.
# Így nem akarjuk csinálni:

class LimiterClass:
    def __init__(self, upperLimit, lowerLimit):
    #...

# mert akkor az ÖSSZES programot meg kellene változtatniuk a vevőinknek, ahol
# LimiterClass-t használják. Ráadásul csak futás közben derülne ki egyes esetekben, hogy
# a programozó elfelejtette adott helyen módosítani a LimiterClass konstruktorának hívását.

# A. Az eddigi egy paraméteres hívás:

lim = LimiterClass(10)

# legyen ezentúl is lehetséges (ne jelentsen szintaktikai hibát).

# B. Ilyenkor működjön ugyanúgy az osztály, mint eddig: alsó korlát ne legyen az értékre.

# C. Ha megadunk alsó korlátot:

lim = LimiterClass(10, -20)

# akkor csak ezen korlátok közötti értéket lehessen beállítani (-20 < value < 10).

# D. Ha a felső határ <= az alsónál, akkor csak a felső határral megegyező értéket
# lehessen beállítani.

# A Nonprofi Kft-nek jelenleg minden fejlesztő kapacitása foglalt, ezért árajánlatot
# kértek a Lehúz és Tsa. nemzetközi tanácsadó cégtől, de akkora összeg szerepelt az ajánlatban,
# hogy azt nem tudták egy Python program változójában elhelyezni, ezért más megoldást keresnek.

# Segítsünk nekik, készítsük el a LimiterClass feltuningolt változatát!

########################################

# 2.

# Itt miért nem kapunk hibajelzést?

lim = LimiterClass(10,)

########################################
