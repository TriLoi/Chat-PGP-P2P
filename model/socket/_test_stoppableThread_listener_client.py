'''
Created on Mar 4, 2017

@author: loi
'''
from model.socket.StoppableThread import StoppableThread
from model.socket.Listener import Listener
from model.socket.Client import Client

class mserver(StoppableThread):
    def __init__(self):
        super(mserver,self).__init__()
        self._listener = Listener(80,1000)

    def run_begin(self):
        self._listener.start()
        print("server : start listener 80")
        pass
    
    def run_do(self):
        self._listener.listen(self.action)
        pass
    
    def run_end(self):
        self._listener.stop()
        print("server : stop listener 80")
        pass
    
    def action(self, address, client):
        print("server : recv from " + str(address[0]) + ":80 -> " + str(client.recv(Listener._BUFSIZ)))
        client.send(b'yolo80')
        print("server : send to " + str(address[0]) + ":80 -> yolo80")
        pass
    pass
    
class mclient(StoppableThread):
    def __init__(self, i):
        super(mclient,self).__init__()
        self._client = Client('localhost',80)
        self._id = str(i)

    def run_begin(self):
        self._client.connect()
        print("client " + self._id + " : connect to localhost")
        pass
    
    def run_do(self):
        if(self._client.isConnected()):
            print("client " + self._id + " : isConnected -> true")
            self._client.send(b"message")
            print("client " + self._id + " : send to localhost -> message")
            print("client " + self._id + " : recv from localhost -> " + str(self._client.recv()))
        else:
            print("client " + self._id + " : isConnected -> false")
            self.stop()
        pass
    
    def run_end(self):
        self._client.disconnect()
        print("client " + self._id + " : stop client")
        pass
    pass

s = mserver()
s.start()
cl1 = mclient(1)
cl1.start()
cl2 = mclient(2)
cl2.start()

ch = input()

s.stop()
print("stop app")
