from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from .models import User, Book, Review, UserBook, BookDetails

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True

class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        include_relationships = True
        load_instance = True

class ReviewSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        include_relationships = True
        load_instance = True

class UserBookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserBook
        include_relationships = True
        load_instance = True

class BookDetailsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BookDetails
        include_relationships = True
        load_instance = True
