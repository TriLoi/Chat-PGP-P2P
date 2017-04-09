'''
Created on Mar 4, 2017

@author: loi
'''

import socket
from exceptions.ListenerException import ListenerException

class Listener(object):
    '''
    classdocs
    '''
    _TIMEOUT_LISTENING = 0.1
    _BUFSIZ = 4096

    def __init__(self, port, max_connections):
        '''
        Constructor
        '''
        super(Listener,self).__init__()
        self._max_connections = max_connections
        self._port = port
        self._sock_src = None
        
    def start(self):
        if(self._sock_src == None):
            self._sock_src = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._sock_src.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self._sock_src.bind(('', self._port))
            self._sock_src.listen(self._max_connections)
    
    def listen(self,onResponseFunction):
        if(self._sock_src == None):
            raise ListenerException()
        
        try:
            self._sock_src.settimeout(Listener._TIMEOUT_LISTENING)
            pair = self._sock_src.accept()
            if(pair is not None):
                client, address = pair
                onResponseFunction(address, client)
                client.close()
                return True
        except socket.timeout:
            pass
        return False
    
    def stop(self):
        if(self._sock_src == None):
            raise ListenerException()
        
        self._sock_src.close()
        self._sock_src = None
    
    pass