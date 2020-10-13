# Osztályok 1.

# A legegyszerűbb osztály, ami nem csinál semmit:

class MyFirstClass(): pass

my_obj = MyFirstClass
print(my_obj)  # <class '__main__.MyFirstClass'>

# Zárójel nélkül is írható:

class MyFirstClass: pass

# Saját kivétel-osztályként akár ilyen is használható.

###########################

# Legyen egy x nevű attribútuma:

class MySecondClass():
    def __init__(self, xParam):
        self.x = xParam

obj_1 = MySecondClass(42)
obj_2 = MySecondClass(10)
print(obj_1.x, obj_2.x)  # 42 10

# x az objektum attribútuma.

# Az __init__() egy tagfüggvény, más néven metódus. A metódusok első
# paramétere az objektumra mutató változó; a self név csak konvenció.

# __init__()-et a futtató rendszer automatikusan meghívja, ha definiáltuk.

###########################

# Könnyen lehet szemléltetni, hogy a self paraméter magára az objektumra mutat:

class MySecondClass():
    def __init__(self, xParam):
        self.x = xParam
        print('self: ',self)

obj_1 = MySecondClass(42)
print('obj_1:', obj_1)

# self:  <__main__.MySecondClass object at 0x00615510>
# obj_1: <__main__.MySecondClass object at 0x00615510>

###########################

# Pythonban az objektumnak kívülről is lehet utólag attribútumot adni,
# ez nagyon különbözik a C++-tól vagy Java-tól.

class MySecondClass():
    def __init__(self, xParam):
        self.x = xParam

obj_1 = MySecondClass(42)
obj_1.y = 10

print(obj_1.x, obj_1.y)  # 42 10

###########################
