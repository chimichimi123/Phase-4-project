#views.py

from schemas import UserSchema, BookSchema, ReviewSchema, UserBookSchema, BookDetailsSchema
from models import Book, User

# Create schema instances
user_schema = UserSchema()
book_schema = BookSchema()
review_schema = ReviewSchema()
user_book_schema = UserBookSchema()
book_details_schema = BookDetailsSchema()

# Example: Serialize a user instance
user_instance = User.query.get(1)
user_data = user_schema.dump(user_instance)

# Example: Serialize a list of book instances
book_instances = Book.query.all()
books_data = book_schema.dump(book_instances, many=True)

# Example: Deserialize JSON data to a user instance
json_data = {"username": "john_doe", "email": "john@example.com"}
user_instance = user_schema.load(json_data)