import socketserver
import threading

class messangerServer(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024)
        self.request.sendall(self.data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    server = socketserver.TCPServer((HOST, PORT), messangerServer)

    server.serve_forever()
