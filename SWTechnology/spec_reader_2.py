# A feladat: olyan fájlolvasó, amely eltávolítja az üres sorokat és azokat,
# amelyekben az első olvasható karakter egy #.

# https://www.youtube.com/watch?v=YXiaWtc0cgE
#  * Ariel Ortiz - The Perils of Inheritance: Why We Should Prefer Composition - PyCon 2019

# 2. megoldás: kompozícióval.

from file_reader import FileReader

class SpecReader_2():
    def __init__(self, path = None):
        self._reader = FileReader(path)

    def setPath(self, path):
        self._reader.setPath(path)

    def close(self):
        self._reader.close()

    def open(self):
        '''Státuszjelzés:
        False, ha bármely okból nem sikerült a művelet
        True, ha sikerült
        '''

        return self._reader.open()

    def readLine(self):
        '''Státuszjelzés:
        -1, ha bármely okból nem sikerült a művelet
        +1, ha sikerült adatot olvasni
        0,  ha már nincs több adat
        '''

        while True:
            ret_dic = self._reader.readLine()
            if ret_dic['status'] <= 0:
                return ret_dic

            data = ret_dic['data'].rstrip()
            if len(data) == 0: continue

            if data.lstrip()[0] == '#': continue

            return ret_dic

##################################

if __name__ == '__main__':
    path = 'nincs_ilyen.txt'
    sr_1 = SpecReader_2(path)

    ret_dic = sr_1.open()
    print('open ezt adta vissza:', ret_dic)

    path = 'van_ilyen.txt'
    sr_1.setPath(path)
    ret_dic = sr_1.open()
    print('open ezt adta vissza:', ret_dic)
    print('*** lássuk a fájl tartalmát')

    while True:
        ret_dic = sr_1.readLine()
        if ret_dic['status'] < 0:
            print('hiba!!!!', ret_dic)
            break

        if ret_dic['status'] == 0:
            break

        print(ret_dic['data'], end='')

    print('*** ennyi volt benne')

###############################

# Hátrány: minden metódushívást delegálni kell a self._reader objektumnak.

###############################

# Előny: Csak azt használjuk a FileReader osztály metódusai közül, amit mi akarunk,
# mintegy mazsolázni tudunk belőlük. Ha holnapután FileReader kap egy új metódust:

class FileReader:
# ...

   def nagy_baromság(self):
       print('most a kútba ugrom')

# akkor ez nem lesz a felhasználóink számára elérhető, amennyiben nem akarjuk.
# A kedves felmenő hagyatékából nem vesszük át tudtunkon kivül veszélyes cuccokat,
# ő már itt nem felmenő, hanem egy szolgáltató.

###############################

# EGY HASONLAT: Legyen az eredeti osztály Étterem típusú, ahol mindenfélét lehet
# rendelni. Egy idő után létrehozunk egy HázhozÉtelt szolgáltatást, amelynél ugyanazokat
# lehet rendelni, mint az Étteremnél, csak épp házhoz szállítják. Mondhatjuk azt, hogy
# ez az új szolgáltatás is egyfajta Étterem, ezért örököltetéssel oldjuk meg:

class HázhozÉtelt(Étterem):
#...

# A bajok akkor kezdődnek, amikor az Étterem új szolgáltatással bővül: kívánságra
# a szakács az asztalnál süti meg a húsokat és a palacsintát. Az öröklés miatt a
# HázhozÉtelt osztály automatikusan felkínálja ezt a lehetőséget, aztán viheti a
# biciklis futár a vázon a séfet a kuncsaft lakására...

###############################



