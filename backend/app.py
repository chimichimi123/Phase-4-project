#app.py

# Remote library imports
from flask_cors import CORS
from flask_restful import Api


# Local imports
from config import create_app
from routes import api_bp

app = create_app()
CORS(app)
api = Api(app)

app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(port=5000, debug=True)