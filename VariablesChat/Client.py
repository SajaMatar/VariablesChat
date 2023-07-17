import socket
import threading
import sys
import os

def helloServer():
    client_socket.send(name.encode('ascii'))  

def recv():
    while True:
        message = client_socket.recv(1027).decode('ascii')
        if (message == ""):
            print("\nServer is Down , Try again later....")
            os._exit(1)
        else:
            print(message)
              

def write():
    while True:
        message_to_send = input()
        client_socket.send("{} : {}".format(name,message_to_send).encode('ascii'))


host="127.0.0.1"
port = 55555

name = input("Welcome to variables , enter your name : ")
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    client_socket.connect((host,port))
    helloServer()
    r = threading.Thread(target=recv)
    r.start()
    w = threading.Thread(target=write)
    w.start()
except:
    print("Server is Down , try again later .... ")



