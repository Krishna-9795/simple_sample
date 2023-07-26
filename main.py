
from app import app
from flask_migrate import Migrate
from app import db


migrate = Migrate(app , db)



if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)