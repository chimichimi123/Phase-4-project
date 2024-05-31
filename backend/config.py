# config.py

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
api = Api()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__)

    # Provide the database URI directly as a string
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Corrected
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.json.compact = False

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    CORS(app)

    return app

# Create the Flask app instance
app = create_app()
