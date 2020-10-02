# 1.

employees = [("James", 285000), ("Cecilia", 120000), ("Zach", 48000), ("Ann", 1258000)]

e_2 = sorted(employees, key=lambda e: e[1])
print(e_2)

#################################

# 2.

e_2 = sorted([ e[0] for e in employees], reverse=True)
print(e_2)

#################################

# 3.

is_unique = len({ e[1] for e in employees }) == len(employees)
print(is_unique)

#################################

# 4.

e_2 = [ e[0] for e in employees if e[1] < 150000 ]
print(e_2)

#################################

# 5.

tup_2 = tuple( e * e for e in lst if e not in tup )
print(tup_2)

#################################

# 6.

f = open('exercise_6.txt')

lst = [len(line.rstrip('\n')) for line in f if 'aaa' in line.lower()]
print(lst)

f.close()

#################################
