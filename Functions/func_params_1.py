# http://www.trytoprogram.com/python-programming/python-function-arguments/
# https://www.python-course.eu/python3_functions.php
# https://www.python-course.eu/python3_passing_arguments.php
# https://note.nkmk.me/en/python-argument-expand/
# https://data-flair.training/blogs/python-function-arguments/
# https://www.w3resource.com/python/python-user-defined-functions.php
# https://stackoverflow.com/questions/14301967/bare-asterisk-in-function-arguments

print('Függvény paraméter nélkül')

def func():
    print('Hello!')

func()   # Hello!

print('Csak kötelező pozícionális paraméterek')

def func(a, b, c):
    print(a,b,c)

# A függvény is egy objektum:

print(func, id(func), hex(id(func))) # <function func at 0x001FD660> 2086496 0x1fd660

func(1,2,3)        # 1 2 3
func(a=1,b=2,c=3)  # hívható névvel is (olvashatóbb)
func(c=3,a=1,b=2)  # tetszőleges sorrendben - korrekt, de zavaró lehet

func(1,b=2,c=3)    # nem sok értelme van, de lehetséges

#func(a=1,2,c=3)  # hiba, pozícionális nem lehet kulcsszó-paraméter után
#func(1,b=2)        # hiba, c hiányzik

print('\nNév (kulcsszó) megadásának kikényszerítése')

def func(a, *, b, c):
    print(a,b,c)

func(1,b=2,c=3)  # 1 2 3
# func(1,2,3)    # hiba, nincs kulcsszó megadva b-hez és c-hez

print('\nDefault paraméter-értékek megadása')

def func(a, b=2, c=3):  # b és c nem kötelező
    print(a,b,c)

func(10,20,30)         # 10 20 30
func(a=10,b=20,c=30)   # 10 20 30 lehet az összes kulcsszóval megadva
func(10)               # 10 2 3
func(10,c=30)          10 2 30
# func()               # hiba, a kötelező a paramétert nem adtuk meg

print('\nNév (kulcsszó) megadásának kikényszerítése 2.')
def func(a, *, b=2, c=3):  # b és c nem kötelező, de ha megadjuk őket,akkor kulcsszóval kell
    print(a,b,c)

func(10)      # 10 2 3
func(10,b=20) # 10 20 3
#func(1,2)    # hiba: nincs kulcsszó b-hez
