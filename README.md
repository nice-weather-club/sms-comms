# sms-comms
a simple flask server that does sms-forwarding and auto-reply for event location

## setup
note: you'll want a mongodb credential to do anything database related

```
python3 -m venv venv  # create a virtual env
source venv/bin/activate  # activate it
pip3 install -r requirements.txt  # install all the required packages
```

alternatively just run ```make build```

To run you'll need to create a ```.env``` file in the top level directory
e.g.
```
EVENT_LOCATION="Westgate Bridge"
GEO_LOCATION="-37.83184926174339, 144.90473068626446"
EVENT_TIME="11.30PM"

DB_URL=<URL>
DB_PW=<SECRET_PASSWORD>
DB_USER=<USERNAME>
```

## using the makefile

some time saving commands

| make command  | action |
|---|---|
|  make build | build and install packages in virtual environment
|  make clean | wipe clean all pytest, virtualenv and cache etc. files for a clean environment| 
|  make run | run the dev flask server on port 5000 on localhost |
|  make lint | run flake8 linter on all source ```.py``` files |
|  make test | run unit tests in tests folder | 


## project goals

TODO:

- [x] add a database
- [ ] fetch phone numbers
- [ ] integrate properly with twilio
- [ ] setup ci/cd



