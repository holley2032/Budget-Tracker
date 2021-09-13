from ..database import db
from . import Encryption, Budget
import json
from flask import Blueprint, request, jsonify

class User(db.Document):
    first_name = db.StringField()
    last_name = db.StringField()
    email = db.StringField()
    password = db.StringField()
    Budget = db.ListField()
    def to_json(self):
        return {"email": self.email}

user = Blueprint("user", __name__)

@user.route('/user', methods=['POST'])
def create_user():
    record = json.loads(request.data)
    user = User(first_name=record['first_name'],
    last_name=record['last_name'],
    email=record['email'],
    password=record['password'])
    user.save()   