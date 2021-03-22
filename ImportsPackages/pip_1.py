# pip install, list, freeze, show, uninstall
# pipdeptree modul

# https://packaging.python.org/tutorials/
#   * https://packaging.python.org/tutorials/installing-packages/#use-pip-for-installing
# https://stackoverflow.com/questions/18966564/pip-freeze-vs-pip-list
# https://stackoverflow.com/questions/29751572/how-to-find-a-python-packages-dependencies

# Az irodai hálózatból a Python felhívása előtt  be kell állítani a proxyt:

# SET HTTPS_PROXY=http://10.196.68.20:3128

# Egy modul vagy package installálása: pip install

# [útvonal\]python -m pip install pandas

# Lehet célzottan egy bizonyos verziót is installálni:

# python -m pip install pandas==1.0.5

# A legfrissebb verzióra való frissítés:

# python -m pip install pandas --upgrade

# Összes csomag kilistázása: pip list

# python -m pip list

# numpy (1.19.5)
# pandas (0.25.3)
# pip (9.0.1)
# python-dateutil (2.8.1)
# pytz (2020.5)
# setuptools (28.8.0)
# six (1.15.0)

# Összes csomag kilistázása freeze segítségével:

# python -m pip freeze

# numpy==1.19.5
# pandas==0.25.3
# python-dateutil==2.8.1
# pytz==2020.5
# six==1.15.0

# pip és setuptools ebben nincs benne és a verziómegadás formátuma is más. Célja: requirements
# fájl előállítása, amelynek segítségével máshol installálni tudjuk a csomagokat.

# A fájlt általában requirements.txt-nek szoktuk nevezni, de ez nem kötelező:

# python -m pip freeze > requirements.txt

# Részletes információ egy csomagról: pip show (NEM peep show)

# python -m pip show pandas

# Name: pandas
# Version: 0.25.3
# Summary: Powerful data structures for data analysis, time series, and statistics
# Home-page: http://pandas.pydata.org
# Author: None
# Author-email: None
# License: BSD
# Location: c:\own\itsh\oktat\venv_tst_dir\my_venv\lib\site-packages
# Requires: numpy, python-dateutil, pytz

# Modul (csomag) eltávolítása: pip uninstall

# python -m pip uninstall pandas

# FIGYELEM: Ez nem távolítja el azon modulokat, amelyeket az illető package használ.

# python -m pip list

# numpy==1.19.5
# python-dateutil==2.8.1
# pytz==2020.5
# six==1.15.0

# numpy, pytz, six megmaradt.

# VIGYÁZAT: Olyan csomagot is el tudunk távolítani, amelyet egy másik használ és
# ez csak akkor fog kiderülni, amikor azt a másik csomagot importálni próbáljuk.
# Ha például eltávolítjuk a numpy-t, akkor a pandas használhatatlanná válik.

# Installálás freeze formátumú fájlból:

# python -m pip install -r requirements.txt

###########################################

# A pipdeptree modul fa-struktúrában mutatja a csomagok egymástól való függését.
# Ezt először installálni kell:

# python -m pip install pipdeptree

# A Scripts könyvtárba kerül, a python.exe alá. Használata:

# [python exe útvonal\Scripts\]pipdeptree

# pandas==0.25.3
#   - numpy [required: >=1.13.3, installed: 1.19.5]
#   - python-dateutil [required: >=2.6.1, installed: 2.8.1]
#     - six [required: >=1.5, installed: 1.15.0]
#   - pytz [required: >=2017.2, installed: 2020.5]
# pipdeptree==2.0.0
#   - pip [required: >=6.0.0, installed: 9.0.1]
# setuptools==28.8.0

# Lekérdezhetünk egy csomagot külön:

# pipdeptree -p python-dateutil

# python-dateutil==2.8.1
#   - six [required: >=1.5, installed: 1.15.0]

###########################################
