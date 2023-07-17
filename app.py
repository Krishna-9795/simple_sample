from flask import Flask ,jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app=Flask(__name__)
db=SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:krishna123@localhost/sample'

class User(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(50))
    Last_name= db.Column(db.String(50))
    Mobile=db.Column(db.Integer,unique=True)
    Created_at=db.Column(db.DateTime, server_default=db.func.now())
    Updated_at=db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    image=db.column(db.String(100))
    
    def __init__(self, first_name, last_name, mobile, image=None):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.image = image
        
        
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
            'image': user.image
        })
    return jsonify(result), 200
        
#creating an id and entering the details      
@app.route('/users/create', methods=['POST'])
def create_user():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    mobile = data.get('mobile')
    image = data.get('image')

    if not first_name or not last_name or not mobile:
        return jsonify(error='Missing required fields'), 400

    new_user = User(first_name=first_name, last_name=last_name, mobile=mobile, image=image)
    db.session.add(new_user)
    db.session.commit()
    
    result = {
        'id': new_user.id,
        'first_name': new_user.first_name,
        'last_name': new_user.last_name,
        'mobile': new_user.mobile,
        'created_at': new_user.created_at,
        'updated_at': new_user.updated_at,
        'image': new_user.image
    }
    return jsonify(result), 201



#updating the table
@app.route('/users/update', methods=['PUT'])
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
        'updated_at': user.updated_at
    }
    return jsonify(result), 200

#delete
@app.route('/users/delete', methods=['DELETE'])
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

