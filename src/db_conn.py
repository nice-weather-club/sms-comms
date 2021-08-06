#!/usr/bin/python3

"""
@author Isaac Keeher
This is a database connector module to fetch
phone number details from mongoDB atlas
as well as insert new ones when people
want to sign up !!
"""

from dotenv import load_dotenv
from pymongo import MongoClient
from pprint import pprint
import os
from random import randint

load_dotenv()

DB_PW = os.environ.get('DB_PW')
DB_USER = os.environ.get('DB_USER')
DB_URL = os.environ.get('DB_URL')

# create a network connection
client = MongoClient(
    f"mongodb+srv://{DB_USER}:{DB_PW}@{DB_URL}")
db = client["testdb"]  # makes a test database called "testdb"
col = db["testcol"]  # makes a collection called "testcol" in the "testdb"


def db_status() -> object:
    # connect to MongoDB, you need to fill out the .env for security :)
    # Issue the serverStatus command and print the results
    serverStatusResult = db.command("serverStatus")
    pprint(serverStatusResult)
    return serverStatusResult


def db_insert(record: str) -> object:
    # Create sample data
    first_name = [
        'Jon', 'Sandor', 'Joffrey', 'Cersei', 'Jaime', 'Sansa',
        'Arya', 'Lem', 'Dolorous Edd', 'Melisandre', 'Varys',
        'Young Griff', 'Rhaegar', 'Asha', 'Theon'
    ]
    last_name = ['Lannistar', 'Stark', 'Targaryen', 'Snow', 'Greyjoy']

    for x in range(1, 20):
        person = {
            'name': first_name[randint(0, (len(first_name)-1))]
            + ' ' + last_name[randint(0, (len(last_name)-1))],
            'phone': randint(61499128, 61499995),
        }
        # Step 3: Insert business object directly into MongoDB via insert_one
        result = col.insert_one(person)
        # Step 4: Print to the console the ObjectID of the new document
        print('Created {0} of 20 as {1}'.format(x, result.inserted_id))
    # Step 5: Tell us that you are done
    print('finished creating 20 people')


def db_list():
    pass

if __name__ == "__main__":
    # col.insert_one({"foo": "bar"})  # add a document to testdb.testcol
    db_insert("hi")
