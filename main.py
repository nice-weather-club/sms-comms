#!/usr/bin/python3

"""
@author Isaac Keeher
This program is an sms forwarder meant to recieve a
text message and forward it on to multiple numbers
"""

from flask import Flask, Response, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'sms is awesome!'


def recieve_sms():
    pass


def send_sms():
    pass


if __name__ == "__main__":
    print("hello")
