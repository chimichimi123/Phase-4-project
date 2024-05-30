#app.py

# Remote library imports
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
from flask_restful import Api
from resources import BookResource, ReviewResource, UserResource, BookDetailsResource


# Local imports
from config import create_app, db

app = create_app()
CORS(app)
api = Api(app)

api.add_resource(BookResource, '/books', '/books/<int:id>')
api.add_resource(ReviewResource, '/reviews', '/reviews/<int:id>')
api.add_resource(UserResource, '/users', '/users/<int:id>')
api.add_resource(BookDetailsResource, '/bookdetails', '/bookdetails/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)