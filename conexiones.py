"""
Para probar el ejemplo ejecutar en otra terminal
inicialmente un servidor que escuche en el puerto 7000.

nc -l 7000

"""

from socket import socket


sock_cliente = socket()
sock_cliente.connect(('localhost', 7000))

sock_cliente.send("Hola que tal")
print sock_cliente.recv(1000)
