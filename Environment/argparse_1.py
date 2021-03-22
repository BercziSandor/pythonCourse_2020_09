# A Python program kapcsolata a környezetével.
# argparse modul

# https://docs.python.org/3.8/howto/argparse.html

# Az argparse segítségével nagyon egyszerűen lehet indítási paramétereket definiálni,
# az ellenőrzéseket és a help összeállítását automatikusan elvégzi.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('x')    # lesz egy kötelező, pozícionális x nevű paraméter,
                            # ami args.x-be kerül be, ha nincs hiba

args = parser.parse_args()  # meg van adva az összes paraméter, megtörténik az ellenőrzés

print('2 * x:', 2 * args.x) # hibás hívásnál ide már el sem fog jutni

# 1. hívás:

# python test.py

# usage: test.py [-h] x
# test.py: error: the following arguments are required: x

# Ezt az üzenetet a sys.stderr kimenetre írja az argparse.

#-----------------------------------

# 2. hívás:

# python test.py 2

# 2 * x: 22

# Azért 22 az eredmény, mert az argparse alapértelmezésben (nyilván) sztringnek
# tekinti a paramétereket.

#-----------------------------------

# 3. hívás: helpet kérünk.

# python.exe test.py -h
# python.exe test.py --help  # így is lehet

# usage: test.py [-h] x
#
# positional arguments:
#   x
#
# optional arguments:
#   -h, --help  show this help message and exit

#########################################

# Adjuk meg a paraméter típusát is.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('x', type=int)
args = parser.parse_args()

print('2 * x:', 2 * args.x) # 2 * x: 4

# python test.py 2

# 2 * x: 4

# A hibás paramétert az argparse visszautasítja:

# python test.py abcd

# usage: test.py [-h] x
# test.py: error: argument x: invalid int value: 'abcd'

#########################################

# Adjunk magyarázó szöveget az x paraméterhez.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('x', type=int, help='négyzetre emeljük')
args = parser.parse_args()

print('2 * x:', 2 * args.x)

# python test.py -h

# usage: test.py [-h] x
#
# positional arguments:
#   x           négyzetre emeljük
#
# optional arguments:
#   -h, --help  show this help message and exit


#########################################

# Csináljunk kötelező kulcsszó paramétert x-ből.
# A kulcsszó paraméterek alapértelmezésben nem kötelezőek, ezért szükség van
# egy required nevű paraméterre az add_argument() hívásban.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-x', type=int, required=True, help='négyzetre emeljük')
args = parser.parse_args()

print('x:', args.x)

# python.exe test.py -x 2

# x: 2

# python.exe test.py

# usage: test.py [-h] -x X
# test.py: error: the following arguments are required: -x

#########################################

# Legyen most az x opcionális; required=True elmarad.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-x', type=int, help='négyzetre emeljük')
args = parser.parse_args()

print('x:', args.x)

# python.exe test.py

# x: None

#########################################

# Adjunk meg x-nek default értéket.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-x', type=int, default=0, help='négyzetre emeljük')
args = parser.parse_args()

print('x:', args.x)

# python.exe test.py

# x: 0

#########################################

# Az argparse modul ezeken kívül még rengeteg lehetőséget kínál.

#########################################
