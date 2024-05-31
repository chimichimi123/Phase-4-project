from flask import request, jsonify, session
from flask_restful import Resource
from models import User, Book, Review, BookDetails
from flask_bcrypt import generate_password_hash
from werkzeug.security import check_password_hash
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
        new_user = User(username=data['username'], password_hash=hashed_password)
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
    
class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()

        if user and check_password_hash(user.password_hash, data['password']):
            session['user_id'] = user.id
            return jsonify(user.to_dict()), 200

        return {"message": "Invalid username or password"}, 401




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

        username = data.get('username')
        password = data.get('password')

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return {"error": "Username already exists"}, 409

        hashed_password = generate_password_hash(password).decode('utf-8')

        new_user = User(username=username, password_hash=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user.to_dict()), 201