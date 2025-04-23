import os
from flask import Flask, request, jsonify

from flask_cors import CORS


app = Flask(__name__)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))