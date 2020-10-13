# Lambda függvény-kifejezések 1.

# https://realpython.com/python-lambda/
# https://docs.python.org/3/howto/sorting.html

# Mark Lutz: Learning Python
#  -> Anonymous Functions: lambda

# Dan Bader: Python Tricks - The Book
#  -> Lambdas Are Single-Expression Functions

# David Beazley, Brian K. Jones: Python Cookbook
#  -> keressünk rá a "lambda" szóra

# Luciano Ramalho: Fluent Python (nagyon utálja a lambda függvényeket)
#  -> Anonymous Functions
############################

# Egy függvénydeklaráció:

def my_func(param):
    return 2 * param

# létrehoz egy függvényobjektumot és hozzárendeli a my_func nevet. Ilyenkor csak maga az objektum
# készül el, a függvény törzsét csak indentálás szempontjából elleőrzi (hogy megtalálja a végét),
# tehát ez például lefut:

def stupid_func():
    nincs_is_ilyen_mi_ez_itt()

print('hello')  # hello

# Létre tudunk hozni névtelen függvényobjektumokat is, ezeket lambda függvényeknek nevezzük.

# Mire lehet jó egy névtelen objektum? Arra, hogy valahol azonnal a keletkezésekor, egyszer felhasználjuk.
# Más objektumokkal kapcsolatban ez megszokott gyakorlat. Van például egy függvényünk, aminek át akarunk
# adni paraméterként egy 2-es konstanst. Ezt így tesszük meg:

my_func(2)

# ami egyszerűbb, mintha külön erre a célra létrehoznánk egy változót, hogy nevet adhassunk a konstansunknak:

two = 2
my_func(two)

# Az első, egyszerűbb megoldásnál is létrehoztunk egy int típusú objektumot, de nem kapott nevet,
# csak felhasználtuk.

############################

# A def kulcsszóval létrehozunk egy függvényt és azonnal nevet is adunk neki. A lambda kulcsszóval
# létre tudunk hozni függvényt úgy, hogy NEM adunk neki nevet.

#            lambda param1, param2,... paramN : KIFEJEZÉS

# a KIFEJEZÉS használja a param1... paramétereket.

# A def egy konstruktor, ami létrehoz egy függvény-objektumot és egy nevet is rendel hozzá; a lambda csak
# létrehozza, de nem ad nevet neki.

# Ez a kifejezés:

lambda param: 2 * param

# egy végrehajtható kifejezés. Mint minden kifejezéshez, ehhez is hozzárendelhetünk nevet (ami nem a tipikus használata):

f = lambda param: 2 * param

# Így keletkezett egy kutyaközönséges függvényünk, amit meg tudunk hívni:

print(f(3))  # 6

# Eddig nem nyertünk semmit, csak annyit értünk el, hogy más szintaktikával is létre tudunk hozni
# függvényt. A lambda kifejezésnek nyilván pont az a specialitása, hogy nem kell nevet adni neki,
# közvetlenül is meg tudjuk hívni:

x = (lambda param: 2 * param)(3)
print(x)   # 6

# Lambda függvény helyett MINDIG használhatunk "normális" függvényt, de van, ahol a lambda egyszerűbb,
# praktikusabb - ott, ahol az illető függvényt egyetlen helyen akarjuk csak használni.

# Csak persze meg kell szokni a szintaktikáját. Eleinte mindenki utálni szokta szegényt.

############################

# KORLÁTOK

# A lambda függvény egy kifejezés, utasításokat, mint pl. if, while nem tartalmazhat.

# Ha kicsit is bonyolultabb a kifejezés, nagyon gyorsan sokkal olvashatatlanabbá tud válni, mint egy
# "normális" függvény. Márpedig az olvashatóság nagy kincs.

############################

# ALKALMAZÁSOK

# 1A.

# lambda függvényt használhatunk ugrótábla kialakításához, hosszabb if...else szerkezetek kiváltása
# céljából (mivel switch sajnos a Pythonban nincs).

# Kiinduló függvény:

def func(funcCode, number):
    if funcCode == 0:
        print(number * number)
    elif funcCode == 1:
        print(2 * number)
    elif funcCode == 2:
        print(number ** -2)

func(1, 10)  # 20

# Persze most képzeljünk el sokkal több elágazást és bonyolultabb kifejezéseket, hogy jobban fájjon.

# Átalakítva:

def func(funcCode, number):
    func_lst = [
      lambda x: x * x,
      lambda x: 2 * x,
      lambda x: x ** -2
    ]

    x = func_lst[funcCode](number)
    print(x)

func(1, 10)  # 20

# Ha nem lambdát használnánk, akkor kellene definiálnunk három függvényt külön
# erre a célra:

def func(funcCode, number):
    def f1(x): return x * x
    def f2(x): return 2 * x
    def f3(x): return x ** -2

    func_lst = [
      f1,
      f2,
      f3
    ]

    x = func_lst[funcCode](number)
    print(x)

func(2, 10)  # 0.01

# f1, f2, f3-at sehol máshol nem akarjuk alkalmazni, egyszer használatosak.
# Ez rosszabbul olvasható (bár ez ízlés kérdése): ha azt akarjuk tudni, hogy
# number = 1 hatsára mit csinál a függvény, akkor először megkeressük
# az egyes indexű elemet, ez f2, aztán megkeressük f2 definícióját.

############################

# 1B.

# Ugrótáblát szótárból is készíthetünk.

# Ha sztringekhez akarjuk hozzárendelni a függvényeket, akkor célszerűen egy szótárban
# helyezzük el a függvényeket.

def func(funcCodeWord, number):
    func_dict = {
      "one":   lambda x: x * x,
      "two":   lambda x: 2 * x,
      "three": lambda x: x ** -2
    }

    x = func_dict[funcCodeWord](number)
    print(x)

func("one", 10)  # 100

# Persze számok esetén is használhatunk szótárat lista helyett:

def func(funcCode, number):
    func_dict = {
      0: lambda x: x * x,
      1: lambda x: 2 * x,
      2: lambda x: x ** -2
    }

    x = func_dict[funcCode](number)
    print(x)

func(1, 10)  # 20

# sőt, ez jobb megoldás, mert sokkal egyszerűbben látható, melyik kódhoz mi tartozik.
# A pozícionális kódolással készült megoldások könnyen elronthatók!

############################

# 2.)

# A sorted függvény alapértelmezett esetben úgy működik, hogy közvetlenül
# hasonlítja össze az elemeket; amelyik kisebb, az kerül előbbre.

lst_1 = ['C','aaaaa','bbb','AAAA','BB']

lst_2 = sorted(lst_1)
print(lst_2)        # ['AAAA', 'BB', 'C', 'aaaaa', 'bbb']

# Sztringeknél egyenként hasonlítódnak össze a karakterek és mivel a kisbetűk kódjai
# nagyobbak az összes nagybetűénél, ezért hátra kerülnek.

# Meg lehet adni key kulcsszóval egy függvényt; ezt fogja minden elemre alkalmazni
# a sorted() függvény és a key függvény visszatérő értékeit hasonlítja össze.

# Ha az elemek hossza szerint akarunk rendezni, akkor a len függvényt adjuk meg:

lst_2 = sorted(lst_1, key=len) # ['C', 'BB', 'bbb', 'AAAA', 'aaaaa']
print(lst_2)

# Mit tegyünk, ha kisbetűssé akarjuk alakítani az összehasonlításhoz az elemeket?
# A lower() nem szabad függvény, hanem metódus - tehát kell csinálnunk egy segédfüggvényt,
# amelyiknek odaadunk paraméterként egy sztringet és ő visszaadja a sztring kisbetűssé
# alakított formáját.

def lower_func(x):
    return x.lower()

lst_2 = sorted(lst_1, key=lower_func)
print(lst_2) # ['AAAA', 'aaaaa', 'BB', 'bbb', 'C']

# Ezt a segédfüggvényt csak külön erre a célra hoztuk létre, többet nem akarjuk használni;
# ez tipikus pálya a lambda számára.

lst_2 = sorted(lst_1, key=lambda x: x.lower())
print(lst_2) # ['AAAA', 'aaaaa', 'BB', 'bbb', 'C']

# a min() és a max() függvényeknél és a list sort() metódusánál hasonló a helyzet, ott is
# meg lehet adni egy összehasonlító key függvényt; hasonlóan a heapq.nlargest() és a heapq.nsmallest()
# metódusoknál is.

# ----------------------------

# Gyakori eset rendezésnél: olyan listát vagy tuple-t akarunk rendezni, amely listákat
# vagy tuple-okat tartalmaz, az elemek valahányadik eleme szerint.

lst_1 = [('John', 180), ('Abraham', 190), ('Eric', 170)]

# "Normál" rendezés, név szerint:

lst_2 = sorted(lst_1)
print(lst_2)  # [('Abraham', 190), ('Eric', 170), ('John', 180)]

# Rendezés magasság, azaz a második mező szerint:

lst_2 = sorted(lst_1,key=lambda x: x[1])
print(lst_2)  # [('Eric', 170), ('John', 180), ('Abraham', 190)]

############################

# Az más nyelvekben is létezik, hogy a rendezéshez definiálni lehet összehasonlító függvényt.
# C-ben például a qsort() standard library függvény ilyen:
#
# void qsort(void *base, size_t nitems, size_t size, int (*compar)(const void *, const void *))
#                                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ----------------------------
#
# Kell egy kis idő, míg megszokja az ember a lambda szintaktikáját és célszerű használatát. Három
# ok miatt éri meg:
#
# 1.) Vannak esetek, amikor egyszerűbb és logikusabb az alkalmazásuk, mint a névvel ellátott
# függvényeké; ld. pl. fentebb a sorted() key paramétere.
#
# 2.) Mások használják és sokszor kell mások kódját megértenünk.
#
# 3.) Mélyebben, alaposabban megértjük a nyelv működését.
