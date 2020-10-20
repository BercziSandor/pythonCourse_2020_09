# Lehet saját kivétel-osztályt definiálni, ennek Exception leszármazottjának kell lennie.

class MyException(Exception): pass
# class MyException(ValueError): pass  # így is lehet

def func(param):
    if param > 10:
        raise MyException(f'big parameter: {param}')

    return 2 * param

try:
    x = func(12)
    print(x)
except Exception as e:
    print(e)

# big parameter: 12

#######################################

# Dobhatunk beépített kivételt is. Paramétert
# nem kötelező adni.

def func(param):
    if param > 10:
        raise ValueError(f'big parameter: {param}')
        # raise ValueError

    return 2 * param

try:
    x = func(12)
    print(x)
except Exception as e:
    print(type(e), e)

# <class 'ValueError'> big parameter: 12
# <class 'ValueError'>  ha nem adtunk paramétert

#######################################

# Dobáskor vesszővel elválasztva több paramétert is átadhatunk, ezek
# egy tuple-ba kerülnek bele.

def func(param):
    if param > 10:
        raise ValueError('egy', 2)

    return 2 * param

try:
    x = func(12)
    print(x)
except Exception as e:
    print('e:', e)
    print('e.args típusa:', type(e.args))
    for a in e.args:
        print(a)

# e: ('egy', 2)
# e.args típusa: <class 'tuple'>
# egy
# 2

#######################################

# Különböző adatstruktúrákat is átadhatunk:

def func(param):
    if param > 10:
        raise ValueError({'problem': 'big number', 'details': f'param: {param}'})

    return 2 * param

try:
    x = func(12)
    print(x)
except Exception as e:
    dic = e.args[0]
    for key, value in dic.items():
        print(key, value)

# problem big number
# details param: 12

#######################################

# Külön ágakban kaphatjuk el a különböző típusú kivételeket:

def func(param):
    if param > 10:
        raise ValueError(param)

    if param > 5:
        raise Exception(param)

    return 2 * param

for par in (12, 6):
    try:
        x = func(par)
        print(x)
    except ValueError as e:
        print('ValueErrort kaptam', e)
    except Exception as e:
        print(type(e), e)

# ValueErrort kaptam 12
# <class 'Exception'> 6

# A futtató rendszer az elkapáskor föntről lefelé vizsgálja az except ágakat és az első
# olyant választja, amely a típus megfelel. Megfelel: megegyezik, vagy ebből leszármaztatott
# típus. Exception az összes kivétel-típus őse, ez mindenfajta kivételnél 'megfelel'.

# Vegyük ki most a ValueError ágat:

for par in (12, 6):
    try:
        x = func(par)
        print(x)
#   except ValueError as e:
#       print('ValueErrort kaptam', e)
    except Exception as e:
        print(type(e), e)

# <class 'ValueError'> 12
# <class 'Exception'> 6

# Az Exception mindent elkap.

#######################################

# Cseréljük fel az ágakat:

for par in (12, 6):
    try:
        x = func(par)
        print(x)
    except Exception as e:
        print(type(e), e)
    except ValueError as e:
        print('ValueErrort kaptam', e)

# <class 'ValueError'> 12
# <class 'Exception'> 6

# A ValueError ág soha nem jut szóhoz.

#######################################

# A kivétel típusa információ: a hívónak ezzel is jelezzük, hogy mi történt.
# A részleteket paraméterben átadva lehet elmondani.

#######################################
