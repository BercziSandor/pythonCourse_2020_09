# numpy lineáris algebrai műveletek
# np.linalg.inv, np.allclose, np.linalg.solve

# Mátrix inverze

import numpy as np

arr_1 = np.array([[10, 20], [30, 40]])
print(arr_1)

# [[10 20]
# [ 30 40]]

arr_inv = np.linalg.inv(arr_1) # inverz mátrix
print(arr_inv)

# [[-0.2   0.1 ]
# [ 0.15 -0.05]]

m_mul_1 = arr_1 * arr_inv # elemenkénti szorzás
print(m_mul_1)

# [[-2.   2. ]
#  [ 4.5 -2. ]]

m_mul_2 = np.matmul(arr_1, arr_inv) # mátrixszorzás
print(m_mul_2)

# [[  1.00000000e+00   1.11022302e-16]
#  [  0.00000000e+00   1.00000000e+00]]

expected = np.array([[1, 0], [0, 1]])
all_close = np.allclose(expected, m_mul_2)
print(all_close) # True

#############################

# A linalg modul sok mátrixműveletet tartalmaz, pl. lineáris egyenletrendszert így
# tudunk megoldani:

# 3 * x0 + x1 = 9
# x0 + 2 * x1 = 8

a = np.array([[3,1], [1,2]])
b = np.array([9,8])
x = np.linalg.solve(a, b)
print(x) # [2. 3.]

#############################
