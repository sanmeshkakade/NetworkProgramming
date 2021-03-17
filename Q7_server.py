import socket
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDR = (SERVER, PORT)
BUFFER =1024
FORMAT = 'utf-8'


def CRLFreadline(sock ,BUFFER):
    data, addr = sock.recvfrom(BUFFER)
    line = ""
    lines = 0
    data = data.decode(FORMAT)
    i=0
    while i < len(data):
        if data[i]=='\n':
            line += 1
            print(f"{lines} line - {line}")
            line = ""
        elif data[i]=='\r' and data[i+1]=='\n':
            i += 1
            line += 1
            print(f"{lines} line - {line}")
            line = ""
        else:
            line += data[i]
        i += 1
    print(f"{lines+1}, line - {line}")

i = 0
while i<2:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(ADDR)
        CRLFreadline(s,BUFFER)
        i += 1
