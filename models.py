from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required,create_access_token,get_jwt_identity

from app import db


class User_log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    
    def __init__(self,username,password):
        self.username=username
        self.password=password
    
    pass  


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(50))
    last_name= db.Column(db.String(50))
    mobile=db.Column(db.String(20),unique=True)
    created_at=db.Column(db.DateTime, server_default=db.func.now())
    updated_at=db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    image_url=db.Column(db.String(100))
    

    def __init__(self,username,first_name, last_name, mobile, image_url=None):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.image_url = image_url
        
    pass