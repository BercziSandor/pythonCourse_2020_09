# https://www.python-course.eu/python3_abstract_classes.php

# Absztrakt osztályok

# Azt akarjuk, hogy egy osztály leszármazottainak kötelező legyen definiálniuk
# bizonyos metódusokat.

from abc import ABC, abstractmethod

class AbstractBase(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def must_implement(self):
        pass

class Concrete_1(AbstractBase):
    def must_implement(self):
        print('I am Concrete_1')

class Concrete_2(AbstractBase):
    def must_implement(self):
        print('I am Concrete_2')


x = Concrete_1()
y = Concrete_2()

x.must_implement() # I am Concrete_1
y.must_implement() # I am Concrete_2

############################

# Ez nem megy:

class Concrete_3(AbstractBase):
    pass

z = Concrete_3()

# Traceback (most recent call last):
#   File "test.py", line 31, in <module>
#     z = Concrete_3()
# TypeError: Can't instantiate abstract class Concrete_3 with abstract methods must_implement

# Ez azért jó, mert az objektum létrehozásakor már hibajelzést kapunk, nem csak akkor,
# amikor felhívnánk a hiányzó metódust.

############################

# Alkalmazás: Pl. többféle adatbázishoz készítünk interfész-osztályt. Azt akarjuk,
# hogy bizonyos műveletek mindegyiknél definiálva legyenek.

class AbstractDB(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def read(self):
        pass

############################
