#Not Needed
from cryptography.fernet import Fernet
import cryptography
#Symmetric Key
#import cryptography.hazmat.primitives
#import cryptography.hazmat.backends
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import utils

private_crypted_key = {}
private_signed_key = {}

def new_keys():

    global private_crypted_key
    global private_signed_key
    private_crypted_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend())
    print(private_crypted_key)

    private_signed_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend())
    print(private_signed_key)

def sign_file():
    message = (b"A message I need to sign")
    signature = private_signed_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print(signature)

def hash_file():
    chosen_hash = hashes.SHA256()
    hasher = hashes.Hash(chosen_hash, default_backend())
    hasher.update(b"file data")
    digest = hasher.finalize()
    signed = private_signed_key.sign(
        digest,
        padding.PSS(
            mgf=padding.MGF1(chosen_hash),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        utils.Prehashed(chosen_hash)
    )
    print(signed)


def signing_verifying_key(file_hash, pub_key):
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(b"my Deep dark secret")
    print token

    original_key = f.decrypt(token)
    print original_key


def encryption_decryption():
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(b"my Deep dark secret")
    print token

    original_key = f.decrypt(token)
    print original_key


def read_file(filename):
    with open(filename, 'r') as f:
        contents = f.readlines

    print contents

if __name__ == "__main__":
    print("Symmetric.py is being run directly")
    read_file('testfile.txt')
    new_keys()
    sign_file()
    hash_file()
else:
    print("Symmetric.py is being imported")
