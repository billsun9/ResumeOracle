# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 14:10:13 2022

@author: Bill Sun
"""
import requests
import json

def parse_search(s):
    return s.replace(" ", "%20")

def get_job_data(search_str):
    QUERY = 'https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=b2a11ec2&app_key=dbb7646792780c6c5127eb2bd9f9e15c&results_per_page=10'
    headers = {'Content-Type': 'applications/json',
               'Access-Control-Allow-Origin':'*',
               'Access-Control-Allow-Methods':'GET'}
    
    search_keywords = parse_search(search_str)
    query = '%s&what=%s' % (QUERY, search_keywords)
    req = requests.get(query, headers=headers)
    if req.status_code == 200:
        res = []
        for item in json.loads(req.text)['results']:
            res.append({'company':item['company']['display_name'], 
                        'description':item['description'], 
                        'title':item['title'],
                        'link':item['redirect_url']})
        return res
    return ["FAILED!"]