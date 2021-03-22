# SZÁMOK

# Decimális --> hexa

d = 255; h = hex(d)
print(h) # 0xff

# Hexa --> decimális

h = 0xff; d = int(h)
print(d)

#########################################

# KARAKTEREK

# Karakter --> decimális (Unicode kód)

c = 'á'; d = ord(c)
print(d) # 225

# Decimális (Unicode kód) --> karakter

d = 225; c = chr(d)
print(c) # á

# Karakter --> hexa (Unicode kód)

c = 'á'; h = hex(ord(c))
print(h) # 0xe1

# Hexa (Unicode kód) --> karakter

h = 0xe1; c = chr(h)
print(c)

#########################################

# STR, BYTES

# Sztring --> bytes

s = 'áé'; b = s.encode('UTF-8')
print(b) # b'\xc3\xa1\xc3\xa9'

# bytes --> sztring

b = b'\xc3\xa1\xc3\xa9'; s = b.decode('UTF-8')
print(s) # áé

#########################################
