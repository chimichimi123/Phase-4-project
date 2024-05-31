# resources.py

from flask import request, jsonify, session
from flask_restful import Resource, reqparse, marshal_with, fields
from models import db, User, Book, Review, BookDetails
from flask_bcrypt import generate_password_hash

book_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'author': fields.String,
    'summary': fields.String,
    'cover_image_url': fields.String,
}

class BookResource(Resource):
    @marshal_with(book_fields)
    def get(self, id=None):
        if id:
            book = Book.query.get_or_404(id)
            return book
        else:
            books = Book.query.all()
            return books

    @marshal_with(book_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('author', type=str, required=True)
        parser.add_argument('summary', type=str)
        parser.add_argument('cover_image_url', type=str)
        data = parser.parse_args()

        new_book = Book(**data)
        db.session.add(new_book)
        db.session.commit()
        return new_book, 201

    @marshal_with(book_fields)
    def put(self, id):
        book = Book.query.get_or_404(id)
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('author', type=str)
        parser.add_argument('summary', type=str)
        parser.add_argument('cover_image_url', type=str)
        data = parser.parse_args()

        for key, value in data.items():
            if value is not None:
                setattr(book, key, value)
        
        db.session.commit()
        return book

    def delete(self, id):
        book = Book.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        return '', 204
    
class ReviewResource(Resource):
    def get(self, id=None):
        if id:
            review = Review.query.get_or_404(id)
            return jsonify(review.to_dict())
        else:
            reviews = Review.query.all()
            return jsonify([review.to_dict() for review in reviews])

    def post(self):
        data = request.get_json()
        if not data:
            return {"error": "Invalid input"}, 400
        new_review = Review(**data)
        db.session.add(new_review)
        db.session.commit()
        return jsonify(new_review.to_dict()), 201

    def put(self, id):
        review = Review.query.get_or_404(id)
        data = request.get_json()
        if not data:
            return {"error": "Invalid input"}, 400
        for key, value in data.items():
            setattr(review, key, value)
        db.session.commit()
        return jsonify(review.to_dict())

    def delete(self, id):
        review = Review.query.get_or_404(id)
        db.session.delete(review)
        db.session.commit()
        return '', 204

class UserResource(Resource):
    def get(self, id=None):
        if id:
            user = User.query.get_or_404(id)
            return jsonify(user.to_dict())
        else:
            users = User.query.all()
            return jsonify([user.to_dict() for user in users])

    def post(self):
        data = request.get_json()
        if not data:
            return {"error": "Invalid input"}, 400
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201

    def put(self, id):
        user = User.query.get_or_404(id)
        data = request.get_json()
        if not data:
            return {"error": "Invalid input"}, 400
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return jsonify(user.to_dict())

    def delete(self, id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

class BookDetailsResource(Resource):
    def get(self, id=None):
        if id:
            details = BookDetails.query.get_or_404(id)
            return jsonify(details.to_dict())
        else:
            # Handle request to fetch all book details if ID is not provided
            details = BookDetails.query.all()
            return jsonify([details.to_dict() for details in details])

    def post(self):
        data = request.get_json()
        if not data:
            return {"error": "Invalid input"}, 400
        new_details = BookDetails(**data)
        db.session.add(new_details)
        db.session.commit()
        return jsonify(new_details.to_dict()), 201

    def put(self, id):
        details = BookDetails.query.get_or_404(id)
        data = request.get_json()
        if not data:
            return {"error": "Invalid input"}, 400
        for key, value in data.items():
            setattr(details, key, value)
        db.session.commit()
        return jsonify(details.to_dict())

    def delete(self, id):
        details = BookDetails.query.get_or_404(id)
        db.session.delete(details)
        db.session.commit()
        return '', 204

class Login(Resource):
    def post(self):
        username = request.json.get('username')
        user = User.query.filter_by(username=username).first()
        if user:
            session['user_id'] = user.id
            return {'id': user.id, 'username': user.username}, 200
        return {'message': 'User not found'}, 404

class Logout(Resource):
    def delete(self):
        session.pop('user_id', None)
        return {}, 204

class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        if user_id:
            user = User.query.get(user_id)
            return {'id': user.id, 'username': user.username}, 200
        return {}, 401

class Signup(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return {"error": "Invalid input"}, 400

        # Extract user data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Check if username or email already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return {"error": "Username already exists"}, 409
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            return {"error": "Email already exists"}, 409

        # Hash the password
        hashed_password = generate_password_hash(password).decode('utf-8')

        # Create a new user with hashed password
        new_user = User(username=username, email=email, password_hash=hashed_password)

        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user.to_dict()), 201