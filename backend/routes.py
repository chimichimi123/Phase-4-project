# routes.py
from flask import request, jsonify, Blueprint
from models import db, User, Book, Review, UserBook

bp = Blueprint('routes', __name__)


@bp.route('/books', methods=['GET', 'POST'])
def handle_books():
    if request.method == 'POST':
        data = request.get_json()
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
        for key, value in data.items():
            setattr(book, key, value)
        db.session.commit()
        return jsonify(book.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(book)
        db.session.commit()
        return '', 204

# DONT FORGET ad the reviews route and the route for users

def register_routes(app):
    app.register_blueprint(bp)