# http://www.trytoprogram.com/python-programming/python-function-arguments/
# https://www.python-course.eu/python3_functions.php
# https://www.python-course.eu/python3_passing_arguments.php
# https://note.nkmk.me/en/python-args-kwargs-usage/
# https://data-flair.training/blogs/python-function-arguments/
# https://www.w3resource.com/python/python-user-defined-functions.php

# Dan Bader: Python Tricks - The Book
#  -> Fun With *args and **kwargs

# Opcionális pozícionális paraméterek

# Tetszőleges számú pozícionális paraméter: *args.

def func(*args):  # args: egy tuple
    print(args, type(args))

func(10,20) # (10, 20) <class 'tuple'>

def func(*args):
    print(len(args), ' darab paraméter', end='|')
    for arg in args:
        print(arg, end=' ')
    print()

func(10, 20) # 2 darab paraméter|10 20

# A *args név bármi más is lehet, az args a szokásos.

################################

# Opcionális kulcsszó paraméterek

def func(**kwargs):  # kwargs: egy dict
    print(kwargs, type(kwargs))

func(a=10,b=20) # {'a': 10, 'b': 20} <class 'dict'>

# kwargs név is csak konvenció.

def func(**kwargs):
    for item in kwargs.items():  # item: key-value tuple
        print(item, end=' ')

    print()

    for item in kwargs.items():
        print(item[0],'=',item[1], end='; ')

    print()

func(a=10, b=20)

# ('a', 10) ('b', 20)
# a = 10; b = 20;

############################

# Olyan függvény, amelynek tetszőleges számú pozícionális és kulcsszó paramétere lehet:

# def func(*args, **kwargs):

# Olyankor lehet hasznos, amikor adott helyen tovább kell adni függvényhívást, mint
# például leszármaztatott osztályból a szülőnek, vagy dekorátoroknál (ld. később).
# Továbbá olyankor, amikor változó számú paraméterrel akarunk dolgozni - pl. az a
# feladat, hogy mindegyiket formázni kell valahogy, vagy az összegüket képezni.

############################

# Nehezíti a tanulást, hogy a hívás helyén is alkalmazhatjuk a * és ** operátorokat.

# Hívásnál *: egy lista vagy tuple kibontása.

def func(*args):
    for e in args:
        print(e, end=' ')
    print()

lst = ['A', 'B']
func(*lst) # A B

# Pontosabban: Nemcsak lista vagy tuple, hanem tetszőleges iterátor, pl.:

func(*range(3)) # 0 1 2

#++++++++++++++++++++

# Hívásnál **: egy dictionary kibontása kulcs-érték párokba.

def func(**kwargs):
    for e in kwargs.items():
        print(e)

dic = {'A': 1, 'B': 2}
func(**dic)
# ('A', 1)
# ('B', 2)

############################
