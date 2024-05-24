from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import pdb

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
    if username in users and check_password_hash(users.get(username), password):
        return username

@auth.error_handler
def unauthorized():
    return jsonify({"message": "Unauthorized access"}), 401

@app.route('/')
@auth.login_required
def home():
    return jsonify({"message": "Hello world"})

@app.route("/rest/<method>", methods = ['GET'])
@auth.login_required
def rest_api_data(method):
    country_code = request.args.get('countryCode')
    language_code = request.args.get('languageCode')
    search_text = request.args.get('searchText')

    if auth.current_user() is None:
        return jsonify({"message": "UNAuthorised User"}), 403
    if not country_code:
        return jsonify({"message": "Missing Country code!"}), 400
    if country_code == "RU":
        return jsonify({"message": "Sorry, Access to Russia is forbidden!"}), 403

    # check user has permissions for country
    if country_code not in user_allowed_countries[auth.current_user()]:
        return jsonify({"message": "Sorry, user doesnt have permissions to access this country"}), 403

    return_message = f"The server found this message {search_text} for country {country_code} {language_code=}"
    return jsonify({"message": return_message}),200


if __name__ == '__main__':
    app.run(debug=True)