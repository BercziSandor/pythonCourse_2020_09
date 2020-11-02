# array tuple-ból, dict-ből, delimitált sztringből
# reshape, size

# Tuple a forrás:

tup = (10, 20, 30)
arr_1 = np.array(tup)
print(arr_1) # [10 20 30]

#############################

# Dict:

dic = {'A': 10, 'B': 20, 'C': 30}

arr_1 = np.array([v for v in dic.values()])
print(arr_1) # [10 20 30]

#############################

str_1 = '10; 20; 30'

lst_1 = str_1.split(';')
print(lst_1) # ['10', ' 20', ' 30']

arr_1 = np.array(lst_1).astype(int)
print(arr_1) # [10 20 30]

#############################

# Egy dimenziós tömb --> egy soros két dimenziós tömb:

x = np.array([1, 2, 3])
print(x, x.shape, x.ndim) # [1 2 3] (3,) 1

y = x.reshape((1, 3))
print(y, y.shape, y.ndim) # [[1 2 3]] (1, 3) 2

#############################

# Egy dimenziós tömb --> egy oszlopos két dimenziós tömb:

y = x.reshape((3, 1))
print(y, y.shape, y.ndim)

# [[1]
#  [2]
#  [3]] (3, 1) 2

#############################

# Két soros, három oszlopos tömb --> három soros, két oszlops tömb:

x = np.array([[1, 2, 3], [4, 5, 6]])
print(x, x.shape, x.ndim)

# [[1 2 3]
#  [4 5 6]] (2, 3) 2

y = x.reshape((3, 2))
print(y, y.shape, y.ndim)

# [[1 2]
#  [3 4]
#  [5 6]] (3, 2) 2

#############################

# Két soros, három oszlopos tömb --> egydimenziós tömb:

x = np.array([[1, 2, 3], [4, 5, 6]])
print(x, x.shape, x.ndim)

# [[1 2 3]
#  [4 5 6]] (2, 3) 2

y = x.reshape(x.size)
print(y, y.shape, y.ndim) # [1 2 3 4 5 6] (6,) 1

#############################

#############################


