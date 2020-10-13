# Lecture_4\exercises_4.py megoldásai

# 1.

def listofmax_2(*iterables):
    return [ None if len(series) == 0 else max(series) for series in iterables ]

lst_1 = []
tup_2 = [10, 20, 30]
set_3 = {100, 200, 300}

print(listofmax_2(lst_1, tup_2, set_3))
print(listofmax_2())

#####################################

# 2.

# Ez:

print

# nem egy függvényhívás, csak a függvény-objektumból álló kifejezés.

print(print) # <built-in function print>

#####################################

# 3.

employees = [("James", 285000), ("Cecilia", 120000), ("Zach", 48000), ("Ann", 1258000)]

# A.)

# Feltételes kifejezést kell használnunk:

lst = [ (name , salary) if salary < 130000 else (name, 'titkos') for name, salary in employees ]
print(lst) # [('James', 'titkos'), ('Cecilia', 120000), ('Zach', 48000), ('Ann', 'titkos')]

# B.)

lst = list()
for name, salary in employees:
    if salary < 130000:
        lst.append((name, salary))
    else:
        lst.append((name, 'titkos'))

print(lst) # [('James', 'titkos'), ('Cecilia', 120000), ('Zach', 48000), ('Ann', 'titkos')]

#####################################

# 4.

lst_1 = [1, 2, -3]
tup_2 = [10, 20, 30]
set_3 = {100, 200, 300}
lst_empty = []

# A.

def listofsum(*iterables):
    return [ sum(series) if len(series) > 0 else None for series in iterables ]

print(listofsum(lst_1, tup_2, set_3, lst_empty)) # [0, 0, 600, None]
print(listofsum()) []

# B.

def listofsum(*iterables):
    ret_lst = []
    for series in iterables:
        if len(series) > 0:
            ret_lst.append(sum(series))
        else:
            ret_lst.append(None)

    return ret_lst

print(listofsum(lst_1, tup_2, set_3, lst_empty)) # [0, 0, 600, None]
print(listofsum()) []

#####################################

# 5.)

# A.

lst = [ 'abc', 2, 3.5, (4, 5), ['A', 'Z'], -20 ]
num_lst = [ e for e in lst if isinstance(e, (int, float))]

print(num_lst) # [2, 3.5, -20]

# B.

num_lst = []
for e in lst:
  if isinstance(e, (int, float)):
      num_lst.append(e)

print(num_lst) # [2, 3.5, -20]

#####################################

# 6.)

lst = [ 2, 30, 100, 3000, 40000 ]

# A.

num_lst = [ '0' * (4 - len(str(e))) + str(e) for e in lst ]

print(num_lst) # ['0002', '0030', '0100', '3000', '40000']

# B.

num_lst = []
for e in lst:
    e_str = str(e)
    num_lst.append('0' * (4 - len(e_str)) + e_str)

print(num_lst) # ['0002', '0030', '0100', '3000', '40000']

#####################################

# 7.)

# A.

# stupid_func első sorában egy új dict keletkezik egy másik memóriacímen, a
# bemeneti dict-et ettől kezdve senki nem változtatja. A memóriacímek kiíratásával
# világossá válik a dolog:

def stupid_func(param, resultDict):
    print('stupid_func elején resultDict címe:', id(resultDict))
    resultDict = {'status': False, 'result': None}
    print('inicializálás után resultDict címe:', id(resultDict))

    if param < 0:
        return

    resultDict['status'] = True
    resultDict['result'] = 10 * param

    return

# Teszt:

result_dict = {'status': False, 'result': None}
print('hívás előtt result_dict címe:', id(result_dict))
stupid_func(2, result_dict)
print('hívás után result_dict címe:', id(result_dict))

# hívás előtt result_dict címe: 2678976
# stupid_func elején resultDict címe: 2678976
# inicializálás után resultDict címe: 35521520
# hívás után result_dict címe: 2678976

# Híváskor:
# 
# result_dict ----> 2678976 {'status': False, 'result': None}
#                    ^
#                    |
# resultDict  -------+

A függvény első sora után:

# result_dict ----> 2678976  {'status': False, 'result': None}
#
# resultDict  ----> 35521520 {'status': False, 'result': None}

# B.

# Nem új dict-et kell létrehozni, hanem a paraméterként kapottat változtatni.

def stupid_func(param, resultDict):
    resultDict.clear()
    resultDict['status'] = False
    resultDict['result'] = None

    if param < 0:
        return

    resultDict['status'] = True
    resultDict['result'] = 10 * param

    return

# Teszt:

result_dict = {'status': False, 'result': None}
stupid_func(2, result_dict)
print(result_dict) # {'status': True, 'result': 20}

#####################################
