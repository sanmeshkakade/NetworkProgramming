import socket

SERVER = "127.0.1.1"
PORT = 5999
ADDR = (SERVER, PORT)
BUFFER = 1024
FORMAT = 'utf-8'

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(ADDR)

s_str = input("Enter an string")

c.send(s_str.encode(FORMAT))
print(f"Received String from {ADDR} : {c.recv(BUFFER).decode(FORMAT)}")