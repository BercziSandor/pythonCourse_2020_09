# Kilépés while és for ciklusból: break utasítás

lst = [1, 2, 3, 4, 5, 6]

for e in lst:
    if e > 2:
        break
        
    print(e)

# 10
# 20

# while ciklusban ugyanígy működik.

lst = [1, 2, 3, 4, 5, 6]

# Ciklus folytatása:

for e in lst:
    if e % 3 == 0:
        continue
        
    print(e)

# 1
# 2
# 4
# 5
