from app import db

class User(db.Model):
    cache_ok = True
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(128), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    contacts = db.relationship('Contact', backref = 'Users', lazy = 'dynamic')

    def __repr__(self):
        return f"<User {self.username}>"

class Contact(db.Model):
    cache_ok = True
    id = db.Column(db.Integer, primary_key = True)
    contact_name = db.Column(db.String(64), index = True)
    contact_number = db.Column(db.String(15), index = True)
    contact_email = db.Column(db.String(128), index = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<Contact {self.contact_name}>"