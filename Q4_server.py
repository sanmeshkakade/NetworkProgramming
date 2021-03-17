import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("127.0.1.1",5590))

print(socket.gethostname())
print(s)

s.listen(4)

while 1:
    c,addr = s.accept()
    c.send(f"Connected to {socket.gethostname()} ".encode('utf-8'))
    c.close()

s.close()