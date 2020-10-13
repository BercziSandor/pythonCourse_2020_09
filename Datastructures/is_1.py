# is operátor vs == operátor

# x is y akkor True, ha a két változó memóriacíme megegyezik, tehát ugyanarról az
# objektumról van szó. x == y akkor True, ha a két objektum tartalma megegyezik.

# is operátor helyett mindig összehasonlíthatjuk a két objektum memóriacímét (id-jét).

# Első eset: vegyünk két egyforma listát:

lst_1 = [1, 2, 3]
lst_2 = [1, 2, 3]
print(lst_1 == lst_2, lst_1 is lst_2) # True False
print(id(lst_1), id(lst_2))           # 7923752 7984072

# Egyformák, de nem ugyanazok.
# Ha az egyik objektumot megváltoztatjuk, a másik nem fog változni:

lst_1[0] = 9
print(lst_1, lst_2)  # [9, 2, 3] [1, 2, 3]

# lst_1 és lst_2 két cédula, a két lista lakcímét tartalmazza; ezek ketten nem ugyanott laknak.

#######################################

# Második eset: vegyünk egy listát és egy másik változót tegyünk egyenlővé az elsővel:

lst_1 = [1, 2, 3]
lst_2 = lst_1
print(lst_1 == lst_2, lst_1 is lst_2)  # True True
print(id(lst_1), id(lst_2))            # 35383336 35383336

# lst_2 = lst_1 azt jelenti, hogy a két változó ugyanazt a memóriacímet tartalmazza.
# Ha az egyik objektumot megváltoztatjuk, a másik is megváltozik:

lst_1[0] = 9
print(lst_1, lst_2) # [9, 2, 3] [9, 2, 3]

# Most lst_1 és lst_2 ugyanazt a lakcímet tartalmazza.

#######################################

# Az egyenlőség csak akkor teljesül, ha azonos típusú objektumokról van szó.

lst_1 = [1, 2, 3]
tup_1 = (1, 2, 3)
print(lst_1 == tup_1) # False

# list és tuple soha nem egyenlők. Ha egyforma típusúakra konvertáljuk őket,
# akkor persze már megegyezhetnek:

print(lst_1 == list(tup_1))  # True

#######################################

# Immutábilis alaptípusokkal (sztringekkel, számokkal) más a helyzet.
# Ezeknél észleli a fordító, hogy egyformák és csak egyetlen példányt foglal le
# a memóriában. Ebből nem lehet baj, hiszen nem változtatható a memóriatartalom.

x = 'ABC'; y = 'ABC'
print(x is y) # True

x = 10; y = 10
print(x is y) # True

#######################################

# Az, hogy például egy egész szám immutábilis, abból látszik, hogy a += művelet után
# más memóriacímre kerül az eredmény.

x = 5
print(id(x)) # 1577862864
x += 5
print(id(x)) # 1577862944

# Listánál más a helyzet:

x = [1, 2]
print(id(x)) # 31320104

x += [3, 4]
print(id(x)) # 31320104

#######################################
