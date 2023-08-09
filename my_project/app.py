from flask import Flask
from datetime import timedelta
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from url import app_routes

app=Flask(__name__)
db=SQLAlchemy()
jwt = JWTManager(app) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:krishna123@localhost/sample'
app.config['JWT_SECRET_KEY'] = 'Krishna#9795 ' 
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

db.init_app(app)
with app.app_context():
    db.create_all()




if __name__ == '__main__':
    app_routes(app)
    app.run(debug=True)