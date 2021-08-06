#!/usr/bin/python3

"""
@author Isaac Keeher
This program is an sms forwarder meant to recieve a
text message and forward it on to multiple numbers

It should also reply when texted for event details
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


@app.route("/getLocation", methods=["POST"])
def inbound_sms():
    """This function returns the location of the rave when somebody sends a message
    """
    response = twiml.Response()
    # we get the SMS message from the request. we can also get
    # "To" and the "From" phone number as well
    inbound_message = request.form.get("Body")
    # we can now use the incoming message text
    # TODO: maybe use a regex here to search for "location" or "where"?
    if inbound_message == "YES":
        response.message(
            f"Hey tripper! The party location is \
             {EVENT_LOCATION} - {GEO_LOCATION} - starting at {EVENT_TIME}"
             )
    else:
        response.message(
            "Do you want to know where the party is? If so, reply 'YES'"
            )
    # we return back the mimetype because Twilio needs an XML response
    return Response(str(response), mimetype="application/xml"), 200


@app.route("/forwardMsg", methods=["POST"])
def recieve_sms():
    """This function is to forward messages to existing users
    """
    # response = twiml.Response()
    inbound_message = request.form.get("Body")
    print(inbound_message)
    # TODO: add some database connecting code


if __name__ == "__main__":
    app.run(debug=True)
