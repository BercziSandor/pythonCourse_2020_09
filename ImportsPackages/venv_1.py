# Virtuális környezetek, venv modul

# https://www.youtube.com/watch?v=APOPm01BVrk
#   * Python Tutorial: VENV (Windows) - How to Use Virtual Environments with the Built-In venv Module (Corey Schaefer)
# https://packaging.python.org/tutorials/
#   * https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments
#   * https://packaging.python.org/tutorials/installing-packages/#use-pip-for-installing

# A venv modul virtuális futtató környezet létrehozására szolgál. A Python 3.3 verziója
# előtt ez nem volt része a standard könyvtárnak, a virtualenv modult kellett importálni.

# Mikor kell venv I.

# Lehet, hogy a Pythonnak csak egyetlen verzióját használjuk, de egyes külső moduloknak,
# (pl. pandas vagy django) az egyik projektben az egyik verzióját, egy másik projektben
# egy másik verzióját akarjuk használni és a két verzió nem kompatibilis.

# Mikor kell venv II.

# Pontosan látni akarjuk, hogy egy projekthez mely modulokra van szükség.

###########################################

# Virtuális környezet létrehozása

# Készítünk egy üres könyvtárat, pl. my_venv néven.

# Lefuttatjuk a venv modult:

# [elérési út\]python.exe -m venv my_venv

# Amely python.exe verzióval ezt a parancsot végrehajtottuk, az fog bemásolódni
# a my_env\Scripts alkönyvtárba egy minimális környezettel együtt.

###########################################

# Virtuális környezet megszüntetése

# Letöröljük a my_env könyvtárat.

###########################################

# Virtuális környezet használata I.: direkt eléréssel

# Készítünk egy futtató batch fájlt, amelyben specifikáljuk ezen python.exe helyét:

my_venv\Scripts\python [modul]
pause

# Vagy: A Notepad++-ban csinálunk egy új Run parancsot, ahol ezen python.exe elérési
# útvonalát adjuk meg.

###########################################

# Virtuális környezet használata II.: aktiválással.

# Nyitunk egy futtató (cmd) ablakot és ezt a parancsot hajtjuk végre:

# my_venv\Scripts\activate.bat

# A prompt megváltozik, az elején megjelenik egy (my_venv) előtag. Ettől kezdve
# az útvonal nélküli python.exe hívás a my_venv könyvtárba másolt programot fogja felhívni.

# Ha még nem akarjuk bezárni a cmd ablakot, de a továbbiakban nem a virtuális környezetet
# akarjuk használni, akkor deaktiváljuk:

# my_venv\Scripts\deactivate.bat

# Figyeljük meg, hogy a prompt elejéről eltűnt a (my_venv).

###########################################

# Nézzük meg, mely modulok (csomagok) állnak rendelkezésre a virtuális környezetben:

python -m pip list

# Csak ezt a két modult fogjuk látni, a verziójukkal együtt:

# pip (9.0.1)
# setuptools (28.8.0)

# Próbáljuk ki, egy test.py fájlba írjuk ezt:

import numpy # ModuleNotFoundError

# és hajtsuk végre a test.py modult.
# numpy tényleg nem áll itt rendelkezésre.

# Installáljuk a numpy modult:

python -m pip install numpy

# Ellenőrizzük:

python -m pip list

# numpy (1.19.5)
# pip (9.0.1)
# setuptools (28.8.0)

# Rájöttünk, hogy a numpy mégsem kell:

python -m pip uninstall numpy

###########################################

# Azon szkripteket, amelyekre később is szükségünk lesz, NE a my_venv könyvtárba
# tegyük, mert azt a könyvtárat tipikusan el szoktuk távolítani, amikor befejeztük
# a kísérletezést.

# Ha gitet használunk, akkor a my_venv könyvtárat érdemes beleírni a .gitignore fájlba,
# nehogy véletlenül belekerüljön a repóba, ezzel feleslegesen növelve annak a méretét.

###########################################
