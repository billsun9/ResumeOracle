from flask import request, jsonify, Flask
from flask_cors import CORS, cross_origin
import json

from utils import get_job_data
app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/api/v0/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return "<p>Plantain API running!</p>"
    elif request.method == 'POST':
        
        return {"msg": "AYO"}
    else:
        return "<p>Wrong Method</p>"
    
@app.route('/api/v0/pull', methods=['POST'])
def pull():
    if request.method == 'POST':
        
        search_query = request.get_json()["search_query"]
        
        return {"msg": "OK", "data": get_job_data(search_query)}

if __name__ == '__main__':
    app.run(debug=False)