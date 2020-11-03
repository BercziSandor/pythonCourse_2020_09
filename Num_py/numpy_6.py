# Példa reshape alkalmazására

# Egy egy dimenziós tömbben mérési adatokat tárolunk.

src_arr = np.array(
[
10, 20, 12, 21, 9, 17, 15, 28, 11, 23, 14, 20, 13, 19,
11, 19, 14, 23, 8, 16, 17, 26, 12, 24, 15, 22, 15, 20
])

# Minden nap reggel és este mérünk valamit, például levegőszennyezettséget vagy
# debilitásszintet politikusi beszédekben, mindegy is, a lényeg, hogy kétdimenziós
# ábrázolásra lenne szükség. Az adatok jelentése:

[   H   K SZE  CS  P SZO  V
   10  20  12  21  9  17 15  reggel
   28  11  23  14 20  13 19  este
   11  19  14  23  8  16 17  reggel
   26  12  24  15 22  15 20  este
]

# Ennyi adat van:

num_points = src_arr.size
print('összesen:', num_points) # összesen: 28

# Alakítsuk át kétdimenzióssá a tömböt úgy, hogy 7 elem legyen egy sorban:

tgt_arr = src_arr.reshape(int(num_points / 7), -1)

# int(): enélkül float az osztás eredménye és azzal nem lehet indexelni.
# -1: ez azt jelenti, hogy a Numpy fogja kiszámítani.

print(tgt_arr)

# [[10 20 12 21  9 17 15]
#  [28 11 23 14 20 13 19]
#  [11 19 14 23  8 16 17]
#  [26 12 24 15 22 15 20]]

n_rows = tgt_arr.shape[0]
print('sorok száma:', n_rows) # sorok száma: 4
print('napok száma:', int(tgt_arr.shape[0] / 2)) # napok száma: 2

# Vegyük például az összes kedd esti adatot:

print('az összes kedd esti adat:', tgt_arr[1::2, 1]) # az összes kedd esti adat: [11 12]

# tgt_arr[1::2, 1]
#         ^     ^
#      esti     keddi

# A napok szerinti indexelést szebbé tehetjük egy dict-tel:

napok = {'H': 0, 'K': 1, 'SZE': 2, 'CS': 3, 'P': 4, 'SZO': 5, 'V': 6}
kedd_index = napok['K']

print('az összes kedd reggeli adat:', tgt_arr[::2, kedd_index])
# az összes kedd reggeli adat: [20 19]

print('az összes keddi adat:', tgt_arr[:, kedd_index])
# az összes keddi adat: [20 11 19 12]

# Azon indexek, ahol 20-as érték van:

where_20 = np.where(tgt_arr == 20)
print(where_20) # (array([0, 1, 3], dtype=int32), array([1, 4, 6], dtype=int32))

for row, col in zip(where_20[0], where_20[1]):
    print(row, col, tgt_arr[row, col])

# 0 1 20
# 1 4 20
# 3 6 20

#############################
