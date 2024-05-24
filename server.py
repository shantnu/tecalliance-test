from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": generate_password_hash("password1"),
    "user2": generate_password_hash("password2"),
}

user_allowed_countries = {
    "user1": ["US", "UK", "DE"],
    "user2": ["UK", "IN"],
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(password, users[username]):
        return username

@auth.error_handler
def unauthorized():
    return jsonify({"message": "Unauthorized access"}), 401

@app.route('/')
@auth.login_required
def home():
    return jsonify({"message": "Hello world"})


if __name__ == '__main__':
    app.run(debug=True)