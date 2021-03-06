# -*- coding:utf-8 -*-

# Author:Chuixin Zeng

import hashlib

m = hashlib.md5()
m.update("Hello".encode(encoding='utf-8'))
m.update("It's me".encode(encoding='utf-8'))
print(m.digest())
m.update("It's been a long time since last time we ...".encode(encoding='utf-8'))

print(m.digest())  # 2进制格式hash
print(len(m.hexdigest()))  # 16进制格式hash
'''
def digest(self, *args, **kwargs): # real signature unknown
    """ Return the digest value as a string of binary data. """
    pass

def hexdigest(self, *args, **kwargs): # real signature unknown
    """ Return the digest value as a string of hexadecimal digits. """
    pass 

'''

# ######## md5 ########

hash = hashlib.md5()
hash.update('admin'.encode(encoding='utf-8'))
print(hash.hexdigest())

# ######## sha1 ########

hash = hashlib.sha1()
hash.update('admin'.encode(encoding='utf-8'))
print(hash.hexdigest())

# ######## sha256 ########

hash = hashlib.sha256()
hash.update('admin'.encode(encoding='utf-8'))
print(hash.hexdigest())

# ######## sha384 ########

hash = hashlib.sha384()
hash.update('admin'.encode(encoding='utf-8'))
print(hash.hexdigest())

# ######## sha512 ########

hash = hashlib.sha512()
hash.update('admin'.encode(encoding='utf-8'))
print(hash.hexdigest())