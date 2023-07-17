import socket
import threading

class Client:
    def __init__(self, sok, name, address):
        self.sock = sok
        self.name = name
        self.address = address
  

def add_client(name):
    currentUsers.append(Client(client_socket,name,client_address))
    return currentUsers[-1]


def hello_client():
    name = client_socket.recv(1024).decode('ascii')
    print("{} is in the chat.".format(name))
    broadcast("******** {} is here".format(name).encode('ascii'),client_socket)
    getMessages(add_client(name))

def whoIsHere(client):
    users = "{ "
    for user in currentUsers :
        users += (user.name+ ", ") 
    users+=" }"
    client.sock.send(users.encode('ascii'))

def  getMessages(user):
    while True:
      try:
        message = user.sock.recv(1024)
        if message.decode('ascii') == "{} : whoIsHere".format(user.name):
            whoIsHere(user)
        else:
            broadcast(message,user)
      except:
        break

def broadcast(message,user1):
    if currentUsers:
         #broadcast("{} has left the chat.\n".format(user.name).encode('ascii'),user)
         for user in currentUsers:
            try:
                if user != user1:
                    user.sock.send(message)
            except :
                print("{} has left the server\n".format(user.name))
                name = user.name
                user.sock.close()
                currentUsers.remove(user)
                if len(currentUsers) > 1:
                 for u in currentUsers : 
                    u.sock.send("**** {} has left the chat".format(name).encode('ascii'))
                else:
                   for u in currentUsers:
                    u.sock.send("**** you are alone in the chat...".encode('ascii'))

    else:
        print("**** No one is connected yet.")



host = "127.0.0.1"
port = 55555

SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
SERVER.bind((host,port))
SERVER.listen(4)

currentUsers = []

print("Waiting for connections : ")
while True:
    try:
        client_socket , client_address = SERVER.accept()
        hello_thread = threading.Thread(target = hello_client) 
        hello_thread.start()
    except socket.error:
        print("Done")
