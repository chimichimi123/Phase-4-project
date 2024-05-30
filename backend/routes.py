# routes.py
from flask import request, jsonify, Blueprint
from models import db, User, Book, Review, BookDetails

book_bp = Blueprint('book', __name__)

@book_bp.route('/books', methods=['GET', 'POST'])
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

@book_bp.route('/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
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
    
review_bp = Blueprint('review', __name__)
    
@review_bp.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    new_review = Review(**data)
    db.session.add(new_review)
    db.session.commit()
    return jsonify(new_review.to_dict()), 201

@review_bp.route('/reviews/<int:id>', methods=['GET', 'PUT', 'DELETE'])
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
    
user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET', 'POST'])
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

@user_bp.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
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
    
book_details_bp = Blueprint('book_details', __name__)

@book_details_bp.route('/bookdetails', methods=['GET', 'POST'])
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

@book_details_bp.route('/bookdetails/<int:id>', methods=['GET', 'PUT', 'DELETE'])
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
    app.register_blueprint(book_details_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(book_bp)
    app.register_blueprint(review_bp)
