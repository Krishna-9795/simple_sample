import base64
import os
import uuid
from flask import Flask ,request,jsonify
import datetime

with open('C:\\Users\\HP\\Desktop\\person-holds-a-book-over-a-stack-and-turns-the-page.jpg', 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    print(encoded_string)




@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    if 'image' in data:
        base64_image = data['image']
        image_data = base64.b64decode(base64_image)
        unique_filename = generate_unique_filename()
        image_path = os.path.join('uploads', unique_filename)
        os.makedirs('uploads', exist_ok=True)
        with open(image_path, 'wb') as image_file:
            image_file.write(image_data)
        return 'Image uploaded successfully!'
    return 'No image file provided.'

def generate_unique_filename():
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    random_id = str(uuid.uuid4().hex)
    filename = f"{timestamp}_{random_id}.jpg"
    return filename
