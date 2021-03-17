import socket

SERVER = '127.0.1.1'
PORT = 5999
ADDR = (SERVER, PORT)
BUFFER = 1024
FORMAT = 'utf-8'

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
num = input('Enter an integer')
c.sendto(num.encode(FORMAT),ADDR)

ans,addr = c.recvfrom(1024)
print(f"Return Output from {addr} : {ans.decode(FORMAT)}")