import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5999
ADDR = (SERVER, PORT)
BUFFER = 1024
FORMAT = 'utf-8'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)

def handle_client(c, addr):
    while 1:
        r_str = c.recv(BUFFER).decode(FORMAT)
        if r_str:
            print(f"Received from {addr} {r_str}")
            r_str = str(r_str) [::-1]
            print(f"Sending to {addr} {r_str}")
            c.send(r_str.encode(FORMAT))

def start():
    s.listen()
    print(f"[Listening on {ADDR}]")
    while True:
        c, addr = s.accept()
        thread = threading.Thread(target = handle_client, args = (c, addr))
        thread.start()


start()