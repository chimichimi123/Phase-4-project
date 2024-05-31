# models.py

from config import db
from sqlalchemy import func
from sqlalchemy import CheckConstraint
from flask_bcrypt import generate_password_hash, check_password_hash


# Models go here!

class TimestampMixin:
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class User(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    reviews = db.relationship('Review', backref='user', lazy=True)
    books = db.relationship('UserBook', backref='user', lazy=True)
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }

class Book(db.Model, TimestampMixin):
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
            'details': self.details.to_dict() if self.details else None,
            'reviews': [review.to_dict() for review in self.reviews],
        }

class Review(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    rating = db.Column(db.Integer, CheckConstraint('rating >= 1 and rating <= 5'), nullable=False)
    comment = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'book_id': self.book_id,
            'rating': self.rating,
            'comment': self.comment,
            'user': self.user.to_dict() if self.user else None,
        }

class UserBook(db.Model, TimestampMixin):
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
        
class BookDetails(db.Model, TimestampMixin):
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