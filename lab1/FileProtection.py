#Not Needed
import sys
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


public_crypted_key = None
private_crypted_key = None
signature = None
public_signed_key = None
private_signed_key = None


def new_keys():

    global private_crypted_key
    global private_signed_key
    global public_crypted_key
    global public_signed_key

    private_crypted_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend())
    print(private_crypted_key)
    public_crypted_key = private_crypted_key.public_key()

    private_signed_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend())
    print(private_signed_key)
    public_signed_key = private_signed_key.public_key()

def sign_file(digest):
    #Signing message
    global signature
    signature = private_signed_key.sign(
        digest,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("File is signed!")

def hash_file(file_message):

    message = file_message.encode(encoding='UTF-8')
    chosen_hash = hashes.SHA256()
    hasher = hashes.Hash(chosen_hash, default_backend())

    #Hashing message
    hasher.update(message)
    digest = hasher.finalize()
    print ("File is hashed! Here is hashed file:", digest)
    #Call signing_message
    sign_file(digest)
    return digest

def encryption(signed_file):
    print sys.getsizeof(signed_file, "bytes")
    cipertext = public_crypted_key.encrypt(
        signed_file,
        padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    print("File is completely encrypted! Here is encrypted File:", cipertext)
    return cipertext

def verify(message):
    public_signed_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("The message matches the signature!")


def decryption(cipertext):
    plaintext = private_crypted_key.decrypt(
        cipertext,
        padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    print("File is completely decrypted! Here is decrypted file:", plaintext)
    return plaintext

def read_file(filename):
    with open(filename, 'r') as f:
        contents = f.read().replace('\n', '')
    #print contents
    #print(type(contents))
    print("File is loaded!")
    return contents

if __name__ == "__main__":
    print("Symmetric.py is being run directly")

    new_keys()

    file_txt = read_file('testfile.txt')
    #sign_file(file_txt)
    hashed_file = hash_file(file_txt)
    verify(hashed_file)
    print("Encryption and Decryption")
    encrypted_msg = encryption(hashed_file)
    decrypted_msg = decryption(encrypted_msg)
    verify(decrypted_msg)
    print("Here is decrypted_msg, it should be the same as the hashed_file", decrypted_msg)

else:
    print("Symmetric.py is being imported")
