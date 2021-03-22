# Lecture_7\exercises_7.py megoldásai

# 1.)

# A dict-té alakítás felesleges, ráadásul 3.7-es verzió előtt hibás is lehet az eredmény,
# mert a dict-ből kiolvasásnál nincs definiálva a sorrend.

names_reversed = [ e[0] for e in sorted(employees, key=lambda x: x[0], reverse=True)]
print(names_reversed) # ["Zach","James", "Cecilia", "Ann"]

####################################

# 2.)

# A.

# Ha az lst-ben vannak többször előforduló elemek, ezek a kimeneten csak egyszer
# fognak szerepelni:

lst = [10, 11, 5, 6, 7, 4, 6] # 6 kétszer van
tup = (10, 11, 7, 4)

# [25, 36]

# B.

res = [e*e for e in lst if e not in tup]

# [25, 36, 36]

####################################

# 3.)

lines = ['AA BB CC', 'AA EE FF', 'GG HH II']
s_list = ('AA', 'EE', 'XX')

result = find_any(lines, s_list)
print(result) # ['AA BB CC', 'AA EE FF', 'AA EE FF']

# Ha több keresett sztring is előfordul egy sorban, akkor az a sor többször meg
# fog jelenni a kimeneten.

# B.

def find_any(lines, search_list):
    out_lst = []
    for line in lines:
        for searched in search_list:
            if searched in line:
                out_lst. append(line)
                break # ez hiányzott

    return out_lst

####################################

# 4.)

def find_all(lines, search_list):
    out_lst = []
    for line in lines:
        do_it = True
        for searched in search_list:
            if searched not in line:
                do_it = False
                break

        if do_it:
            out_lst.append(line)

    return out_lst

lines = ['AA BB CC', 'AA EE FF', 'GG HH II']
s_list = ('AA', 'EE')

result = find_all(lines, s_list)
print(result)

####################################

# 5.)

def merge_func(series_1, series_2):
    x_1 = None; x_2 = None
    it_1 = iter(series_1)
    it_2 = iter(series_2)
    while True:
        try:
            if x_1 is None:
                x_1 = next(it_1)
        except StopIteration:
            x_1 = None

        try:
            if x_2 is None:
                x_2 = next(it_2)
        except StopIteration:
            x_2 = None

        if x_1 is None and x_2 is None:
            return

        if x_2 is None:
            yield x_1
            x_1 = None
            continue

        if x_1 is None:
            yield x_2
            x_2 = None
            continue

        if x_1 <= x_2:
            yield x_1
            x_1 = None
        else:
            yield x_2
            x_2 = None

lst_1 = [10, 20, 30, 40, 40]
lst_2 = [15, 25, 25, 50]

lst = [x for x in merge_func(lst_1, lst_2)]
print(lst) # [10, 15, 20, 25, 25, 30, 40, 40, 50]

####################################
