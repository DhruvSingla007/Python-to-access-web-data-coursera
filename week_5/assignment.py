import urllib.request, urllib.parse, urllib.error
import xml.etree.cElementTree as ET

url = input("Enter the url : ")
fhandle = urllib.request.urlopen(url).read()

ans = 0

tree = ET.fromstring(fhandle)
counts = tree.findall('.//count')

for count in counts:
    ans = ans + int(count.text)


print(ans)