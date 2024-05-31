from flask import Blueprint
from flask_restful import Api
from resources import BookResource, ReviewResource, UserResource, BookDetailsResource, Login, Logout, CheckSession, Signup

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(BookResource, '/books', '/books/<int:id>')
api.add_resource(ReviewResource, '/reviews', '/reviews/<int:id>')
api.add_resource(UserResource, '/users', '/users/<int:id>')
api.add_resource(BookDetailsResource, '/bookdetails', '/bookdetails/<int:id>')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Signup, '/signup')