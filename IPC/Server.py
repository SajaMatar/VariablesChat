import socket
import os

# check if there exists a file 
if os.path.exists("/tmp/unixSockets"):
    os.remove("/tmp/unixSockets")

server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
# in unixSockets you are binding your socket to a file (created upen binding)
server.bind("/tmp/unixSockets")
print("Waiting for a connection...")

# where to store clients messages
what_was_sent = open('output.txt','w')
while True:
    try : 
       datagram = server.recv(1024)
       if not datagram:
          break
       else:
           what_was_sent.write("The message was : "+datagram.decode('utf-8')+"\n")
        
    
    except KeyboardInterrupt:
       print("\nShutting Down ....... \nDone") 
       break


server.close()
# remove it when the server is down
os.remove("/tmp/unixSockets")
