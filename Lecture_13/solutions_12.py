# Lecture_12\exercises_12.py megoldásai.

# 1.)

def limit_decor(funcToBeDecorated):
    def decorated(*args, **kwargs):
        ret_lst = funcToBeDecorated(*args, **kwargs)

        for e in ret_lst:
            if e > 50: raise ValueError('túl nagy! ' + str(e) + ' > 50')

        return ret_lst

    return decorated

@limit_decor
def func(param):
    return [2 * e for e in param]

try:
    lst = None
    lst = func([10, 20, 30])
except ValueError as ex:
    print(ex) # túl nagy! 60 > 50

#############################################

# 2.)

def limit_decor_param(limit):
    def limit_decor(funcToBeDecorated):
        def decorated(*args, **kwargs):
            ret_lst = funcToBeDecorated(*args, **kwargs)

            for e in ret_lst:
                if e > limit: raise ValueError(f'túl nagy! {e} > {limit}')

            return ret_lst

        return decorated

    return limit_decor

@limit_decor_param(55)
def func(param):
    return [2 * e for e in param]

try:
    lst = None
    lst = func([10, 20, 30])
except ValueError as ex:
    print(ex)  # túl nagy! 60 > 55

#############################################

# 3.)

def modIterFunc(inputSeries, number):
    for x in inputSeries:
        if x % number == 0:
            yield x
            
m = modIterFunc(range(19), 6)

for e in m:
    print(e)

# 0
# 6
# 12
# 18


#############################################

