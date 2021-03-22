# Memória-adatbázis, az adatbázis, mint adatszerkezet.
# Egyediség-feltétel, LIKE operátor, indexek

# https://stackoverflow.com/questions/2955121/why-would-someone-need-an-in-memory-database

# Nem akarjuk lemezre menteni az adatbázis tartalmát, csak addig van rá szükség,
# amíg a program fut.

import sqlite3

database = ':memory:'

# AZ ADATBÁZIS-TÁBLA IS EGY ADATSZERKEZET! Az SQL képességeivel kiegészíthetjük a
# Python képességeit.

# Az sqlite (illetve az SQL)

# * Kis helyen tud tárolni adatokat.
# * Indexeket lehet definiálni, miáltal gyorsan lehet
#    + keresni akár
#      - kisbetű-nagybetű érzéketlenül is
#      - több mező szerint is külön-külön
#      - több mező szerint egyszerre
#      - szövegrészre is
#    + rendezni
#    + csoportosítani
#    + táblákat összekapcsolni.

# * Adatkapcsolatokat jól le lehet vele írni.

# * Ellenőrzéseket tud végezni:
#    + típusellenőrzéseket
#    + kitöltöttség-ellenőrzéseket
#    + konzisztencia-ellenőrzéseket.

# A hátrány: ismerni kell az SQL-t is. Viszont ezt nem nehéz megtanulni + nagy része
# szabványos, bár persze van egy csomó adatbázis-specifikus tulajdonság is.

# Az itt leírtak persze nemcsak memória-adatbázisokra igazak, de az hatalmas előny,
# hogy az sqlite memória-adatbázishoz SEMMILYEN külső komponens nem kell.

############################################

# Egyediség-feltétel.

import sqlite3

database = ':memory:'
conn = sqlite3.connect(database)
c = conn.cursor()

cmd = """
CREATE TABLE points (
 x integer NOT NULL,
 y integer NOT NULL,
 value integer,
 UNIQUE (x,y)
);
"""
c.execute(cmd);

cmd = '''INSERT INTO points(x, y, value) VALUES
(1, 1, 100),
(1, 2, 100)
'''
c.execute(cmd)

cmd = 'SELECT * FROM points'
c.execute(cmd)
rows = c.fetchall()
print(rows)  # [(1, 1, 100), (1, 2, 100)]

# Mi történik, ha a UNIQUE feltételt megsértjük?

cmd = 'INSERT INTO points(x, y, value) VALUES (1, 1, 100)' # x = 1, y = 1 már van!
c.execute(cmd)

# Traceback (most recent call last):
#   File "test.py", line 24, in <module>
#     c.execute(cmd)
# sqlite3.IntegrityError: UNIQUE constraint failed: points.x, points.y

#########################################

# Szövegrészre keresés LIKE operátorral.

import sqlite3

database = ':memory:'
conn = sqlite3.connect(database)
c = conn.cursor()

cmd = """
CREATE TABLE t1 (
  f1 TEXT
);
"""
c.execute(cmd)

cmd = "INSERT INTO t1(f1) VALUES ('BUDAPEST'), ('budapest')"
c.execute(cmd)

cmd = "PRAGMA case_sensitive_like=ON" # legyen érzékeny a kisbetű-nagybetűre
c.execute(cmd)

cmd = "SELECT * FROM t1 WHERE f1 LIKE 'BUDA%'"
c.execute(cmd)
rows = c.fetchall()
print(rows) # [('BUDAPEST',)]

cmd = "PRAGMA case_sensitive_like=OFF" # ne legyen érzékeny a kisbetű-nagybetűre
c.execute(cmd)

cmd = "SELECT * FROM t1 WHERE f1 LIKE 'BUDA%'"
c.execute(cmd)
rows = c.fetchall()
print(rows) # [('BUDAPEST',), ('budapest',)]

#########################################

# Ismerkedés az indexekkel.

import sqlite3

database = ':memory:'
conn = sqlite3.connect(database)
c = conn.cursor()

cmd = """
CREATE TABLE people (
  name TEXT,
  city TEXT
);
"""
c.execute(cmd)

cmd = "CREATE INDEX idx_name ON people(name)"
c.execute(cmd)

cmd = '''INSERT INTO people(name, city) VALUES
('János', 'Budapest'), ('John', 'London')
'''
c.execute(cmd)

# Lekérdezés az indexelt mező szerint:

cmd = "SELECT * FROM people WHERE name = 'János'"
c.execute(cmd)
rows = c.fetchall()
print(rows)  # [('János', 'Budapest')]

# A sebességnövekedés persze csak nagy adatmennyiségeknél érzékelhető, mindenesetre
# kérdezzük le a lekérdezés végrehajtási tervét.

cmd = "EXPLAIN QUERY PLAN " + cmd
c.execute(cmd)
rows = c.fetchall()
print(rows) # [(0, 0, 0, 'SEARCH TABLE people USING INDEX idx_name (name=?)')]

# Látszik, hogy használja az indexet.

# Lekérdezés a nem indexelt mező szerint:

cmd = "SELECT * FROM people WHERE city = 'Budapest'"
c.execute(cmd)
rows = c.fetchall()
print(rows) # [('János', 'Budapest')]

cmd = "EXPLAIN QUERY PLAN " + cmd
c.execute(cmd)
rows = c.fetchall()
print(rows) # [(0, 0, 0, 'SCAN TABLE people')]

# Látszik, hogy nem használ indexet.

#########################################
