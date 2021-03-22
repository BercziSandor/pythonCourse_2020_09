# https://www.w3schools.com/python/python_json.asp
# https://www.youtube.com/watch?v=9N6a-VLBa2I  Python Tutorial: Working with JSON Data using the json Module (Corey Schaefer)
# https://lornajane.net/posts/2013/pretty-printing-json-with-pythons-json-tool
# http://jsoneditoronline.org/   JSON online editor

###################

# JSON: JavaScript Object Notation. Adatcseréhez, konfigurációs fájlokhoz használják,
# a legtöbb nyelvben van illesztő egység hozzá.

# loads: Sztringből beolvasás.

import json

str_1 =  '{"name": "John", "age":30.5, "cities": ["New York", "Budapest"]}'

x = json.loads(str_1)
print(x)  # {'name':'John', 'age':30.5, 'cities': ['New York', 'Budapest']}

# A sztringeknél idézőjelet kell használni, aposztrofot nem fogad el.

str_1 =  '{'name': "John"}'

x = json.loads(str_1) # SyntaxError

# A dict kulcsoknak sztringeknek kell lenniük.
# tuple-t, set-et nem ismer.

###################

# dumps: sztringbe írás.

import json

lst_1 =  ['John', 30.5, ['New York', 'Budapest']]

str_1 = json.dumps(lst_1)
print(str_1, type(str_1))  # ["John", 30.5, ["New York", "Budapest"]] <class 'str'>

###################
