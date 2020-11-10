# A NULL

import sqlite3

database = ':memory:'
conn = sqlite3.connect(database)
c = conn.cursor()

cmd = """
CREATE TABLE t1 (
 x integer
);
"""
c.execute(cmd);

cmd = 'INSERT INTO t1(x) VALUES (1), (2), (NULL)';
c.execute(cmd)

c.execute('SELECT * FROM t1')
rows = c.fetchall()
for row in rows:
    print(row)

# (1,)
# (2,)
# (None,)

c.execute('SELECT * FROM t1 WHERE x <> 1')
rows = c.fetchall()
for row in rows:
    print(row)

# (2,)

# A NULL minden összehasonlításban NULL (definiálatlan) eredményt ad.
