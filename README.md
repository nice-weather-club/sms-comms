# sms-comms
a simple flask server that does sms-forwarding and auto-reply for event location

TODO:

- [ ] add a database for phone numbers
- [ ] integrate properly with twilio
- [ ] setup ci/cd

To run you'll need to create a .env file in the top level directory
e.g.
```
EVENT_LOCATION="Westgate Bridge"
GEO_LOCATION="-37.83184926174339, 144.90473068626446"
EVENT_TIME="11.30PM"

DB_URL=<URL>
DB_PW=<SECRET_PASSWORD>
DB_USER=<USERNAME>
```