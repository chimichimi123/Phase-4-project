from marshmallow import Schema, fields, validate

class BookSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    author = fields.String(required=True)
    summary = fields.String()
    cover_image_url = fields.String()

    # Optional: You can add validation to fields
    title = fields.String(required=True, validate=validate.Length(min=1))
    author = fields.String(required=True, validate=validate.Length(min=1))
    summary = fields.String(validate=validate.Length(max=500))
    cover_image_url = fields.String(validate=validate.URL())

class ReviewSchema(Schema):
    id = fields.Integer(dump_only=True)
    book_id = fields.Integer()
    rating = fields.Integer(validate=validate.Range(min=1, max=5))
    comment = fields.String()
    user_id = fields.Integer()

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    email = fields.Email(required=True)
    
class BookDetailsSchema(Schema):
    id = fields.Integer(dump_only=True)
    book_id = fields.Integer()
    genre = fields.String()
    year = fields.Integer()
    pages = fields.Integer()
    publisher = fields.String()
    description = fields.String()
