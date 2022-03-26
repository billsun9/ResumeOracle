# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 13:35:08 2022

@author: Bill Sun
"""

import requests
import json

def parse_search(s):
    return s.replace(" ", "%20")

def get_job_data(search_str):
    QUERY = 'https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=b2a11ec2&app_key=dbb7646792780c6c5127eb2bd9f9e15c&results_per_page=25'
    headers = {'Content-Type': 'applications/json',
               'Access-Control-Allow-Origin':'*',
               'Access-Control-Allow-Methods':'GET'}
    
    search_keywords = parse_search(search_str)
    query = '%s&what=%s' % (QUERY, search_keywords)
    req = requests.get(query, headers=headers)
    if req.status_code == 200:
        return json.loads(req.text)['results']
    return {"msg":"search failed!"}

out = get_job_data("blockchain developer solidity")