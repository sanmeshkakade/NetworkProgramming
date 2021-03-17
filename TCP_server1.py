import socket
import threading

# Variables
# dis_msg
DISCONNECT_MESSAGE = "!DISCONNECT"
# header length
HEADER = 1024
# port
PORT = 9090
# format for encoding and decoding
FORMAT = 'utf-8'

# server name
SERVER = socket.gethostbyname(socket.gethostname())
# object for binding
ADDR = (SERVER, PORT)

# creating socket for host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
print(f"[SERVER SOCKET] {s} ")
# binding socket
s.bind(ADDR)


# function for handling clients
def handle_client(c, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = c.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = c.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f" [{addr}] {msg}")
            c.send("Msg received".encode(FORMAT))

    c.close


# function for starting socket server
def start():
    s.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # accepting the connection i.e. socket object nd IP- address of connection
        c, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(c, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
