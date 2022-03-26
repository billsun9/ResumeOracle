import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
import json

from utils import generate_uuid, write_json

DB_PATH = './data/data.json'
CREATOR_TO_ID_PATH = './data/creator_to_id.json'
app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/api/v0/', methods=['POST'])
def post():
    x = request.data
    y = json.loads(str(x, encoding='utf-8'))
    
    uuid = write_json(y)
    
    return {"msg":"success", "c_id":uuid}

@app.route('/api/v0/creator_info', methods=['GET'])
def get_all():
    json_file = open(DB_PATH, 'r')
    db = json.load(json_file)
    json_file.close()
    
    json_file = open(CREATOR_TO_ID_PATH, 'r')
    creator_to_id_db = json.load(json_file)
    json_file.close()
    
    return {"db": db, 
            "creator_to_id":creator_to_id_db}

@app.route('/api/v0/creator_info/<c_id>', methods=['GET'])
def get_specific(c_id):
    json_file = open(DB_PATH, 'r')
    db = json.load(json_file)
    json_file.close()
    try:
        x = db[c_id]
        return x
    except KeyError:
        return {"msg": "cant find creator!"}

@app.route('/api/v0/', methods=['GET'])
def index():
    return "<p>Plantain API running!</p>"

if __name__ == '__main__':
    app.run(debug=False)

    