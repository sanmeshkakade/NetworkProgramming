import socket

# header length
HEADER = 1024
# port
PORT = 9090
# format for encoding and decoding
FORMAT = 'utf-8'
# Address to be connected to
SERVER = "127.0.1.1"
# dis_msg
DISCONNECT_MESSAGE = "!DISCONNECT"
# object for binding
ADDR = (SERVER, PORT)

# creating socket for client
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
# connecting to socket
c.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '* (HEADER - len(send_length))
    c.send(send_length)
    c.send(message)
    print(c.recv(2048).decode(FORMAT))

send("HelloA")
send("HelloB")
send("HelloC")
send(DISCONNECT_MESSAGE)




