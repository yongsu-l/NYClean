from twilio.rest import Client
from auth import *

# Your Account SID from twilio.com/console
account_sid = acc
# Your Auth Token from twilio.com/console
auth_token  = auth

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16463715825", 
    from_="+18445517078",
    body="Hello from Python!")

print(message.sid)