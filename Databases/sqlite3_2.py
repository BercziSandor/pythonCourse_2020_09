# Memória-adatbázis

# Nem akarjuk lemezre menteni az adatbázis tartalmát, csak addig van rá szükség, amíg
# a program fut.

# https://stackoverflow.com/questions/2955121/why-would-someone-need-an-in-memory-database

# AZ ADATBÁZIS-TÁBLA IS EGY ADATSZERKEZET! Az SQL képességeivel kiegészíthetjük a Python képességeit.

# Az sqlite

# * kis helyen tud tárolni adatokat,
# * gyorsan tud keresgélni köztük,
# * adatkapcsolatokat jól le lehet vele írni,
# * ellenőrzéseket tud végezni:
#   + típusellenőrzéseket
#   + kitöltöttség-ellenőrzéseket
#   + konzisztencia-ellenőrzéseket.

import sqlite3

database = ':memory:'
conn = sqlite3.connect(database)
c = conn.cursor()

cmd = "DROP TABLE IF EXISTS points;"
c.execute(cmd)

cmd = """
CREATE TABLE points (
 x integer NOT NULL,
 y integer NOT NULL,
 value integer,
 UNIQUE (x,y)
);
"""
c.execute(cmd);

cmd = 'INSERT INTO points(x, y, value) VALUES (1, 1, 100)';
c.execute(cmd)

cmd = 'INSERT INTO points(x, y, value) VALUES (1, 2, 100)';
c.execute(cmd)

c.execute('SELECT * FROM points WHERE x = 1 AND y = 2')
row = c.fetchone()
print(row)

#########################################

# Mi történik, ha a UNIQUE feltételt megsértjük?

cmd = 'INSERT INTO points(x, y, value) VALUES (1, 1, 100)';
c.execute(cmd)

# Traceback (most recent call last):
#   File "test.py", line 24, in <module>
#     c.execute(cmd)
# sqlite3.IntegrityError: UNIQUE constraint failed: points.x, points.y

#########################################
