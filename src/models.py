import flask_sqlalchemy
from flask_login import UserMixin
db = flask_sqlalchemy.SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    keyvalue = db.relationship("KeyValue", backref="userkeyvalue")

class KeyValue(db.Model):
    __tablename__ = 'keyvalue'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100))
    value = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

