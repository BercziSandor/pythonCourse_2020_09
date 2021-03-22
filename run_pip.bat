echo off

: a proxy-beállítás csak a céges hálózatban kell
SET HTTPS_PROXY=http://10.196.68.20:3128
"c:\Users\A107191088\AppData\Local\Programs\Python\Python38-32\python.exe" -m pip install seaborn

pause