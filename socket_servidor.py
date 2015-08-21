from socket import socket
import os
server_sock = socket()
server_sock.bind(('', 7002))
server_sock.listen(10)

while True:
    conexion = server_sock.accept()
    print conexion
    
    