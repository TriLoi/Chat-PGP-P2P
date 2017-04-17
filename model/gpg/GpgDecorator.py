'''
Created on 17 avr. 2017

@author: root
'''
from model.gpg.GpgManager import GpgManager

class GpgDecorator(object):
    '''
    classdocs
    '''
    
    def __init__(self, key, nextGpgDecorator=None):
        '''
        Constructor
        '''
        self._key = key
        self._next = nextGpgDecorator
        
    def encrypt(self, message):
        if(self._next == None):
            return GpgManager.encrypt(self._key, message)
        return GpgManager.encrypt(self._key, self._next.encrypt(message))
    
    def decrypt(self, message):
        if(self._next == None):
            return GpgManager.decrypt(self._key, message)
        return self._next.decrypt(GpgManager.decrypt(self._key, message))