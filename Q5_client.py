import socket

SERVER = "127.0.1.1"
PORT = 9004
ADDR = (SERVER, PORT)
#BUFFER = 1024
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(ADDR)

while 1:
    s_str = input()
    if s_str!= DISCONNECT_MESSAGE:
        c.send(s_str.encode(FORMAT))
    else:
        c.send(s_str.encode(FORMAT))
        break

c.close()