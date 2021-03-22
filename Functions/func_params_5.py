# A változtatható default paraméterek kelepcéje

def func(param1, lst = []):
    lst.append(param1)

    return lst

lst_1 = func(10)
print(lst_1)  # [10]

lst_2 = func(20)
print(lst_2)  # [10, 20] !!!!!!

# A default paraméter akkor keletkezik, amikor a függvény-objektum keletkezik, NEM
# akkor, amikor felhívódik. Tehát abból 1 darab példány van. Amikor második paraméter
# nélkül hívjuk a függvényt, akkor mindig ugyanazt a default listát használja a futtató
# rendszer, nem mindig egy újat.

############################################

# Helyesen:

def func(param1, lst = None):
    if lst is None:
        lst = []
    lst.append(param1)

    return lst

lst_1 = func(10)
print(lst_1) # [10]

lst_2 = func(20)
print(lst_2) # [20]

############################################

# A probléma persze más változtatható típusoknál is fennáll:

def func(param1, set_ = set()):
    set_.add(param1)

    return set_

set_1 = func(10)
print(set_1)  # {10}

set_2 = func(20)
print(set_2)  # {10, 20} !!!!!

############################################