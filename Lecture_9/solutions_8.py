# Lecture_8\exercises_8.py megoldásai

# 1.)

a = a1[a2 == 2 * a1]

####################################

# 2.)

# A.

fname = 'in_1.txt'
f = open(fname, 'r')
lst = []
for i, line in enumerate(f):
    lst.append(str(i + 1) + ' ' + line.rstrip('\n'))

f.close()
print(lst)

# B.

fname = 'in_1.txt'
f = open(fname, 'r')
lst = [str(i + 1) + ' ' + line.rstrip('\n') for i, line in enumerate(f)]
f.close()
print(lst)

####################################

# 3.)

fname_1 = 'in_1.txt'
f_1 = open(fname_1, 'r')

fname_2 = 'in_2.txt'
f_2 = open(fname_2, 'r')

lst = [line_1.strip('\n') + '|' + line_2.strip('\n') for line_1, line_2 in zip(f_1, f_2)]
f_1.close()
f_2.close()

print(lst)

############################################

# 4.)

fname = 'in_1.txt'
f = open(fname, 'r')

dic = {}
for line in f:
    lst = line.split(';')
    if len(lst) < 2: continue

    key = lst[0].strip()
    value = int(lst[1])
    if key not in dic:
        dic[key] = value
    else:
        dic[key] += value

f.close()

print(dic)

############################################

# 5.)

import numpy as np

arr = np.array([
[10, 20, 30, 7],
[12, 9, 17, 22],
[4, 8, 14, 11]
])

names = ['Budapest', 'Debrecen', 'Szolnok']

rows, columns = np.where(arr > 15)

dic = {}
for row, col in zip(rows, columns):
    name = names[row]
    value = arr[row, col]
    if name not in dic:
        dic[name] = [value]
    else:
        dic[name].append(value)

print(dic) # {'Budapest': [20, 30], 'Debrecen': [17, 22]}

# A setdefault metódus segítségével tömörebben is megfogalmazhatjuk:

for row, col in zip(rows, columns):
    name = names[row]
    value = arr[row, col]

    dic.setdefault(name,[]).append(value)

############################################