import sys
import socket

SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
PORT = 9004
ADDR = (SERVER, PORT)
#BUFFER = 1024
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


def handle_client(c, addr, total_data=0, buffer=""):

    connected = True
    while connected:
        data = c.recv(1024)
        try:
            data = data.decode(FORMAT)
            if data == DISCONNECT_MESSAGE:
                connected = False
                return (total_data, buffer)
            buffer = buffer + data
            total_data += sys.getsizeof(data)

        except Exception as e:
            print(e)


while True :
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(ADDR)
        s.listen(10)
        c, addr = s.accept()
        res = handle_client(c, addr)
        print(f"Total Size of bytes received : {res[0]}\nData received : {res[1]}")
    c.close()

