#routes.py

from flask import Blueprint, request, jsonify
from flask_restful import Api
from flask_cors import CORS
from functools import wraps
from .config import SECRET_KEY
import jwt

from resources import BookResource, ReviewResource, UserResource, BookDetailsResource, Logout, CheckSession, Signup

routes = Blueprint('routes', __name__)

users = {
    'user1': {
        'username': 'Chimi',
        'password': 'password'
    }
}

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user = data['username']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

        return func(current_user, *args, **kwargs)

    return decorated

@routes.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Could not verify'}), 401

    username = auth.username
    password = auth.password

    if username in users and users[username]['password'] == password:
        token = jwt.encode({'username': username}, SECRET_KEY, algorithm='HS256')
        return jsonify({'token': token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401

@routes.route('/protected')
@token_required
def protected(current_user):
    return jsonify({'message': f'Hello, {current_user}!'})

def setup_routes(api, app):
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    api.add_resource(BookResource, '/books', '/books/<int:id>')
    api.add_resource(ReviewResource, '/reviews', '/reviews/<int:id>')
    api.add_resource(UserResource, '/users', '/users/<int:id>')
    api.add_resource(BookDetailsResource, '/bookdetails', '/bookdetails/<int:id>')
    api.add_resource(Logout, '/logout')
    api.add_resource(CheckSession, '/checksession')
    api.add_resource(Signup, '/signup')
