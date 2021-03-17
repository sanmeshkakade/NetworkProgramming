import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.1.1', 0))
print('listening on port:', sock.getsockname()[1])
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)