#!/usr/bin/python3

"""
@author Isaac Keeher
This is a database connector module to fetch
phone number details from mongoDB atlas
"""

from dotenv import dotenv_values
from pymongo import MongoClient
from pprint import pprint

config = dotenv_values(".env")

DB_PW = config['DB_PW']
DB_USER = config['DB_USER']
DB_URL = config['DB_URL']


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
