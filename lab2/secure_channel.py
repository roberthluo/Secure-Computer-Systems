import sys
import json
import twilio
from twilio.rest import Client

import yaml

stored_data = {}

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

def compute_alpha():
    password = "fdfdf"
    password = stored_data['password']
    g = 9
    p = 23
    access_code = (g^len(password)) % p
    print("Access code", access_code)
    stored_data['accessCode'] = access_code
    return (access_code)

def get_info():

    global stored_data

    print ("Please enter your username!")
    data['userName'] = sys.stdin.readline()

    print ("Please enter your password!")
    data['password'] = sys.stdin.readline()



def check_sms():
    generated_value = "fd"

    print ("Please enter your sms verification code!")
    value = sys.stdin.readline()
    if(value == generated_value):
        print("You have logged in!")
    else:
        print("That is not your sms verification code!")



def test_twilio():
    data = {'account_sid': '',
            'auth_token': ''}

    with open("twilio_api_key.yaml", "r") as stream:
        data = yaml.load(stream)

    print(data["account_sid"])

    client = Client(data["account_sid"], data["auth_token"])

    access_code = stored_data['accessCode']
    print("accessCode 123123123", stored_data)
    print("accessCode ", stored_data['accessCode'])

    try:
        message = client.messages.create(

            to="+16137934538",
            from_="+13658006524",
            body=access_code)

        print(message.sid)
    except twilio.base.exceptions.TwilioRestException as e:
        print (e)

if __name__ == "__main__":

    print ("Start!")
    get_info()

    compute_alpha()
    test_twilio()
