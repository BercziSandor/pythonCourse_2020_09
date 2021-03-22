# Lecture_13\exercises_13.py megoldásai.

# 1.)

def modIterFunc_2(inputSeries, number):
    for x in inputSeries:
        try:
            if x % number == 0:
                yield x / number
        except TypeError:
            yield x

m = modIterFunc_2([1, 'A', [10, 20], 66., 8, 12, (24, 36)], 6)

for e in m:
    print(e)

# 'A'
# [10, 20]
# 11.0
# 2.0
# (24, 36)

#############################################
