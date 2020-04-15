import urllib.request, urllib.error, urllib.parse
import json

url = input("Enter the url : ")
fhandle = urllib.request.urlopen(url)

data = fhandle.read().decode()
js = json.loads(data)

ans = 0

commentList = js["comments"]

for comment in commentList:
    ans = ans + comment["count"]

print(ans)