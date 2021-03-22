# any() és all() függvények

# Mindkettőnek paraméterként egy iterálható sorozatot kell adni. all() akkor
# ad vissza True értéket, ha a sorozat minden eleme booleanként értelmezve True;
# any() pedig akkor, ha legalább egy eleme True.

lst = [False, False, True]
print(all(lst), any(lst)) # False True

# Pythonban logikailag értelmezve hamisnak számít a nulla numerikus érték, minden
# üres iterálható sorozat és a None (ún. Falsy értékek):

lst = [0, 0.0, None, [], '', set(), dict()]
print(any(lst)) # False

# A többi igaznak számít (Truthy, Trueish):

lst = [-1, [2], '0', {1}, {'a': 1}]
print(all(lst)) # True

# Ezt a két függvényt a numerikus számításokban sűrűn használják, de nem csak ott.

# Egy listában van-e pozitív elem:

lst = [2, -3, -4, 5, 6]
x = any([e > 0 for e in lst])
print(x) # True

x = all([e > 0 for e in lst])
print(x) # False

# Az alábbi példát innen vettem kölcsön (és egy kicsit módosítottam):

# https://realpython.com/any-python/

# Állásra jelentkezők adatait tartjuk nyilván egy listában:

applicants = [
    {
        "name": "Devon Smith",
        "programming_languages": ["c++", "ada"],
        "years_of_experience": 1,
        "has_degree": False,
        "email_address": "devon@email.com",
    },
    {
        "name": "Susan Jones",
        "programming_languages": ["python", "javascript"],
        "years_of_experience": 2,
        "has_degree": False,
        "email_address": "susan@email.com",
    },
    {
        "name": "Sam Hughes",
        "programming_languages": ["java"],
        "years_of_experience": 5,
        "has_degree": True,
        "email_address": "sam@email.com",
    },
    {
        "name": "Jane Perfect",
        "programming_languages": ["java", "c++", "python"],
        "years_of_experience": 10,
        "has_degree": True,
        "email_address": "jane@email.com",
    },
]

# Valamilyen követelményeknek megfelelő jelölteket akarunk kiválasztani a listából.
# Ezt többféleképpen tehetjük meg; itt olyan megoldást tárgyalunk, amely egyszerűen
# paraméterezhetővé teszi a függvényt. Ja és persze alkalmat ad any() és all() bemutatására.

# A követelmény az, hogy az illető ismerje a Pythont (naná), vagy legyen legalább 5 év
# tapasztalata, vagy legyen egyetemi végzettsége.

# A függvény nulladik változata:

def who_to_call_0(applicantSeries):
    ret_lst = []
    for applicant in applicantSeries:
        if "python" in applicant["programming_languages"] or \
        applicant["years_of_experience"] >= 5 or \
        applicant["has_degree"]:
            ret_lst.append(applicant)

    return ret_lst

result = who_to_call_0(applicants)
print([ e['name'] for e in result ]) # ['Susan Jones', 'Sam Hughes', 'Jane Perfect']

# Ez elég egyszerű, nem érdemes más megoldást keresni, de mi most mégis megtesszük
# két okból:

# 1. Ha a kiválasztási követelményrendszer bonyolultabb, akkor a következőkben bemutatandó
#    megoldás már áttekinthetőbb, könnyebben változtatható lehet.
# 2. Az any() és all() függvények bemutatásához pont azért jó ez a példa, mert egyszerű.

######################################

# Egy kis függvényt írunk, amely paraméterként egy jelölt adatait kapja és visszaad egy
# listát, amelyben az egyes szempontoknak való megfelelés szerepel Boolean változóként.

def criteria(applicant):
    lst = ["python" in applicant["programming_languages"],
           applicant["years_of_experience"] >= 5,
           applicant["has_degree"]
          ]

    return lst

# Susan Jones esetében pl. ez az eredmény:

crit_susan = criteria(applicants[1])
print(crit_susan) # [True, False, False]

# Állítsuk elő a kritériumok listáját minden jelentkezőre (NYILVÁN listcomp-pal):

criteria_lst = [ criteria(app) for app in applicants ]

for crit in criteria_lst: print(crit)

# [False, False, False]
# [True, False, False]
# [False, True, True]
# [True, True, True]

# Azokat fogjuk behívni interjúra, akik legalább egy kritériumnak megfelelnek:

meets_lst = [ any(crit) for crit in criteria_lst ]
print(meets_lst) # [False, True, True, True]

# Azok neve, akiket behívunk:

call_for_interview = [ app['name'] for i, app in enumerate(applicants) if meets_lst[i] ]
print(call_for_interview) # ['Susan Jones', 'Sam Hughes', 'Jane Perfect']

######################################

# Ha most azokat keressük, akik mindegyik feltételnek megfelelnek, akkor
# az any() helyett az all() függvényt kell használni:

meets_lst = [ all(crit) for crit in criteria_lst ]
print(meets_lst) # [False, False, False, True]

# A többi változatlan.

print(call_for_interview) # ['Jane Perfect'] (már a neve gyanús volt)

######################################

# Legyen most az az előírás, hogy a jelentkező feleljen meg legalább két követelménynek.
# Írjunk erre egy kis függvényt:

def meets_2(criteria):
    return criteria.count(True) >= 2

meets_lst = [ meets_2(crit) for crit in criteria_lst ]
print(meets_lst) # [False, False, True, True]

# A többi változatlan.

print(call_for_interview) # ['Sam Hughes', 'Jane Perfect']

# Ha valaki nagyon szereti a lambda függvényeket, használhat ilyet is, bár ebben
# az esetben nem biztos, hogy javít az olvashatóságon:

meets_lst = [ (lambda crit: crit.count(True) >= 2)(crit) for crit in criteria_lst ]
print(meets_lst) # [False, False, True, True]

print(call_for_interview) # ['Sam Hughes', 'Jane Perfect']

######################################

# Tegyük bele egy függvénybe az egészet:

def who_to_call(applicantSeries, criteriaFunc, choosingFunc):
    '''
    applicantSeries: iterable of applicant data
    criteriaFunc: creates a list of Booleans for an applicant
    choosingFunc: determines from the list of Booleans whether to choose the applicant
    Returns: list of applicants to be called
    '''

    criteria_lst = [ criteriaFunc(app) for app in applicantSeries ]
    meets_lst = [ choosingFunc(crit) for crit in criteria_lst ]
    call_for_interview = [ app for i, app in enumerate(applicantSeries) if meets_lst[i] ]

    return call_for_interview

# Nyilván az egész struktúrát érdemes visszaadni, nem csak a jelentkező nevét.
# 1. Ha már egy mezőt akarnánk kiválasztani, akkor az inkább az email lenne (a név
#    nem biztos, hogy egyedi).
# 2. Az egész függvénynek NEM kell tudnia, mi van az applicants-ban! Ez benne a szép.

lst = who_to_call(applicants, criteria, any)

from pprint import pprint  # pretty print, hogy ezzel is megismerkedjünk

pprint(lst)

# [{'email_address': 'susan@email.com',
#   'has_degree': False,
#   'name': 'Susan Jones',
#   'programming_languages': ['python', 'javascript'],
#   'years_of_experience': 2},
#  {'email_address': 'sam@email.com',
#   'has_degree': True,
#   'name': 'Sam Hughes',
#   'programming_languages': ['java'],
#   'years_of_experience': 5},
#  {'email_address': 'jane@email.com',
#   'has_degree': True,
#   'name': 'Jane Perfect',
#   'programming_languages': ['java', 'c++', 'python'],
#   'years_of_experience': 10}]

# Vegyük észre, hogy a függvény applicantSeries paramétere TETSZŐLEGES iterálható
# sorozat lehet. Ha holnaptól más adatszerkezetben akarjuk tárolni a jelölteket,
# semmi akadálya, amennyiben a criteriaFunc, choosingFunc függvények passzolnak hozzá.

# Azáltal, hogy függvényeket is át tudunk adni paraméterként, szépen szegmentálható
# az algoritmus. Ha más kritériumokat akarunk támasztani a jelöltekkel szemben, akkor
# csak a criteriaFunc függvényt kell módosítanunk, ha az egyes feltételek súlyozását,
# akkor choosingFunc-ot.

######################################
