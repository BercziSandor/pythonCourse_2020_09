# A feladat: olyan fájlolvasó, amely eltávolítja az üres sorokat és azokat,
# amelyekben az első olvasható karakter egy #.

# https://www.youtube.com/watch?v=YXiaWtc0cgE
#  * Ariel Ortiz - The Perils of Inheritance: Why We Should Prefer Composition - PyCon 2019

# 1. megoldás: örököltetéssel.

from file_reader import FileReader

class SpecReader_1(FileReader):
    def __init__(self, path = None):
        super().__init__(path)

    def readLine(self):
        '''Státuszjelzés:
        -1, ha bármely okból nem sikerült a művelet
        +1, ha sikerült adatot olvasni
        0,  ha már nincs több adat
        '''

        while True:
            ret_dic = super().readLine()
            if ret_dic['status'] <= 0:
                return ret_dic

            data = ret_dic['data'].rstrip()
            if len(data) == 0: continue

            if data.lstrip()[0] == '#': continue

            return ret_dic

##################################

if __name__ == '__main__':
    path = 'nincs_ilyen.txt'
    sr_1 = SpecReader_1(path)

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

# Előny: néhány metódust egyszerűen öröklünk, nem kell újból ezeket beprogramozni.
# Itt ezek: setPath(), open(), close().

###############################

# Hátrány: MINDENT öröklünk, ami az ős-osztályban MOST VAGY A JÖVŐBEN elérhető.
# Olyasmit is, amit nem feltétlenül szeretnénk. Ha két hét múlva beépítenek valamit
# az ős-osztályba, ami a mi felhasználóink számára veszélyes vagy felesleges,
# nem is fogunk tudni róla.
# Ha FileReader kap egy új metódust:

class FileReader:
# ...

   def nagy_baromság(self):
       print('most a kútba ugrom')

# akkor ez SpecReader_1 felhasználói számára is elérhető lesz.

# Egy kicsit valóságosabb példa: Az ős osztályba beépítenek egy metódust, amellyel
# át lehet kapcsolni a működést úgy, hogy bizonyos hossz felett csonkolja olvasáskor
# a readLine metódus a sorokat.

class FileReader:
# ...
   def set_truncate(self, maxLength):
       self._do_truncate = True
       self._max_length = maxLength

    def readLine(self):
        #...

        try:
            data = self._f_obj.readline()
            if len(data) > self._max_length:
                data = data[:self._max_length]
        #...

# Ekkoor ez működni fog:

sr_1 = SpecReader_1(path)
sr_1.set_truncate(10)
#...

# A sorok 10 hosszúra lesznek nyisszantva, mert a felmenőnk ezt jó ötletnek
# tartotta és persze nekünk nem szólt róla, csak a felhasználóknak.. Ha akart
# volna szólni, akkor se tudott volna, hiszen ő nem tudja, hogy a jövőben ki hol
# fog örököltetni az osztályából.

###############################
