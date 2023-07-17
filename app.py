from flask import Flask ,jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app=Flask(__name__)
db=SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:krishna123@localhost/sample'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name= db.Column(db.String(50))
    mobile=db.Column(db.String(20),unique=True)
    created_at=db.Column(db.DateTime, server_default=db.func.now())
    updated_at=db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    image_url=db.Column(db.String(100))
    
    def __init__(self, first_name, last_name, mobile, image_url=None):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.image_url = image_url
        
        
#for reading the data in the fields
@app.route('/users', methods=['GET'])
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
        
#creating an id and entering the details      
@app.route('/users/create', methods=['POST'])
def create_user():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    mobile = data.get('mobile')
    image_url = data.get('image_url')

    if not first_name or not last_name or not mobile:
        return jsonify(error='Missing required fields'), 400

    new_user = User(first_name=first_name, last_name=last_name, mobile=mobile, image_url=image_url)
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



#updating the table
@app.route('/users/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify(error='User not found'), 404

    data = request.get_json()
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

#delete
@app.route('/users/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify(error='User not found'), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify(message='User deleted'), 200


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)

