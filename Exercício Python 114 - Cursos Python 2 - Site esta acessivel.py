import urllib
import urllib.request
print('-=-'*15)
print(f'{"SITE ACESSIVEL":^45}')
print('-=-'*15)
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
    print('Site acessando normalmente')
except:
    print('Site não acessível')
