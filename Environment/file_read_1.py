# Szöveges fájl megnyitása és a sorok beolvasása iterátor interfésszel.

# https://docs.python.org/3.6/tutorial/inputoutput.html#methods-of-file-objects

f_obj = open('input.txt','rt') # r: read t: text mode

for line in f_obj:
    print(line)

f_obj.close() # Mindig zárjuk be a fájlt használat után!

# line 1
#
# line 2

# A dupla soremelés azért van, mert beolvasásnál megmarad a sorvég-jel és a
# print hozzáteszi a másikat. A sorvégjeleket így tudjuk eltávolítani:

for line in f_obj:
    line = line.rstrip('\n')
    print(line)
    
# Elég '\n'-et megadni, mer beolvasáskor a sorvégjeleket a Python minden oprendszernél
# egyetlen '\n' (line feed, LF, hexa A) karakterre konvertálja.

# Ha az összes sorvégi fehér karaktert le akarjuk vágni, akkor az rstrip() metódusnak
# nem adunk semmilyen paramétert.

###############################################

# Az rt paraméter a default, szöveges fájlok olvasásánál elhagyható:

f_obj = open('input.txt')
f_obj = open('input.txt', 'r')

###############################################

# Ha a fájl sorait egy listába akarjuk tenni minden változtatás nélkül, akkor a
# legegyszerűbb megoldás ez:

f_obj = open('input.txt','rt')
lst = list(f_obj)
f_obj.close()

print(lst) # ['line 1\n', 'line 2\n']

###############################################
