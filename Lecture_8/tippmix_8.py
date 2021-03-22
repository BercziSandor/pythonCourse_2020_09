# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# 1.)

x = [10, 20]
y = x.append('A')
print(y)

######################################

# 2.)

def func(param):
    x = param * 2
    while len(x):
        yield(x[-1])
        x = x[:-1]

g = func('ab')
for e in g:
    print(e, end=' ')

print()

######################################

# 3.)

lst = [20, 10, 40, 50, 30]
ix = [1, 0, 4, 2, 3]

for i in ix:
    print(lst[i], end=' ')
print()

######################################

# 4.)

dic_1 = {'H': 0, 'K': 1, 'SZE': 2, 'CS': 3, 'P': 4, 'SZO': 5, 'V': 6}

dic_2 = { v: k for k, v in dic_1.items()}
print(dic_2) # ??

# Mikor van értelme?

######################################

# 5.)

# Három sorozatban összetartozó értékek vannak (az azonos indexű elemek
# tartoznak össze).

names = ['John', 'Jane', 'Jill']
grades = (10, 12, 11)
cities = ['London', 'Liverpool', 'Manchester']

# Írassuk ki az összetartozó értékhármasokat. Várt kimenet:

# John 10 London
# Jane 12 Liverpool
# Jill 11 Manchester


for ????:
    print(name, grade, city)

######################################

# 6.)

def func(param):
    if param > 20:
        raise ValueError('big number!')

    if param < 0:
        raise KeyError('small number!')

    if param % 6 == 0:
        raise Exception('ugly number!')

for p in (12, 25, -10):
    try:
        func(p)
    except Exception as e:
        print('ugly?')
    except KeyError as e:
        print('small?')
    except ValueError as e:
        print('big?')
    else:
        print('no exception')

    print('--------------')

######################################

# 7.)

def func(param):
    if param > 20:
        raise ValueError('big number!')

    return 10 * param


for p in (25, 10):
    try:
        ret_val = func(p)
    except ValueError as e:
        print('big?')
    else:
        print('no exception')
    finally:
        print(f'ret_val = {ret_val}')

    print('--------------')

######################################

# 8.)

def func():
    try:
        return(1)
    except:
        return(2)
    else:
        return(3)
    finally:
        return(4)

print(func())

######################################

# 9.)

lst_1 = [10, {'A': 1}, [100]]
lst_2 = lst_1[:]

lst_1[0] = 99
lst_1[1]['A'] = 88

print(lst_2)

######################################

# 10.)

def func():
    for i in range(1,4):
        yield(i)

print(max(func()) - min(func()))

######################################

# 11.)

def func():
    yield(10)
    yield(20)
    yield(30)

g = func()
print(max(g) - sum(g))

######################################

# 12.)

def func(numbers, outList):
    lst = []
    for number in numbers:
        if number % 3 == 0:
            lst.append(number)

        if number % 6 == 0:
            lst.append(number)

    outList = lst

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
func(numbers, result_lst)
print(result_lst)

######################################

# 13.)

lst = [range(i, i + 2) for i in (2, 4, 6)]
print(len(lst), lst)

######################################

# 14.)

lst = [list(range(i, i + 2)) for i in (2, 4, 6)]
print(len(lst), lst)

######################################

# 15.)

import numpy as np

arr = np.array([range(i, i + 2) for i in (2, 4, 6)])
print(arr.shape)
print(arr)

######################################

# 16.)

def f1(par):
    while par < 100:
        yield par
        par *= 2

for x in zip(f1(20), f1(40)):
    print(x)

######################################

# 17.)

lst = [10, 20, 30]
it = iter(lst)

x = next(it)
print(x)
for e in it:
    print(e)

######################################
