# Lecture_11\exercises_11.py megoldásai

# 1.)

import numpy as np

def func_with_stat(numbers, func):
    ret_dict = {'status': False, 'ret_val': None, 'exc_type': None,
                'n_total': len(numbers), 'n_nan': None }
    func_ret = None

    try:
        ret_dict['n_nan'] = len(numbers[np.isnan(numbers)])
    except Exception as exc:
        ret_dict['exc_type'] = type(exc)
        return ret_dict

    try:
        func_ret = func(numbers)
    except Exception as exc:
        ret_dict['exc_type'] = type(exc)
    else:
        ret_dict['status'] = True
        ret_dict['ret_val'] = func_ret

    return ret_dict

arr = np.array([10, 20, 30, np.NaN])
ret = func_with_stat(arr, np.nansum)
print(ret) # {'status': True, 'ret_val': 60.0, 'exc_type': None, 'n_total': 4, 'n_nan': 1}

ret = func_with_stat(arr, sum)
print(ret) # {'status': True, 'ret_val': nan, 'exc_type': None, 'n_total': 4, 'n_nan': 1}

arr = np.array([10, 20, 30, None])
ret = func_with_stat(arr, np.nansum)
print(ret) # {'status': False, 'ret_val': None, 'exc_type': <class 'TypeError'>, 'n_total': 4, 'n_nan': None}

############################################

# 2.)

import numpy as np

def nan_decor(funcToBeDecorated):
    def decorated(arr):
        for i in range(len(arr)):
            if arr[i] is None:
                arr[i] = np.NaN

        return funcToBeDecorated(arr)

    return decorated

@nan_decor
def func(param):
    return 2 * param

arr_1 = np.array([10, None, 20, 30])
print(func(arr_1)) # [20, nan, 40, 60]

############################################

# 3.)

class ModuloIter:
    def __init__(self, inputSeries, number):
        self.series = inputSeries
        self.number = number
        self.iter = None

    def __iter__(self):
        self.iter = iter(self.series)
        return self

    def __next__(self):
        while True:
            x = next(self.iter)
            if x % self.number == 0:
                return x

m = ModuloIter(range(19), 6)
for e in m:
    print(e)

# 0
# 6
# 12
# 18

############################################

