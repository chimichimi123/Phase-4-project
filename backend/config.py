# config.py

# config.py

# Remote library imports
import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Define metadata, instantiate db
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
api = Api()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__)

    # Set configuration attributes
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.json.compact = False

    # Initialize plugins
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    CORS(app)

    # Import parts of our application
    from routes import register_routes
    register_routes(app)

    return app
