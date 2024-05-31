# app.py

from flask import Flask
from config import db, DATABASE_URI
from routes import setup_routes

def create_app():
    """Initialize the core application."""
    app = Flask(__name__)
    app.secret_key = 'super secret key'

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.json.compact = False

    db.init_app(app)

    # Initialize routes
    setup_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)
