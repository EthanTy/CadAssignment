from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class lostfound(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Imglink = db.Column(db.VarChar(200))
    Item=db.Column(db.VarChar(45))
    DateofReport = db.Column(db.Date)
    Description=db.Column(db.VarChar(200))
    Category = db.Column(db.VarChar(50))

class admin(db.Model, UserMixin):
    idadmin = db.Column(db.Integer, primary_key=True)
    adminemail = db.Column(db.VarChar(100), unique=True)
    adminpassword = db.Column(db.VarChar(45))

class suscribers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.VarChar(45), unique=True)
    sname = db.Column(db.VarChar(45))
    type = db.Column(db.VarChar(45))
    category = db.Column(db.VarChar(45))

