# importing libraries
import socket, time, sys

# creating a socket and accepting user input hostname
socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080

# connecting to the server
print("This is your ip : ", ip)
server_host = input('Enter the friend\'s IP Address : ')
name = input('Enter your name : ')

socket_server.connect((server_host, sport))

# recieving the packets/messsges from the server
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name, " has joined successfully...")
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input('Me : ')
    socket_server.send(message.encode())
