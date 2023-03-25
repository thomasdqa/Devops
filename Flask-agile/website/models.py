from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#4 table database


class Service_request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    admin = db.Column(db.String, nullable=False)
    service_requests = db.relationship(Service_request)

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    service_requests = db.relationship('Service_request')

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    service_requests = db.relationship('Service_request')








