'''
Created on 31 mars 2017

@author: loi
'''
from gnupg import GPG

class GpgManager(object):
    '''
    classdocs
    https://pythonhosted.org/python-gnupg/
    '''
    _GPG_HOME = './gpg_home'

    def __init__(self):
        '''
        Constructor
        '''
        self._gpg = GPG(gnupghome=GpgManager._GPG_HOME)
        self._gpg.encoding = 'utf-8'
        
    def createKey(self, name_email, passphrase):
        ''' Doesn't work
        input_data = self._gpg.gen_key_input(
            key_type="RSA",
            key_length=1024,
            name_email=name_email,
            passphrase=passphrase
        )
        
        key = self._gpg.gen_key(input_data)
        
        ascii_armored_public_keys = self._gpg.export_keys(key)
        ascii_armored_private_keys = self._gpg.export_keys(key, True)
        with open('mykeyfile.asc', 'w') as f:
            f.write(ascii_armored_public_keys)
            f.write(ascii_armored_private_keys)
        '''
        return None
            
    def encrypt(self, key, message):
        return message
    
    def decrypt(self, key, message):
        return message
    
    pass