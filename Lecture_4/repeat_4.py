# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# 1.

def f_1(param):
    def inner():
        print(param, x)

    x = 'world'
    inner()
    
f_1('hello')

###################

# 2.

set = {'A', 'B', 'B', 'C'}
print(set)

lst_1 = list(set)
print(lst_1)

print(set(lst_1))

###################

x = 'ABCDEF'
print(x[:-4:])
print(x[:-4:-2])

y_1 = x
y_2 = x[:]
print(y_1 is x, y_2 is x)

lst = list(x)
print(lst)

lst_1 = lst
lst_2 = lst[:]
print(lst_1 is lst, lst_2 is lst)

###################

def f_2(a, b):
    print(str(a) + str(b))
    
f_2(2, 3)

###################

def f_3(*args):
    print(len(args))

f_3(1, 2, 3, 4)
f_3(a=1, b=2)

###################
