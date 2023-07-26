from app import app
from datetime import timedelta
from flask_jwt_extended import JWTManager, jwt_required,create_access_token,get_jwt_identity


class credentials:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:krishna123@localhost/sample'
    app.config['JWT_SECRET_KEY'] = 'Krishna#9795 ' 
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)


