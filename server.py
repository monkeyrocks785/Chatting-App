# importing the libraries
from os import name
import socket, time, sys

# creating the socket and retriving the hostname
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080

# building the host and the port
new_socket.bind((host_name, port))
print("Binding Successful...")
print("This is your ip : ", s_ip)

# listening for connections
name = input('Enter the name : ')
new_socket.listen(1)

# accepting incoming connections
conn, add = new_socket.accept()
print("Recieved connection from : ", add[0])
print("Connection established...")
print("Connection From : ", add[0])

# storing incoming connection data
client = (conn.recv(1024)).decode()
print(client + " has connected successfully...")
conn.send(name.encode())

# delivering packets/messages
while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ":", message)