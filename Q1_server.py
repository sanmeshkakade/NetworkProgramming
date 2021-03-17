import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5999
ADDR = (SERVER, PORT)
BUFFER = 1024
FORMAT = 'utf-8'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(ADDR)
print(f"[SERVER ACTIVATED] {s}")

while 1:
    data, addr = s.recvfrom(BUFFER)
    data = data.decode(FORMAT)
    data = int(data)
    data = data * data
    data = str(data)
    print(f"Sending to {addr} answer : {data}")
    s.sendto(data.encode(FORMAT),addr)
s.close