from app import db
from . import User

class Budget(db.Document):
    categories = db.ListField()
    name = db.StringField()
    budget_log = db.ListField()
    money_remaining = db.DecimalField()
    money_spent = db.DecimalField()
    money_initial = db.DecimalField()
    user = db.ReferenceField(User)
    def to_json(self):
        return {"email": self.User.email,
        "name": self.name}



    """   
 Old definition of budget for reference:
 
 def __init__(self, username):
        self.categories = []
        self.name = username
        self.budget_log = []

        @property
        def money_left(self):
            return self._money_left

        @money_left.setter
        def money_left(self):  # Computationally inefficient, probably not relevant for a local machine.
            self._money_left = 0
            for cat in self.categories:
                self._money_left += cat.money_left

        @property
        def money_total(self):
            return self._money_total

        @money_total.setter
        def money_total(self):  # Computationally inefficient, but that is probably not relevant for a local machine.
            self._money_total = 0
            for cat in self.categories:
                self._money_total += cat.money_total

    def addCategory(name, amountMoney):
        pass """