# Feltételes kifejezések (conditional expression, ternary operator)

# Olyan kifejezés, amelynek az értéke egy feltételtől függ.

# value_if_true if condition else value_if_false

# Feltételes utasítás:

x = 9
if x > 10:
    y = 'nagy'
else:
    y = 'kicsi'

print(y) # kicsi

# Feltételes kifejezés:

y = 'nagy' if x > 10 else 'kicsi'
print(y) # kicsi

# C-ben így nézne ki:

# y = x > 10 ? "nagy" : "kicsi";

# Van, amikor jobban olvasható - de ez szubjektív. Viszont olyan helyeken, ahol csak KIFEJEZÉS
# szerepelhet és UTASÍTÁS nem (if, while, for...) ott erre van szükség.

# Comprehension-ben például. Legyen az a feladat, hogy egy sorozat minden 10-nél kisebb
# elemét helyettesítsünk 0-val:

lst_1 = [1, 2, 11, 20, 3]
lst_2 = [ 0 if e < 10 else e for e in lst_1 ]
print(lst_2) # [0, 0, 11, 20, 0]

# Ha a feltétel teljesül, akkor az else ághoz tartozó kifejezés ugyanúgy nem értékelődik
# ki, mint az if utasításnál. Ezt így tudjuk szemléltetni:

x = 7
y = x if x < 10 else 1 / 0
print(y) # 7
