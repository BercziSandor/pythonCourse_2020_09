# Mi lesz a kimenet? Lehet hibajelzés is.
# NE futtassuk le, mielőtt tippelnénk!

# 1.)

x = (lambda a,b: 2 * a + 3 * b)(2, 3)
print(x) # ??

######################################

#2.)

def func(a,b,c):
    print(a,b,c)

dic = {'a': 1, 'b': 2, 'c': 3}
func(*dic)

######################################

# 3.)

def func(a=1, b=2, c=3):
   print(a,b,c)

dic = {'a': 1, 'b': 2, 'c': 3}
func(**dic)

######################################

# 4.)

def func(a=1, b=2, c=3):
   print(a,b,c)

dic = {'a': 1, 'b': 2}
func(**dic)

######################################

# 5.)

dic = {'a': 1, 'b': 2}
for key, value in dic:
    print(key, value)

######################################

# 5.)

def func():
    y = 1 /0

x = 'ok'
try:
    x = func()
except Exception:
    print(x)

######################################

# 6.)

dishes = ["pizza", "sauerkraut"]
countries = ["Italy", "Germany"]

country_specialities_zip = zip(dishes,countries)
print(list(country_specialities_zip))

country_specialities_dict = dict(country_specialities_zip)
print(country_specialities_dict)

######################################

# 7.)

x = 'This',
print(len(x))

######################################

# 8.)

from statistics import mean

def func():
    val = 1
    while val < 4:
        yield(val)
        val += 1

g = func()
print(mean(g))

######################################

# 9.)

def my_gen():
    print('I am my_gen')
    for i in (50, 60, 70):
        yield 2 * i

print('hello')
g = my_gen()
print('hello again')

######################################
