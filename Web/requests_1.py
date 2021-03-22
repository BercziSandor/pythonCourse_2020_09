# A requests modul get metódusa

# https://www.w3schools.com/tags/ref_httpmethods.asp
# https://realpython.com/python-requests/

import requests

# Sajnos az irodai környezetben nem működik.

url = 'http://szoftverkli.biz/PYTHON_2021_1/2021_1.zip'
proxies = {                         # ez csak az irodai környezetben kell
    'http': 'http://10.196.68.20:3128',
    'https': 'http://10.196.68.20:3128'
}

r = requests.get(url, proxies=proxies)
print(r.status_code)

if r.status_code == 200:
    save_path = 'python_2021_1.zip'
else:
    save_path = 'error.html' # hibaüzenet

file_obj = open(save_path,'wb')
file_obj.write(r.content)  # bytes típusú
file_obj.close()

# A proxy beállításokkal ez a hibaüzenet jön (amit error.html-be mentettünk el):

# Cache Access Denied
# Sorry, you are not currently allowed to request http://szoftverkli.biz/PYTHON_2021_1/2021_1.zip from this cache until you have authenticated yourself.
# Please contact the cache administrator if you have difficulties authenticating yourself.

# Proxy nélkül még eddig sem jut el. A következőkben feltételezzük, hogy mindenki
# futtatni.tud saját környezetből.

######################################################
