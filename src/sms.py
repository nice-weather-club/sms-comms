# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

from dotenv import load_dotenv
import os

load_dotenv()

DB_PW = os.environ.get('DB_PW')
DB_USER = os.environ.get('DB_USER')
DB_URL = os.environ.get('DB_URL')



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Jungle is massive",
                     from_='+17029194582',
                     to='+61414893059'
                 )

print(message.sid)