# A simple echo client 
import socket 

class FeckClient:
    def __init__(self, host = 'localhost', port = 1337, msg_size = 1024):
        self.host = host
        self.port = port
        self.msg_size = msg_size

    def connect(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.server.connect((self.host,self.port)) 
        
    def send(self, msg):
        self.server.send(bytes(msg, 'utf-8'))
        try:
            data = self.server.recv(self.msg_size)
        except socket.error:
            self.disconnect()
            data = "server disconnected"
        return data
    
    def disconnect(self):
        self.server.shutdown(1)
        self.server.close()

        
if __name__ == '__main__':
    c = FeckClient()
    c.connect()
    response = c.send('Hello world.')
    print(response)
    c.disconnect()