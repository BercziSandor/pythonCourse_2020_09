# Státuszjelzés

# 1. módszer: Státusz és eredmény visszatérő értékben.

def doubler(param):
    result_dict = {'result': None, 'status': False, 'reason': None, 'details': ''}
    if param < 0:
        result_dict['reason'] = 'false parameter'
        result_dict['details'] = f'param = {param}'
        return result_dict

    result_dict['result'] = 2 * param
    result_dict['status'] = True
    return result_dict

# Teszt:

ret_dic = doubler(2)
print(ret_dic) # {'result': 4, 'status': True, 'reason': None, 'details': ''}

ret_dic = doubler(-2)
print(ret_dic)  # {'result': None, 'status': False, 'reason': 'false parameter', 'details': 'param = -2'}

# Így használjuk:

for param in (2, -2):
    ret_dic = doubler(param)
    if ret_dic['status']:
        print('sikerült, az eredmény:', ret_dic['result'])
    else:
        print('nem sikerült, az ok:',ret_dic['reason'], 'a részletek:', ret_dic['details'])
        print('Értesítem a felhasználót és logolok')

    print('-----------------')

# sikerült, az eredmény: 4
# -----------------
# nem sikerült, az ok: false parameter a részletek: param = -2
# Értesítem a felhasználót és logolok
# -----------------

# Fontos mindkét dologra gondolni:
# 1. a felhasználó valami számára érthető, rövid üzenetet kap, esetleg több nyelven;
# 2. a logba belekerülnek a technikai részletek is.

##########################

# 2. módszer: státusz paraméterben, eredmény visszatérő értékben.

def doubler(param, statusDict):
    statusDict.clear()
    statusDict['status'] = False
    statusDict['reason'] = None
    statusDict['details'] = ''

    if param < 0:
        statusDict['reason'] = 'false parameter'
        statusDict['details'] = f'param = {param}'
        return None

    statusDict['status'] = True
    return 2 * param

# Teszt:

status_dict = {}
ret_val = doubler(2, status_dict)
print(ret_val, status_dict)  # 4 {'status': True, 'reason': None, 'details': ''}

ret_val = doubler(-2, status_dict)
print(ret_val, status_dict)  # None {'status': False, 'reason': 'false parameter', 'details': 'param = -2'}

# Így használjuk:

for param in (2, -2):
    ret_val = doubler(param, status_dict)
    if status_dict['status']:
        print('sikerült, az eredmény:', ret_val)
    else:
        print('nem sikerült, az ok:',status_dict['reason'], 'a részletek:', status_dict['details'])
        print('Értesítem a felhasználót és logolok')

    print('-----------------')

# sikerült, az eredmény: 4
# -----------------
# nem sikerült, az ok: false parameter a részletek: param = -2
# Értesítem a felhasználót és logolok
# -----------------

##########################

# 3. módszer: státusz és eredmény paraméterben.

def doubler(param, resultDict):
    resultDict.clear()

    resultDict['result'] = None
    resultDict['status'] = False
    resultDict['reason'] = None
    resultDict['details'] = ''

    if param < 0:
        resultDict['reason'] = 'false parameter'
        resultDict['details'] = f'param = {param}'
        return

    resultDict['status'] = True
    resultDict['result'] = 2 * param

# Teszt:

result_dict = {}
doubler(2, result_dict)
print(result_dict)  # {'result': 4, 'status': True, 'reason': None, 'details': ''}

doubler(-2, result_dict)
print(result_dict)  # {'result': None, 'status': False, 'reason': 'false parameter', 'details': 'param = -2'}

# Így használjuk:

for param in (2, -2):
    doubler(param,result_dict)
    if result_dict['status']:
        print('sikerült, az eredmény:', result_dict['result'])
    else:
        print('nem sikerült, az ok:',result_dict['reason'], 'a részletek:', result_dict['details'])
        print('Értesítem a felhasználót és logolok')

    print('-----------------')

# sikerült, az eredmény: 4
# -----------------
# nem sikerült, az ok: false parameter a részletek: param = -2
# Értesítem a felhasználót és logolok
# -----------------

##########################
