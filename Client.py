'''
Created on Mar 23, 2017

@author: loi
'''
import socket
from exceptions.ClientException import ClientException

class Client(object):
    '''
    classdocs
    '''
    _TIMEOUT_RECV = 1
    _BUFSIZ = 4096
    
    def __init__(self, addr, port):
        '''
        Constructor
        '''
        super(Client, self).__init__()
        self._addr = addr
        self._port = port
        self._sock_dest = None
        
    def connect(self):
        if(self._sock_dest is None):
            self._sock_dest = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._sock_dest.connect((self._addr, self._port))

    def isConnected(self):
        return self._sock_dest is not None
                
    def send(self, message):
        if(self._sock_dest is None):
            raise ClientException()
        
        try:
            self._sock_dest.send(message)
        except BrokenPipeError:
            self.disconnect()
        
    def recv(self):
        if(self._sock_dest is None):
            raise ClientException()
        
        try:
            self._sock_dest.settimeout(Client._TIMEOUT_RECV)
            message = self._sock_dest.recv(Client._BUFSIZ)
            
            if(not message):
                raise ConnectionResetError
            
            return message
        except (ConnectionResetError, socket.timeout):
            self.disconnect()
            return None
        
    def disconnect(self):
        if(self._sock_dest is not None):
            self._sock_dest.close()
            self._sock_dest = None