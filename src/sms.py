from twilio.rest import Client
from auth import *

def sendSMS(location, phone_number):
    # Your Account SID from twilio.com/console
    account_sid = twilio_acc
    # Your Auth Token from twilio.com/console
    auth_token  = twilio_auth

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=phone_number, 
        from_=twilio_num,
        body=location)
    print(message.sid)