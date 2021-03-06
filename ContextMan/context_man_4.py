# Saját context manager generátorral és dekorátorral megvalósítva

# Az előző, fájlolvasós példánál maradunk (context_man_2.py), de most generátorral és a
# contextmanager dekorátorral oldjuk meg a feladatot. Az első változatban nem kezeljük
# a kivételeket.

from contextlib import contextmanager

@contextmanager
def MyReader(path):
    print('__enter__ helyett')
    f_obj = open(path)
    yield f_obj
    print('__exit__ helyett')
    f_obj.close()

with MyReader('yyy.txt') as r:
    line = r.readline()
    print('with vége')

print('with után')

# __enter__ helyett
# with vége
# __exit__ helyett
# with után

# A yield előtti rész felel meg __enter__()-nek, az utána lévő rész pedig __exit__()-nek.

###########################################

# Ha a with blokkban keletkező kivételeket el akarjuk kapni:

@contextmanager
def MyReader(path):
    print('__enter__ helyett')
    f_obj = open(path)
    try:
        yield f_obj
    except Exception as e:
        print(e)
    print('__exit__ helyett')
    f_obj.close()

with MyReader('van_ilyen.txt') as r:
    line = r.readline()
    x = 1/0
    print('with vége')

print('with után')

# __enter__ helyett
# division by zero
# __exit__ helyett
# with után

# Persze a kivétel elkapása után tovább is dobhatjuk, vagy dobhatunk egy más típusú kivételt.

###########################################
