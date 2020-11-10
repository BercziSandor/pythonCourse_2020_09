# Else ág ciklusoknál: akkor megy rá a vezérlés, ha nem volt break

for i in range(5):
    print(i)
else:
    print('végigment a for ciklus')

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print('no break')

# Üres ciklusnál is működik:

for i in range(5,0):
    print(i)
else:
    print('végigment a for ciklus')
