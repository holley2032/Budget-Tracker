from app import db
from . import Encryption, Budget

class User(db.Document):
    first_name = db.StringField()
    last_name = db.StringField()
    email = db.StringField()
    password = db.StringField()
    Budget = db.Document()
    def to_json(self):
        return {"email": self.email}