# 1.)

# Írjunk függvényt, amelynek egy paramétere van. A visszatérő érték: azon
# számok összege, amelyek 0 és a paraméter közé esnek és hárommal oszthatók.
# Ha a paraméter negatív, akkor vegye a függvény a -1-szeresét.

print(f(-4), f(10)) # 3 18

######################################

# 2.)

# Írjunk függvényt, amely paraméterként olyan listát kap, amelynek minden eleme egy lista
# A visszatérő érték legyen egy olyan lista, amely az összes elemet tartalmazza.

lst = [[1,2,3], [10, 20], [30], [100]]

print(f(lst)) # [1, 2, 3, 10, 20, 30, 100]

# A következő megoldás jó eredményt szolgáltat:

def f(inputList):
    out_lst = []
    for lst in inputList:
        for elem in lst:
            out_lst.append(elem)
    return out_lst

# Hogy lehetne egyszerűsíteni?

######################################

# 3.)

# Írjunk függvényt, amely paraméterként számokat tartalmazó két listát vagy tuple-t kap;
# a visszatérő értéke egy lista, amelynek a hossza a rövidebbik paraméter-lista hossza és
# az elemei: az azonos indexű elemek összege.

lst_1 = [1, 2, 3]
lst_2 = [10, 20]

print(f(lst_1,lst_2)) # [11, 22]

######################################
