from Crypto.Cipher import AES
from Crypto.Util import Padding
from hashlib import md5
from base64 import b64encode, b64decode
from datetime import datetime

#source: https://gist.github.com/Frizz925/ac0fb026314807959db5685ac149ed67

def encrypt(password):
    passphrase = password
    #Get Current Date Time
    dateTimeObj = datetime.now()
    content = str(dateTimeObj)
    mode = AES.MODE_CBC
    #Block Size
    bs = AES.block_size

    # encrypting
    key = passphrase.encode('utf-8')
    body = Padding.pad(content.encode('utf-8'), bs)
    iv = key[8:bs+8]

    cipher = AES.new(key, mode, iv)
    key = b64encode(key).decode('utf-8')
    body = b64encode(cipher.encrypt(body)).decode('utf-8')
    iv = b64encode(iv).decode('utf-8')

    return body