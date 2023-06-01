from flask import Flask, render_template, request, redirect, jsonify
import hashlib
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(16)

hashed_passwords = []


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', hashed_passwords=hashed_passwords)


@app.route('/encrypt', methods=['POST'])
def encrypt():
    password = request.form['password']
    if password:
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        hashed_passwords.append(hashed_password)
    return redirect('/')


@app.route('/api_list', methods=['GET'])
def api_content():
    return jsonify(hashed_passwords)


if __name__ == '__main__':
    app.run(debug=True)
