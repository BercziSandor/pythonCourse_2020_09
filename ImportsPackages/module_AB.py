def func_A():
    print('func_A')

def func_B():
    print('func_B, hívom func_A-t')
    func_A()