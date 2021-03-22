# Modulok __name__ attrib�tuma

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

# K�t dolgot figyelhet�nk meg.

# 1. Import�l�skor lefut az import�lt modul.
# 2. A __name__ v�ltoz�ban k�zvetlen futtat�skor az van, hogy __main__, amikor
#    pedig import�lva van a modul neve, akkor a moduln�v.

# Az ut�bbi tulajdons�got haszn�ljuk arra, hogy teszteket �gy �p�ts�nk be a modulba,
# hogy azok import�l�skor ne fussanak le.

# Futtassuk le a module_4.py modult k�zvetlen�l, illetve futtassunk egy olyan modult,
# amiben csak ennyi van:

import module_4

################################

