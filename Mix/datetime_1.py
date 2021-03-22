# datetime modul
# datetime, timedelta
# strftime() metódus

# https://www.w3schools.com/python/python_datetime.asp
# https://www.w3resource.com/python/python-date-and-time.php
# https://www.w3resource.com/python-exercises/date-time-exercise/

# Az alap időszak-kezelő modul, vannak fejlettebbek is.

from datetime import datetime

most = datetime.now()
print(most)                            # 2021-02-19 11:27:17.022674
print(most.year, most.month, most.day) # 2021 2 19
print(most.hour, most.minute)          # 11 27
print(most.second, most.microsecond)   # 17 22674

#########################################

# strftime metódus: formázott megjelenítés.

dt_1 = datetime(2021, 2, 19, 9, 12)
print(dt_1.strftime('%Y - %m - %d (%H:%M)')) # 2021 - 02 - 19 (09:12)

#########################################

# timedelta: datetime objektumok különbsége.

from datetime import datetime, timedelta

most = datetime(2021, 2, 19)
tegnap = datetime(2021, 2, 18)
delta = most - tegnap
print(type(delta)) # <class 'datetime.timedelta'>
print(delta)       # 1 day, 0:00:00

print(delta.seconds, delta.total_seconds()) # 0 86400.0

# timedelta.seconds: egy marhaság, az időkülönbségnek van days, seconds, microseconds
# adattagja, ezek EGYÜTT adják meg az időkülönbséget. A különbséget másodpercben
# a total_seconds() metódus adja meg.

#########################################

# A legfontosabb témák:
# * formátumkonverziók
# * aritmetika (időpontok kivonása, stb.)
# * időzónák kezelése

#########################################

