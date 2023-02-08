##########################################################################################
# Josiah Norman
# 10/03/2022
##########################################################################################

from http import server
from socket import * 
import os

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', 12000))
server_socket.listen(1)

print("server is ready to connect...\n")

while(True):
    
    connection_socket, address = server_socket.accept()
    
    incoming_message = connection_socket.recv(2048)
    
    incoming_file = connection_socket.recv(2047)
    print("HTTP request: \n{}".format(incoming_message.decode()))
    
    
    if (os.path.exists(incoming_file.decode())):
        f = open(incoming_file.decode())
        print("Object to be fetched: {}\nObject content:".format(incoming_file.decode()))
        data = f.read()
        print(data)
        
        header = ("HTTP/1.1 200 Ok\n\n{}".format(data))
        print("HTTP response message:")
        print(header)
        connection_socket.send(header.encode())
        
    else: 
        print("Object to be fetched: {}".format(incoming_file.decode()))
        header = ("HTTP/1.1 404 Not Found")
        print("HTTP response message:\nHTTP/1.1 404 Not Found")
        connection_socket.send(header.encode())
            
    connection_socket.close()
    