from . import Encryption, Budget

class Profile:
    def __init__(self, username, name, password):
        self.username = username
        self.name = name
        self.password = Encryption.encryptPassword(password)
        self.budget = Budget(username)