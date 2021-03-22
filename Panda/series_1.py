# pandas modul, Series adatszerkezet

# https://www.w3resource.com/pandas/series/series.php
# https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html
# https://www.geeksforgeeks.org/python-pandas-series/

# pandas (PANel DATA): A numpy-ra épít; az adatsorok és oszlopok címkével vannak
# ellátva; jól kezeli a hiányzó adatokat.

import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)

# 0 0.25
# 1 0.50
# 2 0.75
# 3 1.00
# dtype: float64

# Series: egydimenziós indexelt adatsor. Ha külön nem specifikáljuk, akkor az index
# a szokásos 0-val kezdődő egész számokból álló sorozat.

print(data.values, type(data.values)) # [ 0.25, 0.5 , 0.75, 1. ] <class 'numpy.ndarray'>
print(data.index, type(data.index))   # RangeIndex(start=0, stop=4, step=1) <class 'pandas.core.indexes.range.RangeIndex'>

# Az indexelés alapesetben ugyanúgy működik, mint amit megszoktunk:

print(data[1])   # 0.5
print(data[1:3])

# 1    0.50
# 2    0.75
# dtype: float64

# A numpy array, illetve a Python szekvenciális adattípusokhoz képest fontos
# különbség, hogy azokhoz csak egy IMPLICIT index tartozik, ami egyszerűen a tárolás
# sorrendjét tükrözi, itt viszont van egy EXPLICIT módon definiált index IS. Alapesetben
# (a fenti példában) a kétféle index megegyezik; az explicit index defaultja az
# implicit index.

#################################################

# Az index lehet pl. sztringek sorozata:

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
print(data)

# a    0.25
# b    0.50
# c    0.75
# d    1.00
# dtype: float64

# A Series ezért felfogható úgy is, mint egy speciális szótár:

print(data['b']) # 0.5

# Az index lehet akár egy tetszőleges számsorozat is:

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[2, 5, 3, 7])
print(data)

# 2    0.25
# 5    0.50
# 3    0.75
# 7    1.00
# dtype: float64

# Itt nagyon szembeötlő az explicit és implicit index különbsége:

print(data[2]) # 0.25

#################################################

# Több ponton is látni fogjuk, hogy az explicit és az implicit indexelés hasonló,
# de egy kicsit eltérnek egymástól, ami a legrosszabb (könnyű hibázni). Ráadásul
# néha nem könnyű kitalálni, melyik indexelés használódik. Az index típusától is függ,
# hogy adott esetben melyik használódik és a slicing működése függ attól, hogy
# melyiket használjuk. Kész őrület.

# 1. példa:

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[2, 5, 3, 7])

print(data[2])   # 0.25 -- explicit

print(data[1:3]) # -- slice: implicit

# 5    0.50
# 3    0.75
# dtype: float64

# 2. példa:

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
print(data[1])   # 0.5   -- implicit
print(data['a']) # 0.25  -- explicit

print(data[1:3]) # implicit; a lezáró elem nincs benne

b    0.50
c    0.75
dtype: float64

print(data['b':'d']) # explicit, a lezáró elem benne van

# b    0.50
# c    0.75
# d    1.00   !!!!!!
# dtype: float64

# Ezért már most elővesszük azt az indexelési szintaktikát, ami élesen megkülönbözteti,
# hogy éppen melyik fajta indexelést használjuk.

#################################################

# loc attribútum: explicit indexelés.

data = pd.Series(['a', 'b', 'c', 'd'], index=[1, 3, 5, 7])
print(data)

# 1    a
# 3    b
# 5    c
# 7    d
# dtype: object

print(data.loc[1]) # a

print(data.loc[1:3])

# 1    a
# 3    b  !!!!!
# dtype: object

# Explicit indexnél a slice felső határa mindig beleértődik - de így legalább
# tudjuk, hogy biztosan az explicit indexet használjuk.

#################################################

# iloc attribútum: implicit indexelés.

print(data.iloc[1]) # b

print(data.iloc[1:3])

# 3    b
# 5    c
# dtype: object

#################################################

# Célszerű MINDIG a loc és iloc attribútumokat használni!

#################################################
