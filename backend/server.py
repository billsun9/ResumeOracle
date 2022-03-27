from flask import request, jsonify, Flask
from flask_cors import CORS, cross_origin
import json
import os
from werkzeug.utils import secure_filename

from utils import get_job_data
from resume_parser import resume_parser

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["UPLOAD_FOLDER"] = "./data"
CORS(app)

@app.route('/api/v0/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return "<p>Plantain API running!</p>"
    elif request.method == 'POST':
        file = request.files['file']
        fname = secure_filename(file.filename)
        user_path = os.path.join(app.config["UPLOAD_FOLDER"], fname)
        file.save(user_path)
        skills = resume_parser(user_path)
        
        res = []
        # hacky method
        if 'Python' in skills: res.extend(get_job_data("python"))
        if 'Java' in skills: res.extend(get_job_data("java"))
        if 'Javascript' in skills: res.extend(get_job_data("python"))
        if 'Sql' in skills: res.extend(get_job_data("sql"))
        if 'Html' in skills: res.extend(get_job_data("html"))
        return {"msg": "AYO", "skills": skills, "payload": res}
    else:
        return "<p>Wrong Method</p>"
    
@app.route('/api/v0/pull', methods=['POST'])
def pull():
    if request.method == 'POST':
        
        search_query = request.get_json()["search_query"]
        
        return {"msg": "OK", "data": get_job_data(search_query)}

if __name__ == '__main__':
    app.run(debug=False)