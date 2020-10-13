# Lecture_2\exercises_2.py megoldásai

# 1.

employees = [("James", 285000), ("Cecilia", 120000), ("Zach", 48000), ("Ann", 1258000)]

e_2 = sorted(employees, key=lambda e: e[1])
print(e_2)

#################################

# 2.

e_2 = sorted([ e[0] for e in employees ], reverse=True)
print(e_2)

# Listcomp nélkül:

e_2 = list()
for e in employees:
    e_2.append(e[0])

e_2 = sorted(e_2, reverse = True)
print(e_2)

#################################

# 3.

is_unique = len({ e[1] for e in employees }) == len(employees)
print(is_unique)

# Listcomp nélkül:

tmp_set = set()
for e in employees:
    tmp_set.add(e[1])

is_unique = len(tmp_set) == len(employees)
print(is_unique)

#################################

# 4.

e_2 = [ e[0] for e in employees if e[1] < 150000 ]
print(e_2)

# Listcomp nélkül:

e_2 = []
for e in employees:
    if e[1] < 150000:
        e_2.append(e[0])

print(e_2)

#################################

# 5.

lst = [ 10, 11, 5, 6, 7, 4 ]
tup = ( 10, 11, 7, 4 )

tup_2 = tuple( e * e for e in lst if e not in tup )
print(tup_2)

#################################

# 6.

f = open('exercise_6.txt')

lst = [len(line.rstrip('\n')) for line in f if 'aaa' in line.lower()]
f.close()

print(lst)

# Listcomp nélkül:
f = open('exercise_6.txt')
lst = []
for line in f:
    if 'aaa' in line.lower():
        lst.append(len(line.rstrip('\n')))
f.close()
print(lst)

#################################
