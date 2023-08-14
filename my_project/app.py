from flask import Flask
from datetime import timedelta
from flask_jwt_extended import JWTManager
from db import db



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:krishna123@localhost/sample'
app.config['JWT_SECRET_KEY'] = 'Krishna#9795 ' 
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

jwt = JWTManager(app) 

db.init_app(app)

import url
url.app_routes(app,db)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)