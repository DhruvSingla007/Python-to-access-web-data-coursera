import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter Url: ")
fhandle = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(fhandle,'html.parser')

tags = soup(string= "wikitable sortable jquery-tablesorter")

print(len(tags))