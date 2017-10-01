import sys
import cryptography
import json



def login(data):
    print (data)

def verify_password(password):
    print (password)

def create_user(info):
    print (info)
    compute_alpha(password)
    store_user(info);

def send_beta():
    print ("beta")

def compute_alpha(password):
    g = 9
    p = 23
    return (g^len(password)) mod p

def get_info():
    with open("login_info.json") as data_file:
        data = json

    print ("Please enter your username!")
    data[0]['userName'] = sys.stdin.readline()

    print ("Please enter your password!")
    data[0]['password'] = sys.stdin.readline()

    print ("Please enter your phone number!")
    data[0]['phoneNumber'] = sys.stdin.readline()


if __name__ == "__main__":

    print ("Start!")
