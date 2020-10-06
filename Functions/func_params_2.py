# http://www.trytoprogram.com/python-programming/python-function-arguments/
# https://www.python-course.eu/python3_functions.php
# https://www.python-course.eu/python3_passing_arguments.php
# https://note.nkmk.me/en/python-args-kwargs-usage/
# https://data-flair.training/blogs/python-function-arguments/
# https://www.w3resource.com/python/python-user-defined-functions.php

# Dan Bader: Python Tricks - The Book
#  -> Fun With *args and **kwargs

print('Opcionális pozícionális paraméterek')

def func(*args):  # args: egy tuple
    print(args)

func(10,20) # (10, 20)

def func(*args):  # args: egy tuple
    print(len(args), 'paraméter', end='|')
    for arg in args:
        print(arg,end=' ')
    print()

func(10, 20) # 2 paraméter|10 20

# A *args név bármi más is lehet, az args a szokásos.

################################

print('Opcionális kulcsszó paraméterek')

def func(**kwargs):  # kwargs: egy dict
    print(kwargs)

func(a=10,b=20) # {'a': 10, 'b': 20}

# kwargs név is csak konvenció

def func(**kwargs):
    for item in kwargs.items():  # item: key-value tuple
        print(item, end=' ')

    print()

    for item in kwargs.items():  # item: key-value tuple
        print(item[0],'=',item[1], end='; ')

    print()

func(a=10, b=20)

# ('a', 10) ('b', 20)
# a = 10; b = 20;

############################

# Olyan függvény, amelynek tetszőleges számú pozícionális és kulcsszó paramétere lehet:

# def func(*args, **kwargs):

############################

# Olyankor lehet hasznos, amikor adott helyen tovább kell adni függvényhívást, mint
# például leszármaztatott osztályból a szülőnek, vagy dekorátoroknál (ld. később).
# Továbbá olyankor, amikor változó számú paraméterrel akarunk dolgozni - pl. az a
# feladat, hogy mindegyiket formázni kell valahogy, vagy az összegüket képezni.
