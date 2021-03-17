import socket
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDR = (SERVER, PORT)
BUFFER =1024
FORMAT = 'utf-8'


def readline_Socket(sock ,BUFFER):
    data, addr = sock.recvfrom(BUFFER)
    line = ""
    lines = 0
    data = data.decode(FORMAT)
    for i in data:
        if i!='\n':
            line+=i
        else:
            lines +=1
            print(f"{lines}, line - {line}")
            line = ""
    print(f"{lines+1}, line - {line}")

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(ADDR)
        readline_Socket(s,BUFFER)
        break
