# Értékadás slicing segítségével.

lst = [10, 20, 30, 40, 50]

# Az 1, 2, 3 indexű elemeket le akarjuk cserélni erre: [-2, -3, -4]

lst[1:4] = [-2, -3, -4]
print(lst) # [10, -2, -3, -4, 50]

#######################################

# Ha slicing segítségével végzünk értékadást, akkor az új elemnek egy iterálható
# sorozatnak kell lennie, amelynek az elemei kerülnek be. Ez tehát NEM működik:

lst = [10, 20, 30, 40, 50]
lst[1:4] = 99 # TypeError: can assign only an iterable

#######################################

# Az új sorozat lehet más elemszámú, mint az eredeti:

lst = [10, 20, 30, 40, 50]
lst[1:4] = [-100]
print(lst) # [10, -100, 50]

# A felső határ túlcímzése most sem okoz gondot:

lst = [10, 20, 30, 40, 50]
lst[1:100] = [-2, -3, -4]
print(lst) # [10, -2, -3, -4]

# Ha a kezdő index túl van a lista végén, akkor az elemek hozzáfűződnek a lista végéhez:

lst = [10, 20, 30, 40, 50]
lst[10:100] = [-2, -3, -4]
print(lst) # [10, 20, 30, 40, 50, -2, -3, -4]

# Ha a kezdő index túl van a lista elején, akkor az elemek hozzáfűződnek a lista
# eleje elé:

lst = [10, 20, 30, 40, 50]
lst[-6:1] = [-2, -3, -4]
print(lst) # [-2, -3, -4, 10, 20, 30, 40, 50]

#######################################

# Nyilván egyetlen elemet is le lehet cserélni:

lst = [10, 20, 30, 40, 50]
lst[1:1] = [99, 100]
print(lst) # [10, 99, 100, 30, 40, 50]

#######################################

# A lista helyben marad megváltozott tartalommal:

lst_1 = [10, 20, 30, 40, 50]
lst_2 = lst_1
lst_1[1:1] = [99, 100]
print(lst_2) # [10, 99, 100, 30, 40, 50]

# Így tudunk tehát helyben új listát létrehozni:

lst_1 = [10, 20, 30, 40, 50]
lst_2 = lst_1
lst_1[:] = [99, 100]
print(lst_2) # [99, 100]

#######################################

# A beillesztendő értéksorozat persze nem csak lista, hanem tetszőleges iterálható
# sorozat lehet:

lst = [10, 20, 30, 40, 50]
lst[1:4] = (-2, -3, -4)
print(lst) # [10, -2, -3, -4, 50]

lst = [10, 20, 30, 40, 50]
lst[1:4] = range(5)
print(lst) # [10, 0, 1, 2, 3, 4, 50]

lst = [10, 20, 30, 40, 50]
dic = {'A': 1, 'B': 2}
lst[1:4] = dic.keys()
print(lst) # [10, 'A', 'B', 50] -- a sorrend 3.6  verzió előtt nem garantált!

#######################################

# Törlés slicing segítségével.

lst = [10, 20, 30, 40, 50]
del(lst[1:4])
print(lst) # [10, 50]

lst = [10, 20, 30, 40, 50]
del(lst[1:100])
print(lst) # [10]

#######################################
