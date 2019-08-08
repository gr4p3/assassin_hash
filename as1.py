#!/usr/bin/python3

import os
import sys
import hashlib
import mechanicalsoup
from time import sleep

banner = ('''Welcome to Assassin_hash
[1].sha256      [6].sha224     [11].blake2b
[2].sha512      [7].sha_512    [12].shake_256
[3].md5         [8].sha384     [13].sha3_224
[4].blake2s     [9].sha_384    [14].sha3_256
[5].shake_128   [10].sha1\n''')
def decrypt(type):
    hash = input('Input hash: ')
    browser = mechanicalsoup.StatefulBrowser()
    for i in range(6):
        os.system('clear')
        print('[+] Searching hash \''+hash+'\'')
        print('[+] Searching in hashtoolkit... '+str(i)+'/5')
        sleep(0.5)
    browser.open('https://hashtoolkit.com/reverse-hash?hash='+hash)
    result = browser.get_current_page().findAll('span',{'title':'decrypted sha1 hash'})
    if len(result) == 0:
        print('[!] No hashes found :(')
    elif len(result) > 0:
        print('[*] Succes! Decrypt hash found :\n')
        print(str(result[0].string)+'    <------Text')

def encrypt(type):
    text = input('Input text: ')
    exec('print(hashlib.'+type+'(b\"'+text+'\").hexdigest())')
#sys.argv
if len(sys.argv) != 2:
    print('Try again. Type '+sys.argv[0]+' -h')
elif len(sys.argv) == 2 and (sys.argv[1] in ('D','d','E','e','-h','h')):
    if sys.argv[1] in ('D','d'):
        print(banner)
        type = input('Select a one: ')
        defi = ['sha256','sha512','md5','blake2s','shake_128','sha224','sha_512','sha384','sha_384','sha1','blake2b','shake_256','sha3_244','sha3_256']
        algoritm = defi[int(type)-1]
        decrypt(algoritm)
    elif sys.argv[1] in ('E','e'):
        print(banner)
        type = input('Select a one: ')
        defi = ['sha256','sha512','md5','blake2s','shake_128','sha224','sha_512','sha384','sha_384','sha1','blake2b','shake_256','sha3_224','sha3_256']
        algoritm = defi[int(type)-1]
        encrypt(algoritm)
    elif sys.argv[1] in ('h','-h'):
        print('Usage: '+sys.argv[0]+' <option>')
        print('Options:')
        print('d  : Decrypt')
        print('e  : Encrypt')
else:
    print('Unexpected Error. Type: '+sys.argv[0]+' -h')
