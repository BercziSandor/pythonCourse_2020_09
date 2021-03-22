# Lecture_1\exercises_1.py megoldásai

# 1.

def f(upper):
    if upper < 0: upper *= -1

    ret_val = 0
    for x in range(0,upper):
        if x % 3 == 0:
            ret_val += x
    return ret_val

print(f(-4), f(10)) # 3 18

#################################

# 2.

def f(inputList):
    out_lst = []

    for lst in inputList:
        out_lst += lst

    return out_lst

lst = [[1,2,3], [10, 20], [30], [100]]

print(f(lst)) # [1, 2, 3, 10, 20, 30, 100]

# Ez gyorsabb is, mint az eredeti megoldás, mert a belső ciklus a Pythonon belül,
# C-ben megírt részben történik meg.

#################################

# 3.

def f(series_1, series_2):
    len_1 = len(series_1)
    len_2 = len(series_2)
    if len_1 < len_2:
        limit = len_1
    else:
        limit = len_2

    out_lst = []
    for i in range(limit):
        out_lst.append(series_1[i] + series_2[i])

    return out_lst

lst_1 = [1, 2, 3]
lst_2 = [10, 20]

print(f(lst_1,lst_2)) # [11, 22]

#################################
