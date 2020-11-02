lst_1 = [10, [100, 200], 'ABC']
lst_2 = lst_1

lst_1[0] = 20
print(lst_2[0]) 

import copy
lst_1 = [10, [100, 200], 'ABC']
lst_2 = vagy lst_1[:] # vagy copy.copy(lst_1)

lst_1[0] = 20
print(lst_2[0]) 

lst_1[1][0] = 99
print(lst_2)

lst_1 = [10, [100, 200], 'ABC']
lst_2 = copy.deepcopy(lst_1)

lst_1[1][0] = 99
print(lst_2)
