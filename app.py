from flask import Flask ,jsonify, request
from datetime import datetime
import os
import uuid
from werkzeug.utils import secure_filename  
import datetime
from flask_jwt_extended import JWTManager, jwt_required,create_access_token,get_jwt_identity
from datetime import timedelta
from utils import *
from configs import credentials


app=Flask(__name__)
db=SQLAlchemy()
jwt = JWTManager(app) 

        
@app.route('/register', methods=['POST'])
def register():
@app.route('/login',methods=['POST'])
def login():
        

@app.route('/profile', methods=['GET'])
@jwt_required()
def get_user_profile():
        
#for reading the data in the fields
@app.route('/users', methods=['GET'])
@jwt_required()
def get_users():



#creating an id and entering the details      
@app.route('/users/create', methods=['POST'])
@jwt_required()
def create_user():

#uploading images
@app.route('/uploads', methods=['POST'])
def generate_unique_filename(filename):
def upload():

#updating the table
@app.route('/users/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):

#delete
@app.route('/users/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):



