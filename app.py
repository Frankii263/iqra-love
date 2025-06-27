from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/images')
def get_images():
    image_folder = os.path.join(app.static_folder, 'images')
    image_files = [
        f'images/{filename}' for filename in os.listdir(image_folder)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
    ]
    return jsonify(image_files)

    app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
