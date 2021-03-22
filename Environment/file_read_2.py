# Sorok beolvasása szöveges fájlból: readline(), readlines() metódusok
# Teljes szövegfájl beolvasása egyszerre: read() metódus

# https://docs.python.org/3.6/tutorial/inputoutput.html#methods-of-file-objects
# https://stackoverflow.com/questions/38105507/when-should-i-ever-use-file-read-or-file-readlines

f_obj = open('input.txt', 'rt')
#contents = f_obj.read()
#print(contents, type(contents), len(contents))

while(True):
    line = f_obj.readline()
    if len(line) == 0: break  # a fájl végét üres sztringgel jelzi

    line = line.rstrip('\n')
    print(line)

f_obj.close()

# line 1
# line 2

# Ez a megoldás a for ciklusossal összehasonlítva bonyolultabb, lassúbb, csak azért
# említődött itt meg, mert találkozhatunk vele.

###############################################

# Ha a teljes fájl sorait egy listában akarjuk elhelyezni, akkor használhatjuk
# a readlines() metódust:

f_obj = open('input.txt', 'rt')
lst = f_obj.readlines()
f_obj.close()

print(lst) # ['line 1\n', 'line 2\n']

# Az lst = list(f_obj) gyorsabb ennél.

###############################################

# Ha a teljes fájlt egyetlen sztringbe akarjuk beolvasni (például mert reguláris
# kifejezésekkel szövegeket fogunk keresni benne), akkor a read metódust használhatjuk.

f_obj = open('input.txt', 'rt')
contents = f_obj.read()
print(contents)

# line 1
# line 2

# Windows alatt a sorvégi CR-LF párok (\r\n) átkonvertálódnak sorvégjelre (\t).

###############################################
