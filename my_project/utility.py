from flask import request ,jsonify
import os
import uuid
from werkzeug.utils import secure_filename 
import datetime


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

