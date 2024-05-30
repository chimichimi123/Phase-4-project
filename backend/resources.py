# resources.py

from flask import request, jsonify
from flask_restful import Resource
from models import db, User, Book, Review, BookDetails

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
        if not data:
            return {"error": "Invalid input"}, 400
        new_book = Book(**data)
        db.session.add(new_book)
        db.session.commit()
        return jsonify(new_book.to_dict()), 201

    def put(self, id):
        book = Book.query.get_or_404(id)
        data = request.get_json()
        if not data:
            return {"error": "Invalid input"}, 400
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


