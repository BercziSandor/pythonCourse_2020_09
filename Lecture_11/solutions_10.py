# Lecture_10\exercises_10.py megoldásai

# 1.)

def limit_decorator(funcToBeDecorated):
    def decorated(*args, **kwargs):
        ret_val = funcToBeDecorated(*args, **kwargs)
        if ret_val > 10:
            ret_val = 10

        return ret_val

    return decorated

@limit_decorator
def func(a, b):
    return a + b

x = func(2, 20)
print(x)  # 10

############################################

# 2.)

def limit_decorator_param(limit):
    def limit_decorator(funcToBeDecorated):
        def decorated(*args, **kwargs):
            ret_val = funcToBeDecorated(*args, **kwargs)
            if ret_val > limit:
                ret_val = limit

            return ret_val

        return decorated

    return limit_decorator

@limit_decorator_param(10)
def func(a, b):
    return a + b

x = func(2, 20)
print(x)  # 10

############################################

# 3.)

def gen_func_1(numbers):
    for num in numbers:
        if num % 6 == 0:
            continue

        yield 3 * num

def gen_func_2(numbers):
    for num in numbers:
        yield num
        yield -num

lst = [10, -1, -12, 2]
g_1 = gen_func_1(lst)
g_2 = gen_func_2(g_1)

for e in g_2:
    print(e, end=' ')
print()

# 30 -30 -3 3 6 -6

############################################

# 4.)

def out_decor(funcToBeDecorated):
    def decorated(param):
        return (param, funcToBeDecorated(param))

    return decorated

@out_decor
def func_1(number):
    return 2 * number

lst = [10, 20, 30, 40]

for e in lst:
    print(func_1(e), end=' ')
print()

# (10, 20) (20, 40) (30, 60) (40, 80)

############################################
