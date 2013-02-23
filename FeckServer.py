
import socket 

class FeckServer:
    def __init__(self, host = '', port = 1337, backlog = 5, msg_size = 1024):
        self.host = host
        self.port = port
        self.backlog = backlog
        self.msg_size = msg_size
        
    def run(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.s.bind((self.host,self.port)) 
        self.s.listen(self.backlog) 
        
        print('Feck!')
        
        while 1: 
            try:
                client, address = self.s.accept() 
                data = client.recv(self.msg_size) 
                if data: 
                    client.send(data) 
                print('Arse! : '+str(data))
            except KeyboardInterrupt:
                print('Feck off.')
                break

f = FeckServer()
f.run()