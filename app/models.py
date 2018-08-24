from app import db

favorites = db.Table('favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('degree_id', db.Integer, db.ForeignKey('degree.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    favorited = db.relationship("Degree", secondary=favorites)

    def __repr__(self):
        return '<User: {}>'.format(self.email)


class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.String(128))
    country = db.column(db.String(64))
    city = db.Column(db.String(64))
    degrees = db.relationship('Degree', backref='school', lazy='dynamic')

    def __repr__(self):
        return '<School: {}>'.format(self.name)

class Degree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.String(128))
    description = db.column(db.Text)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'))

    def __repr__(self):
        return '<Degree: {}>'.format(self.name)
