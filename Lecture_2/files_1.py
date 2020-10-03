# F�jlok olvas�sa 1.

# Sz�veges f�jl megnyit�sa �s a sorok beolvas�sa:

f_obj = open('input.txt','r')

for line in f_obj:
    print(line)

f_obj.close()

# line 1
#
# line 2

# A dupla soremel�s az�rt van, mert beolvas�sn�l megmarad a sorv�g-jel �s a
# print hozz�teszi a m�sikat. A sorv�gjeleket �gy tudjuk elt�vol�tani:

for line in f_obj:
    line = line.rstrip('\n')
    print(line)
    
# El�g '\n'-et megadni, mer beolvas�skor a sorv�gjeleket a Python minden oprendszern�l
# egyetlen '\n' (line feed, LF, hexa A) karakterre konvert�lja.

# Ha az �sszes sorv�gi feh�r karaktert le akarjuk v�gni, akkor az rstrip() met�dusnak
# nem adunk semmilyen param�tert.

# Mindig z�rjuk be a f�jlt haszn�lat ut�n!