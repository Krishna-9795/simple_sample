from app import app,db
from flask import request , jsonify
from models import User ,User_log 
import os
import uuid
from werkzeug.utils import secure_filename 
import datetime
from flask_jwt_extended import JWTManager, jwt_required,create_access_token,get_jwt_identity

#for registering
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400

    present_user = User_log.query.filter_by(username=username).first()
    if present_user:
        return jsonify({'message': 'Username already exists. Please choose a different username.'}), 400
    new_user = User_log(username, password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'})

#login
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User_log.query.filter_by(username=username).first()

    if not user or user.password != password:
        return jsonify({'message': 'Invalid username or password.'}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200

#Profile
def get_user_profile():
    user_id = get_jwt_identity()
    user_log = User_log.query.get(user_id)

    if not user_log:
        return jsonify({'message': 'User not found'}), 404
    user=User.query.filter_by(username=user_log.username).first()
    
    if not user:
        return jsonify({'message': 'Invalid username or password.'}), 401
    
    profile_data = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'mobile': user.mobile,
        'image_url': user.image_url
    }

    return jsonify(profile_data), 200

#getting users data
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'mobile': user.mobile,
            'created_at': user.created_at,
            'updated_at': user.updated_at,
            'image_url': user.image_url
        })
    return jsonify(result), 200

#creating user
def create_user():
    data = request.get_json()
    username=data.get('username')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    mobile = data.get('mobile')
    image_url = data.get('image_url')
    

    if not first_name or not last_name or not mobile:
        return jsonify(error='Missing required fields'), 400

    new_user = User(username=username,first_name=first_name, last_name=last_name, mobile=mobile, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()
    
    result = {
        'id': new_user.id,
        'first_name': new_user.first_name,
        'last_name': new_user.last_name,
        'mobile': new_user.mobile,
        'created_at': new_user.created_at,
        'updated_at': new_user.updated_at,
        'image_url': new_user.image_url
    }
    return jsonify(result), 201

#uploads images
def upload():
    file = request.files['image']
    if file:
        filename = secure_filename(file.filename)#type:ignore
        unique_filename = generate_unique_filename(filename)
        file.save(os.path.join('uploads', unique_filename))
        return 'Image uploaded successfully!'
    return 'No image file provided.'
#func for generating unique filename
def generate_unique_filename(filename):
    unique_id = str(uuid.uuid4().hex)
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    _, extension = os.path.splitext(filename)
    unique_filename = f"{timestamp}_{unique_id}{extension}"
    return unique_filename

#updating user
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if not user:
        return jsonify(error='User not found'), 404

    user.id = data.get('id',user.id)
    user.username=data.get('username',user.username)
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.mobile = data.get('mobile', user.mobile)
    
    db.session.commit()

    result = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'mobile': user.mobile,
        'created_at': user.created_at,
        'updated_at': user.updated_at,
        'image_url':user.image_url
    }
    return jsonify(result), 200

#delete function
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify(error='User not found'), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify(message='User deleted'), 200
