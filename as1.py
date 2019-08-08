#!/usr/bin/python3

import hashlib

print('''Welcome to Assassin_hash
[1].sha256      [6].sha224     [11].blake2b
[2].sha512      [7].sha_512    [12].shake_256
[3].md5         [8].sha384     [13].sha3_224
[4].blake2s     [9].sha_384    [14].sha3_256
[5].shake_128   [10].sha1
''')

type = input('Select a one: ')
text = input('Input word: ')
defi = ['sha256','sha512','md5','blake2s','shake_128','sha224','sha_512','sha384','sha_384','sha1','blake2b','shake_256','sha3_224','sha3_256']

#def decrypt():


def encrypt(type,word):
    exec('print(hashlib.'+type+'(b\"'+text+'\").hexdigest())')

encrypt(defi[int(type)-1],text)
