#!/usr/bin/python3

"""
@author Isaac Keeher
This is a database connector module to fetch
phone number details from mongoDB atlas
"""

from dotenv import load_dotenv
from pymongo import MongoClient
from pprint import pprint
import os

load_dotenv()

DB_PW = os.environ.get('DB_PW')
DB_USER = os.environ.get('DB_USER')
DB_URL = os.environ.get('DB_URL')


def connect():
    # connect to MongoDB, you need to fill out the .env for security :)
    client = MongoClient(
        f"mongodb+srv://{DB_USER}:{DB_PW}@{DB_URL}")
    db = client.admin
    # Issue the serverStatus command and print the results
    serverStatusResult = db.command("serverStatus")
    pprint(serverStatusResult)
    return serverStatusResult


if __name__ == "__main__":
    connect()
