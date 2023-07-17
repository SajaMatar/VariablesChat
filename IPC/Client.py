import socket
import os

print("Connecting to server ...")

# is the servers file exists 
if os.path.exists("/tmp/unixSockets"):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    client.connect("/tmp/unixSockets")
    print("Connected.")


    while True:
        try:
            userIn = input("> ")
            if "" != userIn:
                client.send(userIn.encode('utf-8'))
            else:
                print("Shutting down")
                break
            
        except KeyboardInterrupt :
            print("Shutting down.")
            client.close()
            break
else:
    print("Socket file doesnt exit....\nDone") 
