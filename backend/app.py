#app.py

# Remote library imports
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, User, Book, Review, BookDetails

# Local imports
from config import create_app

app = create_app()
CORS(app)


@app.route('/')
def index():
    return '<h1>Project Server</h1>'

@app.route('/books', methods=['GET', 'POST'])
def handle_books():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400
        new_book = Book(**data)
        db.session.add(new_book)
        db.session.commit()
        return jsonify(new_book.to_dict()), 201
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route('/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_book(id):
    book = Book.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(book.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400
        for key, value in data.items():
            setattr(book, key, value)
        db.session.commit()
        return jsonify(book.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(book)
        db.session.commit()
        return '', 204

@app.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    new_review = Review(**data)
    db.session.add(new_review)
    db.session.commit()
    return jsonify(new_review.to_dict()), 201

@app.route('/reviews/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_review(id):
    review = Review.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(review.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400
        for key, value in data.items():
            setattr(review, key, value)
        db.session.commit()
        return jsonify(review.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(review)
        db.session.commit()
        return '', 204

@app.route('/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(user.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return jsonify(user.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return '', 204

@app.route('/bookdetails', methods=['GET', 'POST'])
def handle_bookdetails():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400
        new_details = BookDetails(**data)
        db.session.add(new_details)
        db.session.commit()
        return jsonify(new_details.to_dict()), 201
    bookdetails = BookDetails.query.all()
    return jsonify([details.to_dict() for details in bookdetails])

@app.route('/bookdetails/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_bookdetail(id):
    details = BookDetails.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify(details.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400
        for key, value in data.items():
            setattr(details, key, value)
        db.session.commit()
        return jsonify(details.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(details)
        db.session.commit()
        return '', 204

if __name__ == '__main__':
    app.run(port=5555, debug=True)