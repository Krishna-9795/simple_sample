
def app_routes(app):

    from flask import jsonify, request
    from flask_jwt_extended import jwt_required
    from utility import register, login, get_user_profile, get_users, create_user, upload, update_user, delete_user



            
    @app.route('/register', methods=['POST'])
    def register():
        return register()
    @app.route('/login',methods=['POST'])
    def login_user():
        return login()

            

    @app.route('/profile', methods=['GET'])
    @jwt_required()
    def get_profile():
        return get_user_profile()


            
    #for reading the data in the fields
    @app.route('/users', methods=['GET']) 
    @jwt_required()
    def get_all_users():
        return get_users()




    #creating an id and entering the details      
    @app.route('/users/create', methods=['POST'])
    @jwt_required()
    def create_new_user():
        return create_user()


    #uploading images
    @app.route('/uploads', methods=['POST'])
    def generate_unique_filename(filename):
        return generate_unique_filename()
    def upload_image():
        return upload()



    #updating the table
    @app.route('/users/update/<int:user_id>', methods=['PUT'])
    def update_existing_user(user_id):
        return update_user(user_id)

    #delete
    @app.route('/users/delete/<int:user_id>', methods=['DELETE'])
    def delete_existing_user(user_id):
        return delete_user(user_id)
