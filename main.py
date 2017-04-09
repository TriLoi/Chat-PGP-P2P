'''
Created on Mar 4, 2017

@author: loi
'''
from model.StoppableThread import StoppableThread
from model.Listener import Listener
from model.Client import Client
from model.GpgManager import GpgManager
    
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
    def __init__(self):
        super(mclient,self).__init__()
        self._client = Client('localhost',80)

    def run_begin(self):
        self._client.connect()
        print("client : connect to localhost")
        pass
    
    def run_do(self):
        if(self._client.isConnected()):
            print("client : isConnected -> true")
            self._client.send(b"message")
            print("client : send to localhost -> message")
            print("client : recv from localhost -> " + str(self._client.recv()))
        else:
            print("client : isConnected -> false")
            self.stop()
        pass
    
    def run_end(self):
        self._client.disconnect()
        print("client : stop client")
        pass
    pass

'''s = mserver()
s.start()
cl1 = mclient()
cl1.start()
cl2 = mclient()
cl2.start()

ch = input()

s.stop()
print("stop app")'''

gpg = GpgManager()
gpg.createKey("yolo@yolo.com","pass123")
