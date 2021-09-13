from flask import Flask
from .classes.Budget import budget
from .classes.User import user
from .database import db

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'Budget',
    'host': 'localhost',
    'port': 27017
}

app.register_blueprint(budget)
app.register_blueprint(user)

db.init_app(app)



if __name__ == '__main__':
    app.run()
