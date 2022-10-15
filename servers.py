class Server:
    __count = 0
    
    def __init__(self):
        Server.__count += 1
        self.ip = Server.__count
        self.buffer = []
        self.rout = ''
        
    def send_data(self, data):
        self.rout.buffer += [data]
    
    def get_data(self):
        a = self.buffer.copy()
        self.buffer = []
        return a
    
    def get_ip(self):
        return self.ip


class Router:
    
    def __init__(self):
        self.buffer = []
        self.servers = []
        
    def link(self, server):
        self.servers += [server]
        server.rout = self

    def unlink(self, server):
        self.servers.remove(server)
        server.router = ''
    
    def send_data(self):
        for i in self.buffer:
            for j in self.servers:
                if i.ip == j.ip:
                    j.buffer += [i]
        self.buffer = []


class Data:
    def __init__(self, data, ip):
        self.data = data 
        self.ip = ip




