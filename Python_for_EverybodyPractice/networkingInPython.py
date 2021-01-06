import socket

url = 'google.com'
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((url,80))
cmd = f'GET http://{url}/romeo.txt HTTP/1.0\n\n'.encode()
print(cmd.decode())
sock.send(cmd)

while True:
    data =sock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
sock.close()