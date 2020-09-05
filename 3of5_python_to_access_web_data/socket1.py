# Modified from original in https://www.py4e.com/code3.zip according to
# problem12.1.py and for experimentation
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
# counter = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
#    print("pass", counter, data.decode(),end='')
    print(data.decode(),end='')
#    counter += 1
mysock.close()
