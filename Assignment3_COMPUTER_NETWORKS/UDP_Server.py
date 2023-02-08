##########################################################################################################
# Josiah Norman
# 10/09/2022
##########################################################################################################

from socket import *
from random import randint
import time

# Create server socket.
server_socket = socket(AF_INET, SOCK_DGRAM)

# Bind server socket to port number.
server_socket.bind(('', 12000))
print("Server is ready to receive messages...\n")

# Run forever loop to keep receiving messages.
while (True):
    
    # Sample will be a number from the set {1,2,3,4,5}.
    sample = randint(1,5)
    message, client_address = server_socket.recvfrom(2048)
    
    # 60% of runs should follow this if statement.
    if sample >= 3:
        server_socket.sendto(message, client_address)
    
    # 40% of runs should follow this if statement.
    else:
        # Error message.
        print("Request timed out.")
    