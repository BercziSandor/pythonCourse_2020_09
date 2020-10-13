# Tuple és lista kibontása változókba

x,y = (3,4)
print(x,y) # 3 4

# Listával ugyanígy megy:

x,y = [3,4]
print(x,y) # 3 4

########################

# Elemek összevonása listába

x,*y = (3,4,5,6)
print(x,y)   # 3 [4, 5, 6]

x,*y,z = (3,4,5,6)
print(x,y,z)  # 3 [4, 5] 6

x,*y,z = (3,4,5)
print(x,y,z)  # 3 [4] 5

x,*y,z = (3,4)
print(x,y,z)  # 3 [] 4

# Ez nem megy:

#*x = (3,4,5,6)
#print(x)

######################

# Ismétlés, összehasonlítás: függvény opcionális paraméterei

def func(*args):
    print(len(args), '*args:', *args, 'args[0]:', args[0])

func(3,4,5,6)    # 4 *args: 3 4 5 6 args[0]: 3

tup = (3,4,5,6)
func(tup)        # 1 *args: (3, 4, 5, 6) args[0]: (3, 4, 5, 6)

tup = (3,4,5,6)
func(*tup)       # 4 *args: 3 4 5 6 args[0]: 3
