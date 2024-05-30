
# Remote library imports
from flask_cors import CORS

# Local imports
from config import create_app

app = create_app()
CORS(app)

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)