from pkg import pkg_globals  # az __init__.py-ban l�v� objektumokra hivatkozni tud

#pkg_globals = {}  # nem sz�p dolog

def func_1():
    print('func_1 pkg_globals:', pkg_globals)
