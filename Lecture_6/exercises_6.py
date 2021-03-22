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

# Meg kell változtatni az osztályt; setValue()-nek legyen egy opcionális paramétere
# False default értékkel. Ha ez a paraméter True, akkor dobjon a metódus ValueError
# kivételt, amikor a beállítandó érték nagyobb a felső határnál.

############################################

# 2.)

# Adott egy függvény, ami karakterekre bontja a bemeneti sztringet és az írásjeleket
# szóközre cseréli:

def punct_replace(inStr, punctChars):
    ret_lst = []
    for c in inStr:
        if c in punctChars:
            ret_lst.append(' ')
        else:
            ret_lst.append(c)

    return ret_lst

punct_chars = '.,;:?!-'
in_str = 'Van? Vagy, esetleg, nincs.Nem tudom!Lehetséges.'
out_str = ''.join(punct_replace(in_str, punct_chars))
print(out_str) # Van  Vagy  esetleg  nincs Nem tudom Lehetséges

# A.

# Írjuk meg a függvényt listcomp segítségével.

# B.

# Rájövünk, hogy gyorsabb lesz a függvényünk, ha nem sztringben, hanem egy set-ben
# adjuk meg az írásjel-karaktereket:

punct_chars = set('.,;:?!-')

# Mit kell változtatni a függvényen?

# C.

# Tovább akarjuk gyorsítani a függvényünket, ezért írjuk át úgy, hogy az elején
# elkészít egy megfelelő méretű listát, aztán ennek az elemeit változtatja megfelelően.

# D.

# A függvényünk (bármelyik változata) segítségével állítsunk elő egy sztringet, amely
# a bemeneti sztring szavait tartalmazza egyetlen szóközzel elválasztva.

############################################

# 3.)

# Adott egy függvény, amely egy listában visszaadja a bemeneti sorozat str típusú elemeit:

def getStrings(inSeries):
    return [e for e in inSeries if isinstance(e, str)]

in_lst = [1, '2', (20, '30'), {'A': 9}, 'X']
out_lst = getStrings(in_lst)
print(out_lst) # ['2', 'X']

# Írjunk generátor függvényt, ami visszaadja a bemeneti sorozat str típusú elemeit.
# Készítsünk a segítségével listát az ilyen típusú elemekből.

############################################
