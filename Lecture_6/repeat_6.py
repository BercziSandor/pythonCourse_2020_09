# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# 1.)

# A.
# Mi a kimenet?

lst = [10, 20, 30]
for i, item in zip(range(len(lst)), lst):
    print(i, item) # ??

# B.
# Ez elég csúf megoldás. Írjunk szebbet!

################################################

# 2.)

def func(param):
  if isinstance(x, (list, tuple)):
      return len(param)

  if isinstance(x, (int, float)):
      return  100 * param

  return 42

x = (3)
y = func(x)
print(y)

################################################

# 3.)

def func(*args):
    for arg in *args:
        print(arg)
    print()

func(1,2,3)

################################################

# 4.)

def func(*args):
    for arg in args:
        print(arg)
    print()

func(1,2,3)

lst = [1,2,3]
func(lst)

tup = (1)
func(*tup)

################################################

# 5.)

def func(a,*kwargs):
    print(a)
    for key in kwargs:
        print(key)

func(1,b=2)

################################################

# 6.)

dic_1 = {'A': 1, 'B': 2}
dic_2 = {20: ('Q', 'W'), 30: [4, 5, 6]}
list = list(dic_1.items())
print(list)

list = list(dic_2.values())
print(list)

################################################

# 7.)

lst = [7, 8, 9]

for i in range(len(lst) - 1):
    print(lst[i])

################################################

# 8.)

lst = [7, 8, 9]

for i in range(len(lst)):
    print(lst[i])

# Hogy lehetne szebben ugyanezt?

################################################

# 9.)

class C:
    def __init__(self):
        self.__value = None

    def setValue(self, value):
        self.__value = value

    def getValue(self):
        return self.__value

c_1 = C()
c_1.setValue(10)
x = c_1.getValue()
print(x)

x = C.getValue(c_1)
print(x)

x = c_1.__class__.getValue(c_1)
print(x)

################################################

# 10.)

def func_1(param):
    if param > 10:
        return 0
    else:
        return 2

def func_2(param):
    return 5 * param

x = func_1(20) or func_2(20)
print(x)

################################################
