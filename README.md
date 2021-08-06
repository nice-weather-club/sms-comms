# sms-comms
a simple flask server that does sms-forwarding and auto-reply for event location

## setup
note: you'll want a mongodb credential to do anything database related

```
python3 -m venv env  # create a virtual env 
pip3 install -r requirements.txt  # install all the required packages
```

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

## project goals

TODO:

- [x] add a database
- [ ] fetch phone numbers
- [ ] integrate properly with twilio
- [ ] setup ci/cd



