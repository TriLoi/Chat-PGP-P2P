'''
Created on Mar 21, 2017

@author: loi
'''

import threading

class StoppableThread(threading.Thread):
    
    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stopper = threading.Event()

    def stop(self):
        self._stopper.set()

    def stopped(self):
        return self._stopper.is_set()

    def run(self):
        self.run_begin()
        while not self.stopped():
            self.run_do()
        self.run_end()
        
    def run_begin(self):
        raise NotImplementedError()
    
    def run_do(self):
        raise NotImplementedError()
    
    def run_end(self):
        raise NotImplementedError()