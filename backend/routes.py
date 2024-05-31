from flask_restful import Api
from flask_cors import CORS
from resources import BookResource, ReviewResource, UserResource, BookDetailsResource, Logout, CheckSession, Signup, Login

def setup_routes(app):
    api = Api(app)

    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    api.add_resource(BookResource, '/books', '/books/<int:id>')
    api.add_resource(ReviewResource, '/reviews', '/reviews/<int:id>')
    api.add_resource(UserResource, '/users', '/users/<int:id>')
    api.add_resource(BookDetailsResource, '/bookdetails', '/bookdetails/<int:id>')
    api.add_resource(Logout, '/logout')
    api.add_resource(CheckSession, '/checksession')
    api.add_resource(Signup, '/signup')
    api.add_resource(Login, '/login')


    