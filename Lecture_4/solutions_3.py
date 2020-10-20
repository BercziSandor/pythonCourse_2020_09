# Lecture_3\exercises_3.py megoldásai

# 1.

diff_1_2 = tuple(sorted(set(lst_1) - set(lst_2)))

# Lehet, hogy valakinek így olvashatóbb:

set_diff = set(lst_1) - set(lst_2)
diff_1_2 = tuple(set_diff)

#############################

# 2.

ret_val = titokzatos_func()
print(type(ret_val))

#############################

# 3.
# A.

# Az in operátor azt vizsgálja, hogy egy sorozat tartalmazza-e az első operandust,
# nem azt, hogy annak MINDEN ELEMÉT tartalmazza-e.

# B.

lst_2 = [1, 2, 3]
lst_1 = [1, 2, 3, 4, 5, lst_2]

contains = lst_2 in lst_1  # True

# C.

lst_1 = [1, 2, 3, 4, 5]
lst_2 = [1, 2, 3]

contains = set(lst_2) <= set(lst_1)
print(contains)

#############################

# 4.

def myfunc(inStr):
    return ''.join([ e for e in inStr if e >= '0' and e <='9'])

# Lehet, hogy valakinek így olvashatóbb:

def myfunc(inStr):
    lst = [ e for e in inStr if e >= '0' and e <='9' ]
    return ''.join(lst)

in_str = '  + 36 1/555\t6677\n'
print(myfunc(in_str)) # 3615556677

#############################

# 5.

def listofmax(*iterables):
    return [ max(series) for series in iterables ]

lst_1 = [1, 2, 3]
tup_2 = [10, 20, 30]
set_3 = {100, 200, 300}

print(listofmax(lst_1, tup_2, set_3)) # [3, 30, 300]
print(listofmax())  # []

# A kikötés a nem üres sorozatokra azért szükséges, mert a max() függvény üres
# sorozatnál ValueError kivételt dob.

#############################
