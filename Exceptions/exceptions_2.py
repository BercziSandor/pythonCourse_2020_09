# else és finally ág, kivétel továbbdobása

# https://www.youtube.com/watch?v=V2fGAv2R5j8 Mario Corchero - Exceptional Exceptions - How to properly raise, handle and create them.
# https://realpython.com/the-most-diabolical-python-antipattern/

def func(param):
    if param > 10:
        raise OverflowError('big number!!!')

    return 2 * param

for p in (100, 5):
    try:
        ret_val = func(p)
    except Exception as e:
        print(e, type(e))
    else:
        print('no exception')
    finally:
        print('good bye!')  # itt zárjuk be a fájolkat, adatbázist, hálózati kapcsolatot...

    print('--------------')

# big number!!! <class 'OverflowError'>
# good bye!
# --------------
# no exception
# good bye!
--------------

#######################################

def func(param):
    if param > 10:
        raise OverflowError('big number, no big problem')

    param = 1 / param
    return param

file_name = __file__
file_obj = open(file_name)  # majd csinálunk vele valamit

for p in (100, 5, 0):
    try:
        ret_val = func(p)
    except OverflowError as e:
        print('OverflowError, semmi baj')
    except Exception as e:
        marker = 'xxx_01'
        msg = f'marker: {marker} file_name: {file_name}'
        print('Nagy baj! Logfájlba írom ezt:', msg)
        print('és továbbdobom')
        raise
    else:
        print('no exception')
    finally:
        file_obj.close()  # a rend kedvéért

    print('--------------')

# OverflowError, semmi baj
# --------------
# no exception
# --------------
# Nagy baj! Logfájlba írom ezt: marker: xxx_01 file_name: test.py
# és továbbdobom
#
# Traceback (most recent call last):
#   File "test.py", line 13, in <module>
#     ret_val = func(p)
#   File "test.py", line 5, in func
#     param = 1 / param
# ZeroDivisionError: division by zero

# El kell dönteni, hogy a hibáról szóló információt továbbdobjuk-e,
# logoljuk-e, illetve mi az, amit továbbdobunk és mi az amit logolunk.

# A marker arra lehet jó, hogy azonosítani tudjuk a hívás helyét a logból (lehet,
# hogy nagyon sok helyről hívódik a függvény).

# A fájlnévvel csak azt akartam mutatni, hogy a hívás helyén lehetnek olyan paraméterek,
# amelyeket a meghívott függvény nem ismer és amelyek segíthetnek a hibakeresésben.

#######################################
