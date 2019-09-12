import fire
import os
from Crypto.Cipher import AES
from getpass import getpass


base_path = os.getenv('SECRETS_ROOT', os.path.expanduser('~/.secrets'))

mode = AES.MODE_ECB

def complete(string, size=32):
    return (string + (size*" "))[0:size]

class Secret:
    def set(self, key, value):
        password = getpass()
        encryptor = AES.new(complete(password), mode)
        f = open("%(base_path)s/%(key)s.enc"%{
            'base_path': base_path,
            'key': key
        }, "wb")
        f.write(encryptor.encrypt(complete(value,256)))

    def get(self, key):
        password = getpass()
        decryptor = AES.new(complete(password), mode)
        f = open("%(base_path)s/%(key)s.enc"%{
            'base_path': base_path,
            'key': key
        }, "rb")
        print(decryptor.decrypt(f.read()))

if __name__ == '__main__':
    fire.Fire(Secret)
