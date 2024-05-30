#app.py

# Remote library imports
from flask import jsonify, request 
from flask_restful import Resource
from flask_cors import CORS
from flask_restful import Api
from schemas import BookSchema
from models import Book


# Local imports
from config import create_app, db

app = create_app()
CORS(app)
api = Api(app)


book_schema = BookSchema()
books_schema = BookSchema(many=True)

class BookResource(Resource):
    def get(self, id=None):
        if id:
            book = Book.query.get_or_404(id)
            return jsonify(book_schema.dump(book))
        else:
            books = Book.query.all()
            return jsonify(books_schema.dump(books))

    def post(self):
        data = request.get_json()
        if not data:
            return {"error": "Invalid input"}, 400
        new_book = Book(**data)
        db.session.add(new_book)
        db.session.commit()
        return jsonify(book_schema.dump(new_book)), 201

if __name__ == '__main__':
    app.run(port=5555, debug=True)