from app import app



class credentials:
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:krishna123@localhost/sample'
app.config['JWT_SECRET_KEY'] = 'Krishna#9795 ' 
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)


