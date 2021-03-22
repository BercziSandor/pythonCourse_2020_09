# Lecture_9\exercises_9.py megoldásai

# 1.)

import numpy as np

arr_1 = np.array([[10, 22, 21], [35, 14, 40]])
print(arr_1)

# [[10 22 21]
#  [35 14 40]]

ix = np.where(arr_1 % 7 == 0)
arr_1[ix] = arr_1[ix] / 7

print(arr_1)

# [[10 22  3]
#  [ 5  2 40]]

############################################

# 2.)

def reverse_decorator(funcToBeDecorated):
    def decorator(*args, **kwargs):
        ret_val = funcToBeDecorated(*args, **kwargs)

        return ret_val[::-1]

    return decorator

@reverse_decorator
def func_1(p1, p2):
    return p1 + p2

print(func_1('AB', 'CD')) # DCBA

@reverse_decorator
def func_2(p):
    return p.lower()

print(func_2('ABCD')) # dcba

# Fontos: ha numpy array típusú a visszatérő érték, akkor ret_val[::-1] NEM másolat,
# hanem ret_val-ra mutató ún. view.

############################################

# 3.)

def round_deco(funcToBeDecorated):
    def decorated(*args, **kwargs):
        ret_lst = funcToBeDecorated(*args, **kwargs)

        return [ e if abs(e) > 0.01 else 0 for e in ret_lst ]

    return decorated

@round_deco
def f_1():
    return [10, -0.005, 0.2, 3, 0.0004]

print(f_1()) # [10, 0, 0.2, 3, 0]

############################################

# 4.)

def round_deco_param(limit):
    def round_deco(funcToBeDecorated):
        def decorated(*args, **kwargs):
            ret_lst = funcToBeDecorated(*args, **kwargs)

            return [ e if abs(e) > limit else 0 for e in ret_lst ]

        return decorated

    return round_deco

@round_deco_param(0.01)
def f_1():
    return [10, -0.005, 0.2, 3, 0.0004]

print(f_1()) # [10, 0, 0.2, 3, 0]

############################################

# 5.)

def gen_func_1(numbers):
    for num in numbers:
        if num % 6 == 0:
            continue

        yield 3 * num

lst = [10, -1, -12, 2]
g = gen_func_1(lst)
for e in g:
    print(e, end=' ')
print()

# 30 -3 6

############################################

# 6.)

def gen_func_2(numbers):
    for num in numbers:
        yield num
        yield -num

lst = [10, 20, -30]
g = gen_func_2(lst)
for e in g:
    print(e, end=' ')
print()

# 10 -10 20 -20 -30 30

############################################
