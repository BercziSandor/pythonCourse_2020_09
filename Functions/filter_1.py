# filter objektum (filter függvény)
# filter kontra generátor kifejezés
# filter lambda függvénnyel
# filter None-nal, mint függvénnyel

# https://www.w3resource.com/python/built-in-function/filter.php
# https://www.geeksforgeeks.org/filter-in-python/
# https://www.digitalocean.com/community/tutorials/how-to-use-the-python-filter-function
# https://stackoverflow.com/questions/3013449/list-comprehension-vs-lambda-filter
# https://blog.finxter.com/python-lists-filter-vs-list-comprehension-which-is-faster/

##################################################

# A filter objektum egy iterátor, amelynek első paramétere egy logikai értéket visszaadó
# függvény, a második egy iterálható sorozat. A filter azokat az elemeket szolgáltatja,
# amelyeknél a függvény logikai igazat (vagy annak megfelelőt) szolgáltat.

# Szűrjük ki (tartsuk meg) egy sorozatból a kettővel osztható elemeket:

def func(a):
    return a % 2 == 0

lst = [2, 3, 10, 5]
filter_obj = filter(func, lst)
print(list(filter_obj)) # [2, 10]

# Ugyanez generátor kifejezéssel:

gen_exp = (e for e in lst if func(e))
print(list(gen_exp)) # [2, 10]

# A filter objektum mindig helyettesíthető egy generátor kifejezéssel; Guido van Rossum
# el is akarta hagyni a Python 3-as verziójából:

# https://www.artima.com/weblogs/viewpost.jsp?thread=98196

# de aztán akkora volt az ellenállás, hogy megmaradt. Szerintem bizonyos esetekben a
# filter-megoldás olvashatóbb, de ez persze szubjektív. Mindenképpen meg kell ismerkedni
# ezzel az eszközzel, mert találkozhatunk vele Python programokban.

##################################################

# Ha az illető függvény "egylövetű", csak itt van rá szükség, akkor persze lambda
# kifejezést is használhatunk:

filter_obj = filter(lambda a: a % 2 == 0, lst)
print(list(filter_obj)) # [2, 10]

# Ugyanez generátor kifejezéssel:

gen_exp = (e for e in lst if (lambda a: a % 2 == 0)(e))
print(list(gen_exp)) # [2, 10]

##################################################

# Ha a filter objektumnak függvényként None-t adunk át, akkor azokat az elemeket
# távolítja el, amelyek logikailag False-nak felelnek meg.

lst = [1, 0, None, 2, [], {}, 3, '', 0.0, 4]
filter_obj = filter(None, lst)
print(list(filter_obj)) # [1, 2, 3, 4]

# Ugyanez generátor kifejezéssel:

gen_exp = (e for e in lst if e)
print(list(gen_exp)) # [1, 2, 3, 4]

# Én nem szeretem egyik formájában sem ezt a megoldást, mert nehezen tudok elképzelni
# olyan helyzetet, amikor ez a feladat:

# Távolítsunk el ebből a sorozatból minden nullát és üres sorozatot.

# Ha az a feladat, hogy minden nullát távolítsunk el, akkor ezt írjuk le explicit módon:

lst = [1, 0, None, 2, [], {}, 3, '', 0.0, 4]
filter_obj = filter(lambda a: a != 0, lst)
print(list(filter_obj)) # [1, None, 2, [], {}, 3, '', 4]

gen_exp = (e for e in lst if e != 0)
print(list(gen_exp)) # [1, None, 2, [], {}, 3, '', 4]

# Az előző tömör felírási forma csak arra alkalmas, hogy kompakt, rövid, elegáns módon
# tudjunk hülyeséget csinálni.

##################################################
