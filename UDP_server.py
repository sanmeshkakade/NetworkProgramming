import socket
import threading

# port
PORT = 9999
# server
SERVER = socket.gethostbyname(socket.gethostname())
# ADDR
ADDR = (SERVER, PORT)
# dis_msg
DISCONNECT_MESSAGE = "!DISCONNECT"
# header length
BUFFER = 1024
# format for encoding and decoding
FORMAT = 'utf-8'
# confirmation_msg
CONFIRM = "Message Received"

# socket created
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# binding socket
s.bind(ADDR)
print(f"[Server Activated] {s}")

# creating function for listening to socket
while 1:
    data, addr = s.recvfrom(BUFFER)
    print(f"[{addr}] {data.decode(FORMAT)}")
    s.sendto(CONFIRM.encode(FORMAT),addr)
