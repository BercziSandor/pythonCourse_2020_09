# Modulok __name__ attribútuma

# module_3 tartalma:

print('__name__:', __name__)

# Futtassuk le ezt a modult:

# python module_3.py

# A kimenet ez lesz:

# __name__: __main__

################################

# Futtassuk most test.py-t, amelynek tartalma:

import module_3

# python test.py

# A kimenet ez lesz:

# __name__: module_3

# Két dolgot figyelhetünk meg.

# 1. Importáláskor lefut az importált modul.
# 2. A __name__ változóban közvetlen futtatáskor az van, hogy __main__, amikor
#    pedig importálva van a modul neve, akkor a modulnév.

# Az utóbbi tulajdonságot használjuk arra, hogy teszteket úgy építsünk be a modulba,
# hogy azok importáláskor ne fussanak le.

# Futtassuk le a module_4.py modult közvetlenül, illetve futtassunk egy olyan modult,
# amiben csak ennyi van:

import module_4

################################

