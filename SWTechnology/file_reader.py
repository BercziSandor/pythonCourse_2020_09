# https://realpython.com/read-write-files-python/
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

# Az alábbi osztályt fogjuk használni a kompozíció kontra örököltetés tervezési
# kérdés szemléltetésénél. Ez nem Python-specifikus téma, minden OO nyelvben találkozunk vele.

class FileReader:
    '''Szöveges fájlból tud sorokat olvasni. Minden kivételt elkap és státuszjelzés
    formájában adja vissza a hívónak.
    '''
    def __init__(self, path = None):
        self._path = path
        self._f_obj = None

    def setPath(self, path):
        self.close()
        self._path = path

    def close(self):
        if self._f_obj is not None:
            self._f_obj.close()

        self._f_obj = None

    def open(self):
        '''Státuszjelzés:
        False, ha bármely okból nem sikerült a művelet
        True, ha sikerült
        '''

        self.close()
        try:
            self._f_obj = open(self._path) # = open(self._path, 'rt')
        except Exception as e:
            return { 'status': False, 'details': str(e) }
        else:
            return { 'status': True, 'details': '' }

    def readLine(self):
        '''Státuszjelzés:
        -1, ha bármely okból nem sikerült a művelet
        +1, ha sikerült adatot olvasni
        0,  ha már nincs több adat
        '''

        if self._f_obj is None:
            return { 'status': -1, 'data': None, 'details': 'no file' }

        try:
            data = self._f_obj.readline()
        except Exception as e:
            return { 'status': -1, 'data': None, 'details': str(e) }
        else:
            status = 1 if len(data) > 0 else 0
            return { 'status': status, 'data': data, 'details': '' }

# Minden dokumentációs leírásnál, amit egy függvényhez készítünk a két legfontosabb dolog:
#  * bemenő paraméterek magyarázata
#  * státuszjelzés leírása

# A státuszjelzést kezdettől fogva be kell építeni a programba, mert később ez már
# szinte reménytelen. Olyan a helyzet, mintha egy házat építenénk úgy, hogy a víz-
# és elektromos vezetékeket majd később fogjuk beleépíteni, amikor minden más már
# készen van.

##################################

if __name__ == '__main__':
    path = 'nincs_ilyen.txt'

    fr = FileReader(path)
    ret_dic = fr.open()
    print('open ezt adta vissza:', ret_dic)

    path = 'van_ilyen.txt'
    fr.setPath(path)
    ret_dic = fr.open()
    print('open ezt adta vissza:', ret_dic)
    print('*** lássuk a fájl tartalmát')

    while True:
        ret_dic = fr.readLine()
        if ret_dic['status'] < 0:
            print('hiba!!!!', ret_dic)
            break

        if ret_dic['status'] == 0:
            break

        print(ret_dic['data'], end='')

    print('*** ennyi volt benne')
