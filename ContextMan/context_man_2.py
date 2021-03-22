# Saját context manager objektummal megvalósítva I.

# A példa csak bemutatást szolgál; megvalósítjuk a fájl objektumokban már rendelkezésre
# álló context manager interfészt.

# Az __exit__() metódusnak kötelező a bemutatott paramétereket adni; erre a kivételkezeléshez
# van szükség (ld. később).

# Az __enter__() metódusnak azért kell magát az objektumot visszaadnia, mert a

    with [konstruktor] as x

# alaknál erre szükség van. Az x változónak a keletkezett objektumra kell mutatnia.

# A feladatot kompozícióval oldjuk meg, az objektumunknak lesz egy adattagja, amelynek
# az open(), close(), readline() hívásokat továbbadja.

class MyReader:
    def __init__(self, path):
        self.path = path
        self.f_obj = None
        print('__init__')

    def __enter__(self):
        self.f_obj = open(self.path)
        print('__enter__')

        return self

    def __exit__(self, excType, excValue, excTraceback):
        self.f_obj.close()
        self.f_obj = None
        print('__exit__', excType, excValue, excTraceback)

    def readLine(self):
        return self.f_obj.readline()

r = MyReader('van_ilyen.txt')
print('with előtt')
with r:                       # itt FELESLEGES __enter__()-ben a return self
    line = r.readLine()
    print('line:', line, 'with vége')

print('with után')

# __init__
# with előtt
# __enter__
# line: 111 with vége
# __exit__ None None None
# with után

# Nem keletkezett kivétel, ezért __exit__ minden paramétere None.

###########################################

# Így is használhatjuk:

print('with előtt')
with MyReader('van_ilyen.txt') as r: # itt SZÜKSÉGES __enter__()-ben a return self
    line = r.readLine()
    print('line:', line, 'with vége')

print('with után')

# __init__
# __enter__
# line: 111 with vége
# __exit__ None None None
# with után

###########################################

# A fentiekben NEM foglalkoztunk az __enter__ metódusban keletkező kivételekkel,
# ha ilyen létrejön, akkor azt a külső programnak kell elkapnia. Ez teljesen rendben
# van, ha az __enter__-ben fellépő kivétel "katasztrofális" hibát jelez, azaz nem
# akarjuk/tudjuk ilyen esetben elkapni és valahogyan folytatni a végrehajtást.

# Valahogy így:

def func(path):
    with MyReader(path) as r:
        while True:
            line = r.readLine()
            if line == '': break
            print('line:', line)

try:
    func('nincs_ilyen.txt')
except Exception as exc:
    print('ajjaj', type(exc))
else:
    print('rendicsek')

# __init__
# ajjaj <class 'FileNotFoundError'>

###########################################
