#!/usr/bin/python3

"""
@author Isaac Keeher
This program is an sms forwarder meant to recieve a
text message and forward it on to multiple numbers
"""

from flask import Flask, Response, request
from twilio import twiml
from dotenv import dotenv_values

config = dotenv_values(".env")


EVENT_LOCATION = config['EVENT_LOCATION']
GEO_LOCATION = config['GEO_LOCATION']
EVENT_TIME = config['EVENT_TIME']

app = Flask(__name__)


@app.route("/")
def hello():
    return Response("App is running!"), 200


@app.route("/getlocation", methods=["POST"])
def inbound_sms():
    """This function returns the location of the rave when somebody sends a message
    """
    response = twiml.Response()
    # we get the SMS message from the request. we could also get the
    # "To" and the "From" phone number as well
    inbound_message = request.form.get("Body")
    # we can now use the incoming message text in our Python application
    if inbound_message is not None:
        response.message(f"Hey tripper! The party location is \
             {EVENT_LOCATION} - {GEO_LOCATION} - starting at {EVENT_TIME}")
    else:
        response.message("Do you want to know where the party is?")
    # we return back the mimetype because Twilio needs an XML response
    return Response(str(response), mimetype="application/xml"), 200


def recieve_sms():
    pass


def send_sms():
    pass


if __name__ == "__main__":
    message = f"Hey tripper! The party location is at {EVENT_LOCATION} " \
             + f"({GEO_LOCATION}) - starting at {EVENT_TIME}!!!"
    print(message)
    # app.run(debug=True)
