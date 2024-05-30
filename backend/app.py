#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, Flask
from flask_restful import Resource
from flask_cors import CORS

# Local imports
from config import db, api, create_app
from routes import register_routes  # Import the register_routes function

app = create_app()
CORS(app)

# Register the routes from routes.py
register_routes(app)

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)