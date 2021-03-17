import socket

# port
PORT = 9999
# server
SERVER = "127.0.1.1"
# ADDR
ADDR = (SERVER, PORT)
# dis_msg
DISCONNECT_MESSAGE = "!DISCONNECT"
# header length
BUFFER = 1024
# format for encoding and decoding
FORMAT = 'utf-8'

# Assigning the socket
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send(msg):
    message = msg.encode(FORMAT)
    c.sendto(message, ADDR)
    print(c.recv(2048).decode(FORMAT))


send("Hello from client")

send("2 nd message")


