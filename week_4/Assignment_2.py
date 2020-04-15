
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
position = input('Enter position: ')

i = 0
ans = None

while i < int(count):
    fhandle = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(fhandle, 'html.parser')
    tags = soup('a')
    url = tags[int(position)-1].get('href',None)
    ans = tags[int(position)-1].contents[0]
    i = i+1

print(ans)