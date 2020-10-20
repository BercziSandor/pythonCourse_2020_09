# Értékadás slicing segítségével.

lst = [10, 20, 30, 40, 50]

# Az 1, 2, 3 indexű elemeket le akarjuk cserélni erre: [-2, -3, -4]

lst[1:4] = [-2, -3, -4]
print(lst) # [10, -2, -3, -4, 50]

# Az új sorozat lehet más elemszámú, mint az eredeti:

lst = [10, 20, 30, 40, 50]
lst[1:4] = [-100]
print(lst) # [10, -100, 50]

# A felső határ túlcímzése most sem okoz gondot:

lst = [10, 20, 30, 40, 50]
lst[1:100] = [-2, -3, -4]
print(lst) # [10, -2, -3, -4]

# Az új értéksorozat persze tetszőleges iterálható sorozat lehet:

lst = [10, 20, 30, 40, 50]
lst[1:4] = (-2, -3, -4)
print(lst) # [10, -2, -3, -4, 50]

lst = [10, 20, 30, 40, 50]
lst[1:4] = range(5)
print(lst) # [10, 0, 1, 2, 3, 4, 50]

lst = [10, 20, 30, 40, 50]
dic = {'A': 1, 'B': 2}
lst[1:4] = dic.keys()
print(lst) # [10, 'A', 'B', 50] persze a sorrend nem garantált

# Törlés slicing segítségével.

lst = [10, 20, 30, 40, 50]
del(lst[1:4])
print(lst) # [10, 50]

lst = [10, 20, 30, 40, 50]
del(lst[1:100])
print(lst) # [10]
