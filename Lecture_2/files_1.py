# Fájlok olvasása 1.

# Szöveges fájl megnyitása és a sorok beolvasása:

f_obj = open('input.txt','r')

for line in f_obj:
    print(line)

f_obj.close()

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

# Mindig zárjuk be a fájlt használat után!