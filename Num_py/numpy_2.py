# Mátrix alapműveletek, broadcasting, astype, táblaforgatás

# Azonos formájú mátrixoknál elemenként hajtja végre a műveletet.

arr_1 = np.array([
[10, 20, 30],
[40, 50, 60]
]
)

arr_2 = np.array([
[100, 200, 300],
[400, 500, 600]
]
)

arr = arr_1 + arr_2
print(arr)

# [[110, 220, 330],
# [440, 550, 660]]

#############################

# Ha sokszorozással egyforma alakra lehet hozni a kettőt, akkor ezt teszi (broadcasting):

arr_1 = np.array([
[10, 20, 30],
[40, 50, 60]
]
)

arr = arr_1 * 2
print(arr)

# [[ 20  40  60]
#  [ 80 100 120]]

# 2 ==> [
#       [2, 2, 2],
#       [2, 2, 2]
#       ]

arr = arr_1 + [2,3,4]
print(arr)

# [[12 23 34]
#  [42 53 64]]

# [2,3,4] ==> [
#             [2,3,4]
#             [2,3,4]
#             ]

arr = arr_1 + [
      [2],
      [3]]
print(arr)
# [[12 22 32]
#  [43 53 63]]

# [            [
#  [2],  ==>     [2, 2, 2],
#  [3]           [3, 3, 3]
# ]            ]

#############################

# Típuskonverzió, astype

arr_1 = np.array([10, 20, 30])
arr_2 = np.array([40, 50, '60'])
print(arr_1 + arr_2) # hiba

print(arr_1 + arr_2.astype(int)) # 50 70 90

#############################

# Táblaforgatás: (pivoting): transpose()

arr_1 = np.array([
['col_1','col_2','col_3'],
[5,6,7],
[8,9,10]
])
arr_2 = np.transpose(arr_1)

print(arr_1)
print(arr_2)

# [['col_1' 'col_2' 'col_3']
#  ['5' '6' '7']
#  ['8' '9' '10']]

# [['col_1' '5' '8']
#  ['col_2' '6' '9']
#  ['col_3' '7' '10']]

#############################
