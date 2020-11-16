# Class és static metódusok

class Test:
    def bound_method(self):
        print('bound method', self)

    @classmethod
    def class_method(cls):
        print('class method', cls)

    @staticmethod
    def static_method():
        print('static method')

t = Test()
print(t)             # <__main__.Test object at 0x01E27BB0>
t.bound_method()     # bound method <__main__.Test object at 0x01E27BB0>

print(Test)          # <class '__main__.Test'>

t.class_method()     # class method <class '__main__.Test'>
# az objektum ismeri az osztályát

Test.class_method()  # class method <class '__main__.Test'>

Test.static_method() # static method

t.static_method()    # static method
# az objektum ismeri az osztály metódusait

########################################

# class method gyakori felhasználása: gyár (factory) függvény.

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def __str__(self):
        return self.name + "'s age is: " + str(self.age)

person_1 = Person('Adam', 19)
print(person_1)

person_2 = Person.fromBirthYear('John',  1985)
print(person_2)

# https://www.programiz.com/python-programming/methods/built-in/classmethod

########################################
