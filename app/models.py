from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return 'User: {}'.format(self.email)

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.String(128))
    #need to add more info here about Schools and other classes
    #Relationships also need to be specified here
    #
