from pkg import pkg_globals  # az __init__.py-ban lévõ objektumokra hivatkozni tud

#pkg_globals = {}  # nem szép dolog

def func_1():
    print('func_1 pkg_globals:', pkg_globals)
