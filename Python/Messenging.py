import socket
import _thread

def Messenger():

    host = "127.0.0.1"
    port = 5000
    print("Testing")
    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    print ("Starting Threads")
    try:
        thread.start_new_thread( recvMessage, (s))
        thread.start_new_thread(sendMessage, (c))
    except:
        print("Unable to do stuff")

def recvMessage(s):
    print ("Recv")
    while true:
        data = s.recieve(1024)
        if data != None:
            print ("User: " + str(data))

def sendMessage(s):
    print ("Send")
    while True:
        msg = input("Say Something: ")
        if msg != None:
            c.send(msg)

Messenger()
