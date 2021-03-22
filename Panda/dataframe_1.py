# pandas modul, DataFrame adatszerkezet.
# Indexelés, slice, loc, iloc
# DataFrame mint oszlopok szótára és mint két dimenziós tömb

# https://www.w3resource.com/pandas/dataframe/dataframe.php
# https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html
# https://www.geeksforgeeks.org/python-pandas-dataframe/
# https://stackoverflow.com/questions/10715965/add-one-row-to-pandas-dataframe
# https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

# DataFrame: kétdimenziós indexelt adatsor, a sorok és az oszlopok is indexelve vannak.

import pandas as pd

data = {'Person': ['Tom', 'Nick', 'Chris', 'Jack'],
        'Age': [20, 21, 19, 18],
        'Height': [175, 180, 178, 185]
       }

df = pd.DataFrame(data)
print(df)

#   Person  Age  Height
# 0    Tom   20     175
# 1   Nick   21     180
# 2  Chris   19     178
# 3   Jack   18     185

# Nem adtunk meg sorindexet, a default a szokásos, 0-tól kezdődő számsor.

print(df.values, type(df.values))

# [['Tom' 20 175]
#  ['Nick' 21 180]
#  ['Chris' 19 178]
#  ['Jack' 18 185]]

print(type(df.values)) # <class 'numpy.ndarray'>
print(df.index)        # RangeIndex(start=0, stop=4, step=1)
print(df.columns)      # Index(['Person', 'Age', 'Height'], dtype='object')

##############################################################

# Meg tudunk adni explicit módon sorindexet:

data = {'Person': ['Tom', 'Nick', 'Chris', 'Jack'],
        'Age': [20, 21, 19, 18],
        'Height': [175, 180, 178, 185]
       }

df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
print(df)

#   Person  Age  Height
# a    Tom   20     175
# b   Nick   21     180
# c  Chris   19     178
# d   Jack   18     185

print(df.index) # Index(['a', 'b', 'c', 'd'], dtype='object')

# Sokszor törekszünk arra, hogy maga az adat numerikus legyen, a szöveges információk
# a sor- és oszlopindexekbe kerüljenek.

data = {'Age': [20, 21, 19, 18],
        'Height': [175, 180, 178, 185]
       }

df = pd.DataFrame(data, index=['Tom', 'Nick', 'Chris', 'Jack'])
print(df)

#        Age  Height
# Tom     20     175
# Nick    21     180
# Chris   19     178
# Jack    18     185

# Itt feltételeztük, hogy a nevek egyediek, mert célszerű egyedi értékeket használni
# indexként, bár nem kötelező, mint látni fogjuk.

##############################################################

data = {'Person': ['Tom', 'Nick', 'Chris', 'Jack'],
        'Age': [20, 21, 19, 18],
        'Height': [175, 180, 178, 185]
       }

df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
print(df)

#   Person  Age  Height
# a    Tom   20     175
# b   Nick   21     180
# c  Chris   19     178
# d   Jack   18     185

# A szokásos indexelési szintaktikával az OSZLOPOKAT tudjuk megcímezni:

print(df['Age'])

# a    20
# b    21
# c    19
# d    18
# Name: Age, dtype: int64

# Ilyenkor az oszlopokat dictionary-ként kezeljük.

##############################################################

# Sorok elérése: loc vagy iloc attribútummal:

print(df.loc['b'])

# Name      Nick
# Age         21
# Height     180
# Name: b, dtype: object

print(df.iloc[1])

# Name      Nick
# Age         21
# Height     180
# Name: b, dtype: object

##############################################################

# Persze valójában a loc és iloc attribútumok arra valók, hogy az adatokat,
# mint kétdimenziós numpy tömböt megcímezzék.

# Egy elem:

print(df.loc['a','Age']) # 20
print(df.iloc[0,1])      # 20

# Egy sor:

print(df.loc['a'])
# vagy:
print(df.loc['a',:])

# Person    Tom
# Age        20
# Height    175
# Name: a, dtype: object

# Egy oszlop:

print(df.loc[:,'Age'])

# a    20
# b    21
# c    19
# d    18
# Name: Age, dtype: int64

# Az első pozíció nem lehet üres, ez nem jó:

print(df.loc[,'Age']) # SyntaxError

##############################################################

# !!!!!!!!!!

# A slicing loc esetében beleveszi a kijelölt tartományba a felső határt, iloc
# esetében nem - iloc felel meg a megszokott konvenciónak.

print(df.loc['a':'c'])

#   Person  Age  Height
# a    Tom   20     175
# b   Nick   21     180
# c  Chris   19     178  # <-- !!!!!

print(df.iloc[0:2])

#   Person  Age  Height
# a    Tom   20     175
# b   Nick   21     180

print(df.loc['a':'c', 'Person'])

# a      Tom
# b     Nick
# c    Chris             # <-- !!!!!
# Name: Person, dtype: object

print(df.loc['a':'c', 'Person':'Age'])

#            !!
#   Person  Age
# a    Tom   20
# b   Nick   21
# c  Chris   19            # <-- !!!!!
#            !!

print(df.iloc[0:2, 0:1])

#   Person
# a    Tom
# b   Nick

##############################################################

# A DataFrame-hez hozzátehetünk újabb oszlopot, mint egy szótárhoz:

df['Weight'] = [80, 82, 72, 90]
# vagy:
df.loc[:,'Weight'] = [80, 82, 72, 90]

print(df)

#   Person  Age  Height  Weight
# a    Tom   20     175      80
# b   Nick   21     180      82
# c  Chris   19     178      72
# d   Jack   18     185      90

##############################################################

# Új sor hozzáadása:

data = {'Person': ['Tom', 'Nick', 'Chris', 'Jack'],
        'Age': [20, 21, 19, 18],
        'Height': [175, 180, 178, 185]
       }

df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])

df.loc['e'] = ['John', 30, 172]
print(df)

#   Person  Age  Height
# a    Tom   20     175
# b   Nick   21     180
# c  Chris   19     178
# d   Jack   18     185
# e   John   30     172

# iloc segítségével NEM tudunk ugyanígy létrehozni egy új sort:

df.iloc[5] = ['Joe', 27, 190] # IndexError

##############################################################

# Nagyon sokféle adatszerkezetből előállítható közvetlenül DataFrame.
# Például listák listájából is:

data = [['Tom', 'Nick', 'Chris', 'Jack'],
        [20, 21, 19, 18]
       ]

df = pd.DataFrame(data)
print(df)

#      0     1      2     3
# 0  Tom  Nick  Chris  Jack
# 1   20    21     19    18

##############################################################