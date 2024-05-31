from flask import request, jsonify, session
from flask_restful import Resource, reqparse
from models import User, Book, Review, BookDetails
from flask_bcrypt import generate_password_hash
from config import db

class BookResource(Resource):
    def get(self, id=None):
        if id:
            book = Book.query.get_or_404(id)
            return jsonify(book.to_dict())
        else:
            books = Book.query.all()
            return jsonify([book.to_dict() for book in books])

    def post(self):
        data = request.get_json()
        new_book = Book(**data)
        db.session.add(new_book)
        db.session.commit()
        return jsonify(new_book.to_dict()), 201

    def put(self, id):
        book = Book.query.get_or_404(id)
        data = request.get_json()
        for key, value in data.items():
            setattr(book, key, value)
        db.session.commit()
        return jsonify(book.to_dict())

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
        new_review = Review(**data)
        db.session.add(new_review)
        db.session.commit()
        return jsonify(new_review.to_dict()), 201

    def put(self, id):
        review = Review.query.get_or_404(id)
        data = request.get_json()
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
    def post(self):
        data = request.get_json()
        hashed_password = generate_password_hash(data['password']).decode('utf-8')
        new_user = User(username=data['username'], email=data['email'], password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201

class BookDetailsResource(Resource):
    def get(self, id=None):
        if id:
            details = BookDetails.query.get_or_404(id)
            return jsonify(details.to_dict())
        else:
            details = BookDetails.query.all()
            return jsonify([details.to_dict() for details in details])

    def post(self):
        data = request.get_json()
        new_details = BookDetails(**data)
        db.session.add(new_details)
        db.session.commit()
        return jsonify(new_details.to_dict()), 201

    def put(self, id):
        details = BookDetails.query.get_or_404(id)
        data = request.get_json()
        for key, value in data.items():
            setattr(details, key, value)
        db.session.commit()
        return jsonify(details.to_dict())

    def delete(self, id):
        details = BookDetails.query.get_or_404(id)
        db.session.delete(details)
        db.session.commit()
        return '', 204
    
class FavoriteBookResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('userId', type=int, required=True, help="User ID is required")
    parser.add_argument('bookId', type=int, required=True, help="Book ID is required")

    def post(self):
        data = FavoriteBookResource.parser.parse_args()
        user_id = data['userId']
        book_id = data['bookId']

        user = User.query.get(user_id)
        book = Book.query.get(book_id)

        if not user or not book:
            return {'error': 'User or Book not found'}, 404

        if book in user.favorite_books:
            return {'message': 'Book already in favorites'}, 400

        user.favorite_books.append(book)
        db.session.commit()

        return {'message': 'Book added to favorites'}, 200


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