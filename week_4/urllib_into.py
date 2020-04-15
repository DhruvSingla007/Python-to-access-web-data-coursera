# earlier we have to write this much of code
'''
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data) < 1): break
    print(data.decode())

mysock.close()
'''

# Use of URLlib
import urllib.request, urllib.error, urllib.parse

# it returns the file handle just like reading a local file
fhandle = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')

# printing the data
for line in fhandle:
    line = line.rstrip()
    print(line.decode())