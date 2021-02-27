

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import json
import sqlite3
from flask import Flask, jsonify, g, redirect, request, url_for

def data_generator():
    '''
    input json file
    return python dictionary consisting of json file
    '''
    app = Flask(__name__)

    @app.before_request
    def before_request():
        g.db = sqlite3.connect('database.db')

    @app.teardown_request
    def teardown_request(exception):
        if hasattr(g, 'db'):
            g.db.close()

    @app.route('/')
    def index():
        return redirect(url_for('static', filename='page.html'))

    @app.route('/json-data/')
    def json_data():
        # get number of items from the javascript request
        nitems = request.args.get('nitems', 2)
        # query database
        cursor = g.db.execute('select * from items limit ?', (nitems,))
        # return json
        return jsonify(dict(('item%d' % i, item)
                            for i, item in enumerate(cursor.fetchall(), start=1)))

    if __name__ == '__main__':
        app.run(debug=True, host='localhost', port=5001)  # http://localhost:5001/
    r = requests.get('https://json.org/example.html')
    print(dir(r.json))
    with open('cvtailor.json') as f:
        data = json.load(f)
    return (data)

practice_data = { 'name':'Obinna', 'email':'Mezu', 'Phone_no':'l04849494', 'linkedin_profile':'o.mezu', 'address':'78 Sir',
'extra_curriculars': [{'name':'', 'organization':'', 'description':'', 'skills': ('communication')}],
'education': [{'organization':'', 'name_of_course':'', 'qualification':'', 'date_completed':'', 'grade':'', 'skills': ('teamwork skills')}],
'experience': [{'organization':'', 'name_of_role':'', 'date_start':'', 'date_finish':'', 'description':'', 'skills': ('problem solving')}],
'projects': [{'name_of_project':'', 'description':'', 'skills': ('accounting') }]}

print(practice_data['extra_curriculars'][0]['skills'])

software_engineer = ['communication', 'teamwork skills', 'problem solving', 'information analysis and research', 'management', 'critical thinking', 'creativity', 'computer programming', 'collaboration']
lawyer = ['language skills', 'commercial awareness', 'teamwork skills', 'problem solving', 'communication', 'negotiation', 'conflict resolution', 'organization', 'decision making', 'customer service skills']
medical = ['problem solving', 'collaboration', 'empathy', 'organization', 'critical thinking', 'leadership skills', 'decision making']
academic_research = ['accounting', 'critical thinking', 'information analysis and research', 'administrative skills', 'active listening', 'management', 'leadership skills', 'collaboration']
accounting_finance = ['accounting', 'organization', 'critical thinking', 'interpersonal skills', 'commercial awareness', 'collaboration', 'communication', 'problem solving', 'adaptability', 'administrative skills']

def proper_data(data, profession):
    '''
    input  file
    return python dictionary consisting of json file
    '''

    new_data = {}
    new_data['name'] = data.get('name')
    new_data['email'] = data.get('email')
    new_data['Phone_no'] = data.get('Phone_no')
    for skills in data.get('extra_curriculars').get('skills'):
        if skills in profession:
            new_data['extra_curriculars'] = data.get('extra_curriculars')
    for skills in data.get('education').get('skills'):
        if skills in profession:
            new_data['education'] = data.get('education')
    for skills in data.get('experience').get('skills'):
        if skills in profession:
            new_data['experience'] = data.get('experience')
    for skills in data.get('projects').get('skills'):
        if skills in profession:
            new_data['projects'] = data.get('projects')

    return new_data



