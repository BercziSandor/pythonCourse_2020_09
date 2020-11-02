# Lecture_6\exercises_6.py megoldásai

# 1.

class LimiterClass:
    'klasszikus megoldás (getter-setter)'
    def __init__(self, upperLimit):
        self.__upper_limit = upperLimit
        self.__value = None
        self.__x__ = 7

    def setValue(self, value, strict=False):
        if value > self.__upper_limit:
            if strict:
                raise ValueError(f'too big value: {value}')
            value = self.__upper_limit
        self.__value = value

    def getValue(self):
        return self.__value

lim_c = LimiterClass(20)
lim_c.setValue(30)
print(lim_c.getValue()) # 20

lim_c.setValue(5)

try:
    lim_c.setValue(40, strict=True)
except ValueError as e:
    print(e)  # toobig value: 40

print(lim_c.getValue()) # 5

####################################
