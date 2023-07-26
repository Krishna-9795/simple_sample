from flask import Flask ,jsonify, request
from datetime import datetime


from flask_jwt_extended import JWTManager, jwt_required,create_access_token,get_jwt_identity

from utils import *
from configs import credentials

app=Flask(__name__)
db=SQLAlchemy()
jwt = JWTManager(app) 

        
@app.route('/register', methods=['POST'])
def register():
    return jsonify({'message': ''})
@app.route('/login',methods=['POST'])
def login():
    return jsonify({'message': ''})
        

@app.route('/profile', methods=['GET'])
@jwt_required()
def get_user_profile():
    return jsonify({'message': ''})
        
#for reading the data in the fields
@app.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    return jsonify({'message': ''})



#creating an id and entering the details      
@app.route('/users/create', methods=['POST'])
@jwt_required()
def create_user():
    return jsonify({'message': ''})

#uploading images
@app.route('/uploads', methods=['POST'])

def upload():
    return jsonify({'message': ''})
def generate_unique_filename(filename):
    return jsonify({'message': ''})

#updating the table
@app.route('/users/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return jsonify({'message': ''})
#delete
@app.route('/users/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return jsonify({'message': ''})



