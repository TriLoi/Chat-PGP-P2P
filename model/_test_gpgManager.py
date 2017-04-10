'''
Created on Mar 4, 2017

@author: loi
'''
from model.GpgManager import GpgManager
    
gpg = GpgManager()
gpg.createKey("yolo@yolo.com","pass123")
