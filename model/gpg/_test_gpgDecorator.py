'''
Created on 17 avr. 2017

@author: root
'''
from model.gpg.GpgDecorator import GpgDecorator

d = GpgDecorator("key1")
d = GpgDecorator("key2",d)

message = d.encrypt("message")
print(message)
message = d.decrypt(message)
print(message)