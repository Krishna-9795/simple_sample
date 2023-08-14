def app_routes(app,db):

    from flask import jsonify, request
    from flask_jwt_extended import jwt_required
    #from utility import  get_users, upload
    import utility
    #from auth import register,login, update_user, delete_user, create_user,get_user_profile,get_users
    import auth      
    @app.route('/register', methods=['POST'])
    def register_user():
        return auth.register("username","password")
    @app.route('/login',methods=['POST'])
    def login_user():
        return auth.login()

            

    @app.route('/profile', methods=['GET'])
    @jwt_required()
    def get_profile():
        return auth.get_user_profile()


            
    #for reading the data in the fields
    @app.route('/users', methods=['GET']) 
    @jwt_required()
    def get_all_users():
        return auth.get_users()




    #creating an id and entering the details      
    @app.route('/users/create', methods=['POST'])
    @jwt_required()
    def create_new_user():
        return auth.create_user()


    #uploading images
    @app.route('/uploads', methods=['POST'])
    def upload_image():
        return utility.upload()
    def generate_unique_filename(filename):
        return utility.generate_unique_filename()



    #updating the table
    @app.route('/users/update/<int:user_id>', methods=['PUT'])
    def update_existing_user(user_id):
        return auth.update_user(user_id)

    #delete
    @app.route('/users/delete/<int:user_id>', methods=['DELETE'])
    def delete_existing_user(user_id):
        return auth.delete_user(user_id)
