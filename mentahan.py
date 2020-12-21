
#Import Module
import os
import requests


banner = """
 Welcome To My Tools
  Admin Finder
 Coded By MLX15
"""
os.system('clear')
print banner

#input target
target = raw_input('[Target]> ')

#open wordlist
f=open('wordlist.txt','r')
kontent=f.read()
x=kontent.split('\n')

for i in x:
     url=target+"/"+i
     code=requests.get(str(url)).status_code
     if code == 200:
             print "[+]Berhasil | url : "+url
     else:
             print "[-] Gagal | url:" + url
