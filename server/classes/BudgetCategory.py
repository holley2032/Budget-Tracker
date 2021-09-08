from ..app import db, app
from . import Budget, User

class BudgetCategory(db.Document):
    name = db.StringField()
    cateogry_log = db.ListField()
    money_remaining = db.DecimalField()
    money_spent = db.DecimalField()
    money_initial = db.DecimalField()
    user = db.ReferenceField(User)
    budget = db.ReferenceField(Budget)
    def to_json(self):
        return {"name": self.name,
        "budget": self.budget}