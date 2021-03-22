# DataFrame beolvasása csv fájlból, display.max_rows,
# head(), notnull(), dropna(), dtypes, astype()
# map függvény alkalmazása oszlopokra

# https://datatofish.com/convert-string-to-float-dataframe/

import numpy as np
import pandas as pd

# Az nba.csv fájl a Data könyvtárban van. Most csak két oszlopot akarunk beolvasni belőle:

df = pd.read_csv('Data/nba.csv', usecols=['Height', 'Weight'])
print('Sorok száma:', df.shape[0]) # 'Sorok száma: 458

# Megnézzük, a print utasítás hatására hány sort fog kiírni:

print(pd.get_option('display.max_rows')) # 60

# Beállítjuk, hogy az összeset írja ki:

pd.set_option('display.max_rows', df.shape[0]+1) # vagy None
print(df)

#     Height  Weight
# 0      6-2   180.0
# 1      6-6   235.0
# 2      6-5   205.0
# 3      6-5   185.0
# 4     6-10   231.0
# 5      6-9   240.0
# 6      6-8   235.0
# ...
# 453    6-3   203.0
# 454    6-1   179.0
# 455    7-3   256.0
# 456    7-0   231.0
# 457    NaN     NaN
#
# [458 rows x 2 columns]

# Az utolsó sor a fájlban
# ,,,,,,,,

# Innen származnak a NaN értékek. A fájl végén sokszor vannak üres, vagy már nem az
# adathoz tartozó sorok. Érdemes erre figyelni.

# Ha csak a DataFrame elejébe akarunk belenézni: head() metódus.

print(df.head())

#   Height  Weight
# 0    6-2   180.0
# 1    6-6   235.0
# 2    6-5   205.0
# 3    6-5   185.0
# 4   6-10   231.0

#################################################

# Eltávolítjuk azokat a sorokat, amelyekben Height vagy Weight NaN, azaz megtartjuk
# azokat, amelyekben mindkettő nem NaN:

df = df[df['Height'].notnull() & df['Weight'].notnull()]
print(df)

#     Height  Weight
# 0      6-2   180.0
# 1      6-6   235.0
# 2      6-5   205.0
# 3      6-5   185.0
# 4     6-10   231.0
# 5      6-9   240.0
# 6      6-8   235.0
# ...
# 451    6-6   206.0
# 452   6-10   234.0
# 453    6-3   203.0
# 454    6-1   179.0
# 455    7-3   256.0
# 456    7-0   231.0
#
# [457 rows x 2 columns]

# Mivel most az ÖSSZES oszlopra előírjuk, hogy nem lehet benne NaN, ezt is írhattuk volna:

df = df.dropna()

print(df.dtypes)

# Height     object
# Weight    float64
# dtype: object

#################################################

# Átszámítjuk cm-re a testmagasságot és kg-ra fontot.

def ft_inch_cm(inStr):
    if not isinstance(inStr, str):  # NaN típusa float
        return(np.NaN)

    arr = [e.strip() for e in inStr.split('-')]
    if len(arr) != 2: return np.NaN

    try:
        feet = int(arr[0])
        inches = int(arr[1])
    except:
        return np.NaN

    if feet < 3 or feet > 10: return np.NaN
    if inches < 0 or inches > 12: return np.NaN

    cm = 30.48 * feet + 2.54 * inches

    return round(cm, 0) # 0 tizedesre kerekítünk

df['Height'] = df['Height'].map(ft_inch_cm)

def pound_kg(inPound):
    try:
        pounds = float(inPound)
        return round(pounds * 0.454, 1)
    except:
        return np.NaN

df['Weight'] = df['Weight'].map(pound_kg)

df = df.dropna() # a konverziónál is keletkezhetett NaN
print(df)

#      Height  Weight
# 0     188.0    81.7
# 1     198.0   106.7
# 2     196.0    93.1
# 3     196.0    84.0
# 4     208.0   104.9
# 5     206.0   109.0
# 6     203.0   106.7
#...
# 451   198.0    93.5
# 452   208.0   106.2
# 453   190.0    92.2
# 454   185.0    81.3
# 455   221.0   116.2
# 456   213.0   104.9
# [457 rows x 2 columns]

print(df.dtypes)

# Height    float64
# Weight    float64
# dtype: object

# float típussá így tudjuk alakítani a sztring formátumban tárolt számokat:

df['Weight'] = df['Weight'].astype(float)

print(df.dtypes)

#################################################

# Minimális, maximális magasság, átlag, medián

print(np.min(df['Height']), np.max(df['Height']))
print(round(np.mean(df['Height']), 2))   # 175.0 221.0
print(round(np.median(df['Height']), 2)) # 201.12 203.0

# Minimális, maximális súly, átlag, medián

print(np.min(df['Weight']), np.max(df['Weight'])) # 73.1 139.4
print(round(np.mean(df['Weight']), 2))   # 100.58
print(round(np.median(df['Weight']), 2)) # 99.9

#################################################

# Ábrázoljuk a súlyt a magasság függvényében:

import matplotlib.pyplot as plt

df.plot(kind = 'scatter', x = 'Height', y = 'Weight')
plt.show()

# Mutassuk a regressziós egyenest is:

df.plot(kind='scatter', x = 'Height', y = 'Weight')

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)
plt.show()

# Nézzük csak a magasságot:

df['Height'].plot()
plt.show()

# A magasságot rendezve:

pd.Series(sorted(df['Height'])).plot()
plt.show()

# (sorted() mindig listát ad vissza, ezt kell Series-é konvertálni.)

# A magasság eltérését az átlagtól:

(df['Height'] - np.mean(df['Height'])).plot()
plt.show()

# A magasság hisztogramját:

df['Height'].plot(kind='hist')
plt.show()

#################################################

# Hozzáteszünk egy oszlopot a magasság és súly hányadosával:

df['H/W'] = round(df['Height'] / df['Weight'], 2)
print(df)

#      Height  Weight   H/W
# 0     188.0   180.0  1.04
# 1     198.0   235.0  0.84
# 2     196.0   205.0  0.96
# 3     196.0   185.0  1.06
# 4     208.0   231.0  0.90
# 5     206.0   240.0  0.86
# 6     203.0   235.0  0.86
# ...
# 451   198.0   206.0  0.96
# 452   208.0   234.0  0.89
# 453   190.0   203.0  0.94
# 454   185.0   179.0  1.03
# 455   221.0   256.0  0.86
# 456   213.0   231.0  0.92
#
# [457 rows x 3 columns]

#################################################
