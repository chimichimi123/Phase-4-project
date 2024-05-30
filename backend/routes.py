# routes.py
from flask import request, jsonify, Blueprint
from models import db, User, Book, Review, UserBook, BookDetails

bp = Blueprint('api', __name__)

@bp.route('/books', methods=['GET', 'POST'])
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

@bp.route('/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
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
    
@bp.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    new_review = Review(**data)
    db.session.add(new_review)
    db.session.commit()
    return jsonify(new_review.to_dict()), 201

@bp.route('/reviews/<int:id>', methods=['GET', 'PUT', 'DELETE'])
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

@bp.route('/users', methods=['GET', 'POST'])
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

@bp.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
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

@bp.route('/bookdetails', methods=['GET', 'POST'])
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

@bp.route('/bookdetails/<int:id>', methods=['GET', 'PUT', 'DELETE'])
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

def register_routes(app):
    app.register_blueprint(bp)
