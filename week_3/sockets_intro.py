
# Sockets is the connection between 2 aplications
import socket

# Making a socket. This doesn't connect yet
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to a destination across the internet with a domain name and the port 80 (which usually refers to the web server)
# I will try to make a connection if the port 80 is there and if it doesn't exsist it will fail
mysock.connect(('data.pr4e.org', 80))

# Making the HTTP command  
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

# Sending the HTTP command
mysock.send(cmd)


while True:

    # 512 here refers to the atmost number of characters we want to recieve
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())

# Closing the socket
mysock.close()