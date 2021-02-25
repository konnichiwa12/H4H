import os
from app import db
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class User(db.Model):
    __tablename__="users"
    #usr_id = db.Column("ID", db.Integer, primary_key=True)
    usr_name = db.Column("username", db.String(100), nullable=True, primary_key=True)
    name = db.Column("name", db.String(100), nullable = True)
    usr_email = db.Column("email", db.String(100), nullable =True)
    usr_pwd = db.Column("password", db.String(100), nullable=True)
    #date_joined = db.Column(db.DateTime, nullable=False)
    #businesses = db.relationship("Business", back_populates="owner")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.date_joined = datetime.now()


class Business(db.Model):
    __tablename__="businesses"
    #busn_id = db.Column("ID", db.Integer, primary_key=True)
    busn_name = db.Column("name", db.String(100), primary_key=True)
    #busn_pwd = db.Column("password", db.Unicode, nullable=True)
    busn_des = db.Column("description", db.String(255), nullable=True)
    busn_add = db.Column("address", db.String(255), nullable=True)
    busn_type = db.Column("type", db.String(100), nullable=True)
    #owner_id = db.Column("Owner ID", db.Integer, db.ForeignKey('owner.usr_id'), nullable = False)
    #owner = db.relationship("owner", back_populates="businesses")
    #date_added = db.Column(db.DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.date_added = datetime.now()


