##########################################################################################################
# Josiah Norman
# 10/09/2022
##########################################################################################################

from socket import *
from statistics import mean
import time
import datetime 
from datetime import date
import sys

# create client socket and adjust socket timeout.
client_socket = socket(AF_INET, SOCK_DGRAM)

server_ip = sys.argv[1]
server_port = sys.argv[2]

# Number of UDP segments that will be sent to the server.
n = int(sys.argv[3])        

# Formatting message.
print("Pinging {}".format(server_ip))

# Counter for the amount of segments recieved by the server.
recieved = 0

# Array that will house values of the total roundtrip in milliseconds. 
f = []

# Weekday array that will be used to transfer a numerical representations for days of the week into grammatical representations.
week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

# Loops n amount of times.
for i in range(n):  
     
    while True:

        # Consistently updates time.
        date = datetime.datetime.now()
        
        # Formatting message that will be sent to the server.
        message = ("Ping {} {} {} {} {}:{}:{} {}".format(recieved + 1, week[date.weekday()], date.month, date.day, date.hour, date.minute, date.second, date.year))
        
        # Sends message to server.
        client_socket.sendto(message.encode(), (server_ip, int(server_port)))
        
        # Stopwatch start. 
        time_sent = time.time()
    
        client_socket.settimeout(1.0)
        
        try:
            
            # Recieves message from server.
            recv_message, server_address = client_socket.recvfrom(2048)
            
            if recv_message != None:
                
                # Stopwatch end.
                time_recieved = time.time()
            
                # Calculates time difference. 
                delta_time = time_recieved - time_sent
                
                # If the message recieved was not an error message.
                roundtrip = int(round(delta_time*1000))
                
                # Increment recieved counter.
                recieved += 1
                
                # Append value to array.
                f.append(roundtrip)
                
                #Formatting message.
                print("Reply from {}: {} time={}ms TTL=1".format(server_ip, recv_message.decode(), float(roundtrip)))
                break
            
        # If no message is recieved.
        except: 
            print("Request timed out.")
            break 
          
client_socket.close()
            
# Statistics portion.
print("\nPing statistics for {}:".format(server_ip))
print("\t Segments: Sent: {}, Recieved: {}, Lost: {} ({}% Loss)".format(n, recieved, n - recieved, round(((n - recieved)/n)*100, 2)))
print("Approximate round trip times in ms:")
print("\t Minimum = {}ms, Maximum = {}ms, Average = {}ms".format(float(min(f)), float(max(f)), round(mean(f), 2)))