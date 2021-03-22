from pkg import pkg_globals  # az __init__.py-ban lévő objektumokra hivatkozni tud

def func_2():
    print('func_2 pkg_globals:', pkg_globals)
