# models.py

from config import db


# Models go here!

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    reviews = db.relationship('Review', backref='user', lazy=True)
    books = db.relationship('UserBook', backref='user', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    summary = db.Column(db.String(500))
    cover_image_url = db.Column(db.String(200))
    reviews = db.relationship('Review', backref='book', lazy=True)
    users = db.relationship('UserBook', backref='book', lazy=True)
    details = db.relationship('BookDetails', backref='book', uselist=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'summary': self.summary,
            'cover_image_url': self.cover_image_url,
        }

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'user_id': self.user_id,
            'book_id': self.book_id,
        }

class UserBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    role = db.Column(db.String(50))

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'role': self.role,
        }
        
class BookDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    genre = db.Column(db.String(50))
    year = db.Column(db.Integer)
    pages = db.Column(db.Integer)
    publisher = db.Column(db.String(50))
    description = db.Column(db.String(500))

    def to_dict(self):
        return {
            'id': self.id,
            'book_id': self.book_id,
            'genre': self.genre,
            'year': self.year,
            'pages': self.pages,
            'publisher': self.publisher,
            'description': self.description,
        }