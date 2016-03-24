import socket
import sys

HOST, PORT = "192.168.1.75", 9829

try:
    while True:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))

        data = input()
        sock.sendall(bytes(data, "UTF-8"))

        recieved = sock.recv(1024)

        print("User1: " + data)
        print(recieved.decode("UTF-8"))
        
finally:
        print("ended")
