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

    @staticmethod
    def createKey(name_email, passphrase):
        ''' Doesn't work
        gpg = GPG(gnupghome=GpgManager._GPG_HOME)
        gpg.encoding = 'utf-8'
    
        input_data = gpg.gen_key_input(
            key_type="RSA",
            key_length=1024,
            name_email=name_email,
            passphrase=passphrase
        )
        
        key = gpg.gen_key(input_data)
        
        ascii_armored_public_keys = gpg.export_keys(key)
        ascii_armored_private_keys = gpg.export_keys(key, True)
        with open('mykeyfile.asc', 'w') as f:
            f.write(ascii_armored_public_keys)
            f.write(ascii_armored_private_keys)
        '''
        return None
    
    @staticmethod        
    def encrypt(key, message):
        return "e_" + key + ":" + message
    
    @staticmethod
    def decrypt(key, message):
        return "d_" + key + ":" + message
    
    pass