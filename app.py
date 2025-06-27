from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os

app = Flask(__name__)
app.secret_key = 'secret_key_here'

USERNAME = 'sahilkijanpari'
PASSWORD = 'parikijansahil'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect('/home')
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/home')
def home():
    if not session.get('logged_in'):
        return redirect('/')
    return render_template('index.html')

@app.route('/images')
def get_images():
    if not session.get('logged_in'):
        return redirect('/')
    image_folder = os.path.join(app.static_folder, 'images')
    image_files = [
        f'images/{filename}' for filename in os.listdir(image_folder)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
    ]
    return jsonify(image_files)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
