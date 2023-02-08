##########################################################################################
# Josiah Norman
# 10/03/2022
##########################################################################################

from http import client
from socket import * 
import sys

client_socket = socket(AF_INET, SOCK_STREAM)

server_ip = sys.argv[1]
server_port = sys.argv[2]
server_file = sys.argv[3]

client_socket.connect((server_ip, int(server_port)))

print("HTTP request to server: ")
header = "GET /{} HTTP/1.1\nHost: {} \n".format(server_file, server_ip)
print(header)

client_socket.send(header.encode())
client_socket.send(server_file.encode())

recieved_message = client_socket.recv(2048)
print("HTTP response from server: \n{}".format(recieved_message.decode()))

client_socket.close()