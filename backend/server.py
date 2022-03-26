from flask import request, jsonify, Flask
from flask_cors import CORS, cross_origin
import json

from utils import get_job_data

DB_PATH = './data/data.json'
CREATOR_TO_ID_PATH = './data/creator_to_id.json'
app = Flask(__name__)

CORS(app)

@app.route('/api/v0/', methods=['POST'])
def query():
    
    return "hi"

@app.route('/api/v0/', methods=['GET'])
def index():
    return "<p>Plantain API running!</p>"

if __name__ == '__main__':
    app.run(debug=False)

    