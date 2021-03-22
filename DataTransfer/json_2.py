# https://www.kdnuggets.com/2020/09/4-tricks-effectively-use-json-python.html
# https://docs.python.org/3/library/json.html
# https://pynative.com/python-json-encode-unicode-and-non-ascii-characters-as-is/
# https://stackoverflow.com/questions/18337407/saving-utf-8-texts-in-json-dumps-as-utf8-not-as-u-escape-sequence
# https://www.youtube.com/watch?v=1lxrb_ezP-g  How to Write Python Scripts to Analyze JSON APIs and Sort Results (Corey Schaefer)

###################

# A None-t null-nak felelteti meg:

import json

print(json.dumps(None)) # null
x = json.loads('null')
print(x)                # None

# A \ escape-karaktert persze megőrzi:

print("\"foo")  # "foo
print(json.dumps("\"foo"))  # "\"foo"

###################

# Fájlba írás: dump metódussal.

f = open('xxx.txt', 'w')
json.dump([12, {'A': 1, 'B': None}], f)
f.close()

# xxx.txt tartalma:

# [12, {"A": 1, "B": null}]

# Fájlból olvasás: load metódussal.

f = open('xxx.txt', 'r')
x = json.load(f)
f.close()
print(x) # [12, {'A': 1, 'B': None}]

###################
