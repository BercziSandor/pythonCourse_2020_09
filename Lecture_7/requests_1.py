import requests

# sajnos az irodai környezetben nem működik (vagy csak VPN-en?)

url = 'http://szoftverkli.biz/PYTHON_2020_1/python_2020_1.zip'

r = requests.get(url, stream=True)
print(r.status_code)

if r.status_code == 200:
    save_path = 'python_2020_1.zip'
else:
    save_path = 'error.html'

file_obj = open(save_path,'wb')
for chunk in r.iter_content(chunk_size=128):
    file_obj.write(chunk)

file_obj.close()
