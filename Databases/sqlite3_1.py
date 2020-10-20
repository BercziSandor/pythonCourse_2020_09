# Ismerkedés az sqlite adatbáziskezelővel

# A standard disztribúció része, nem kell semmit installálni.
# Az alábbi példákban nincs hibakezelés az egyszerűség érdekében; valóságos esetekben
# a hibakezelés nagyon fontos.

import sqlite3

database = r"C:\Users\107191088\Oktat\pythonsqlite.db"
conn = sqlite3.connect(database)
c = conn.cursor()

cmd = "DROP TABLE IF EXISTS projects;"
c.execute(cmd)

cmd = """
CREATE TABLE projects (
 id integer PRIMARY KEY,
 name text NOT NULL
);
"""
c.execute(cmd)

cmd = """
INSERT INTO projects(id, name) VALUES (1, 'project 1'), (2, 'project 2');
"""
c.execute(cmd)

c.execute("SELECT * FROM projects")
rows = c.fetchall() # egy listába beolvassa az összes rekordot
print(rows)         # [(1, 'project 1'), (2, 'project 2')]
for row in rows:
    print(row)

# (1, 'project 1')
# (2, 'project 2')

conn.close()

#########################################

# Újból megnyitjuk az adatbázist és olvasni próbálunk a projects táblából.

conn = sqlite3.connect(database)
c = conn.cursor()

c.execute("SELECT * FROM projects")
rows = c.fetchall()
print(rows) # []  üres!

conn.close()

# fetchall() üres listát ad vissza, ha nincs már több beolvasható adat.

# Eltűntek az adatok. Ez azért van így, mert az INSERT után nem zártuk le
# a tranzakciót COMMIT utasítással:

cmd = """
INSERT INTO projects(id, name) VALUES (1, 'project 1'), (2, 'project 2');
"""
c.execute(cmd)
c.execute("COMMIT")

# A másik megoldás, hogy az adatbázis-kapcsolatot autocommit módban hozzuk létre,
# amit a mérsékelten intuitív elnevezésű isolation_level paraméterrel tudunk beállítani:

conn = sqlite3.connect(database, isolation_level=None)
c = conn.cursor()

cmd = "DROP TABLE IF EXISTS projects;"
c.execute(cmd)

cmd = """
CREATE TABLE projects (
 id integer PRIMARY KEY,
 name text NOT NULL
);
"""
c.execute(cmd)

cmd = """
INSERT INTO projects(id, name) VALUES (1, 'project 1'), (2, 'project 2');
"""
c.execute(cmd)

conn.close()

conn = sqlite3.connect(database)
c = conn.cursor()
c.execute("SELECT * FROM projects")
rows = c.fetchall()
print(rows)         # [(1, 'project 1'), (2, 'project 2')]

# A bevitt adatok megmaradnak conn.close() után is.

#########################################

# Ha a beolvasandó tábla nagyon nagy, akkor persze nem jó ötlet egyszerre az egészet
# beolvasni egy listába. Ilyenkor használhatjuk a fechone() metódust, ami None
# visszatérő értékkel jelzi, hogy elfogytak az adatok.

c.execute("SELECT * FROM projects")
while True:
    row = c.fetchone()
    if row is None:
        break
    print(row)

# (1, 'project 1')
# (2, 'project 2')

# Persze ekkor az iterátort más kimerítettük, c.fetchall() üres listát produkál.

#########################################

# a fetchmany metódussal egyszerre több rekordot tudunk lekérdezni:

c.execute("SELECT * FROM projects")
rows = c.fetchmany(10)
print(rows)         # [(1, 'project 1'), (2, 'project 2')]

#########################################
