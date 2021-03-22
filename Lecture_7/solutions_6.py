# Lecture_6\exercises_6.py megoldásai

# 1.

class LimiterClass:
    'klasszikus megoldás (getter-setter)'
    def __init__(self, upperLimit):
        self.__upper_limit = upperLimit
        self.__value = None

    def setValue(self, value, strict=False):
        if value > self.__upper_limit:
            if strict:
                raise ValueError(f'too big value: {value}')
            value = self.__upper_limit
        self.__value = value

    def getValue(self):
        return self.__value

lim_c = LimiterClass(20)
lim_c.setValue(30)
print(lim_c.getValue()) # 20

lim_c.setValue(5)

try:
    lim_c.setValue(40, strict=True)
except ValueError as e:
    print(e)  # toobig value: 40

print(lim_c.getValue()) # 5

# Érdemes megjegyezni, hogy sokkal praktikusabb lenne a strict paramétert az __init__
# metódusnak átadni; az objektum ettől kezdve a kívánt módon működne és nem kellene
# minden setValue hívásnál megadni a működési módot. 

####################################

# 2.)

# A.

def punct_replace_2(inStr, punctChars):
    return [' ' if c in punctChars else c for c in punctChars]

# B.

# Semmit.

# C.

def punct_replace_3(inStr, punctChars):
    ret_lst = [None] * len(inStr)
    for i, c in enumerate(inStr):
        if c in punctChars:
            ret_lst[i] = ' '
        else:
            ret_lst[i] = c

    return ret_lst

punct_chars = set('.,;:?!-')
in_str = 'Van? Vagy, esetleg, nincs.Nem tudom!Lehetséges.'
out_str = ''.join(punct_replace_3(in_str, punct_chars))
print(out_str) # Van  Vagy  esetleg  nincs Nem tudom Lehetséges

# D.

# Lépésekre bontva (olvashatóbb változat):

lst_1 = punct_replace(in_str, punct_chars) # írásjelek lecserélve szóközre
str_1 = ''.join(lst_1)    # sztring, csak szóközökkel, esetleg többel egymás után
lst_2 = str_1.split()     # lista szóközök nélkül
out_str = ' '.join(lst_2) # sztring egyetlen elválasztó szóközzel

print(out_str) # Van Vagy esetleg nincs Nem tudom Lehetséges

# Tömörebb, nehezebben olvasható és egyáltalán nem debuggolható változat:

out_str = ' '.join(''.join(punct_replace(in_str, punct_chars)).split())
print(out_str)# Van Vagy esetleg nincs Nem tudom Lehetséges

####################################

# 3.)

def getStrings_2(inSeries):
    for e in inSeries:
        if isinstance(e, str):
            yield e

in_lst = [1, '2', (20, '30'), {'A': 9}, 'X']
out_lst = list(getStrings_2(in_lst))
print(out_lst) # ['2', 'X']

####################################
