# -*- coDding: UTF-8 -*-

print("\n###########################")
print("# 1. Alkalmazottak neve és fizetése")

employees = [("James", 285000), ("Cecilia", 120000),
             ("Zach", 48000), ("Ann", 1258000)]
print("\nÁllítsunk elő egy listát a fizetés szerint rendezve.")
print("Bemenet:")
print(employees)

print("Várt eredmény:")
print("[('Zach', 48000), ('Cecilia', 120000), ('James', 285000), ('Ann', 1258000)]")
print("Megoldás:")
print(sorted(employees, key=lambda x: x[1]))

print("\n###########################")
print("# 2. Állítsuk elő a nevek listáját ábécé szerint csökkenő sorrendben.")

print("Várt eredmény:")
print("['Zach', 'James', 'Cecilia', 'Ann']")
print("Megoldás:")
print(list(dict(sorted(employees, key=lambda x: x[0], reverse=True)).keys()))

#NMI A dict-be alakítás felesleges, sőt, gonosz hibát is tud csinálni: a dict-ből kiolvasásnál nincs definiálva a sorrend.

print("\n###########################")
print("# 3. Egy változó értéke legyen True, ha a listában minden fizetés különböző, illetve False, ha van legalább két egyforma fizetés.")
print("Várt eredmény: True.")


def cal3(emp):
    salaries_list = list(dict(emp).values())
    salaries_set = set(dict(emp).values())
    return len(salaries_set) == len(salaries_list)

#NMI Az elgondolás tökéletes; a dict-be alakítás itt is felesleges.

print("Megoldás:")
print(cal3(employees))

print("\n###########################")
print("# 4. Készítsünk egy listát azoknak a nevéből, akiknek a fizetése < 150000.")
print("Várt eredmény:")
print("# ['Cecilia', 'Zach']")


def cal4(emp):
    rv = []
    for key, value in employees:
        if (value < 150000):
            rv.append(key)
    return rv


print("Megoldás:")
print(cal4(employees))


print("\n###########################")
print("# 5. Adott egy lista és egy tuple:")

lst = [10, 11, 5, 6, 7, 4]
tup = (10, 11, 7, 4)
print("# Állítsunk elő egy tuple-t, amely lst azon elemeinek négyzetét tartalmazza, melyek nem fordulnak elő tup-ban.")
print("# Várt eremény:")
print("(25, 36)")


def cal5_1(lst, tup):
    res = []
    for e in set(lst).difference(tup):
        res.append(e*e)
    return tuple(res)

#NMI Jó, csak az ismétlődéseket agyonvágja.

print("Megoldás:")
print(cal5_1(lst, tup))

# Nem fejből. ;)
# NMI Igazi programozó nem dolgozik fejből...

def cal5_2(lst, tup):
    return tuple(filter(None, [element ** 2 if element not in tup else None for element in lst]))

print("Megoldás2:")
print(cal5_2(lst, tup))


print("\n###########################")
print("# 6. Adott az exercise_6.txt fájl. Tegyük bele egy listába mindazon sorok hosszát, amelyekben előfordul")
print("# kisbetű-nagybetű függetlenül az 'aaa' sztring. A hosszban ne legyen benne a sorvégjel.")

print("# Várt eredmény: [10, 22]")
print("[10, 22]")


def cal6(file_name):
    res = []
    f = open(file_name, 'r')
    for l in f:
        l = l.rstrip('\n')
        if ('aaa' in l.lower()):
            res.append(len(l))
    f.close()
    return res

import os
import sys
print(cal6(os.path.dirname(sys.argv[0]) + '/exercise_6.txt'))

print("\n###########################")


