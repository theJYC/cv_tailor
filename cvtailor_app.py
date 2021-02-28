import numpy as np
from random import seed
from random import randint

import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

import string



def firestore_upload(db, form_data):
    addition = db.collection('persons').document()
    addition.set({'name': form_data['name'],'email': form_data['email'],'phone_no':form_data['phone_no'],'linkedin profile':form_data['linkedin_profile'],'address':form_data['address']})

    for term in form_data['extra_curriculars']:
        setter = addition.collection('extra_curriculars').document()
        setter.set(term)

    for term in form_data['education']:
        setter = addition.collection('education').document()
        setter.set(term)

    for term in form_data['experience']:
        setter = addition.collection('experience').document()
        setter.set(term)

    for term in form_data['projects']:
        setter = addition.collection('projects').document()
        setter.set(term)



def firebase_get(db, form_data):
    get_data = db.collection('persons').where('email','==',form_data['email']).stream()

    our_dict = list()
    our_list = list()

    for data in get_data:
        our_dict = data.to_dict()
        data_id = data.id

    get_data = db.collection('persons').document(data_id).collection('education').stream()
    for data in get_data:
        our_list.append(data.to_dict())
    our_dict['education'] = our_list
    our_list = list()

    get_data = db.collection('persons').document(data_id).collection('extra_curriculars').stream()
    for data in get_data:
        our_list.append(data.to_dict())
    our_dict['extra_curriculars'] = our_list
    our_list = list()

    get_data = db.collection('persons').document(data_id).collection('experience').stream()
    for data in get_data:
        our_list.append(data.to_dict())
    our_dict['experience'] = our_list
    our_list = list()

    get_data = db.collection('persons').document(data_id).collection('projects').stream()
    for data in get_data:
        our_list.append(data.to_dict())
    our_dict['projects'] = our_list
    our_list = list()

    return our_dict



def proper_data(db, data):
    '''
    input  file
    return python dictionary consisting of json file
    '''
    data = firebase_get(db, form_data)
    profession = input('''
    which profession do you want a CV for, choose from -
    Software Engineer
    Lawyer
    Medical
    Academic Researcher
    Accounting and Finance
    enter one here: ''').lower()

    get_skills = db.collection('Careers').where('name','==',profession).stream()

    for term in get_skills:
        my_list = []
        get_pro_skills = db.collection('Careers').document(term.id).collection('skills').stream()
        for pro_skills in get_pro_skills:
            my_list.append(pro_skills.to_dict()['name'])

    new_data = {}
    new_data['name'] = data['name']
    new_data['email'] = data['email']
    new_data['phone_no'] = data['phone_no']
    new_data['linkedin_profile'] = data['linkedin_profile']
    new_data['extra_curriculars'] = list()
    new_data['experience'] = list()
    new_data['projects'] = list()
    new_data['education'] = list()

    for term in new_data['extra_curriculars']:
        for skill in term['skills']:
            if skill in my_list:
                new_data['extra_curriculars'].append(term)
                break

    for term in data['experience']:
        for skill in term['skills']:
            if skill in my_list:
                new_data['experience'].append(term)
                break

    for term in data['education']:
        for skill in term['skills']:
            if skill in my_list:
                new_data['education'].append(term)
                break

    for term in data['projects']:
        for skill in term['skills']:
            if skill in my_list:
                new_data['projects'].append(term)
                break

    return new_data

def get_form_data():
    print('now you need to fill a form just ones and you can generate a CV for any role you like later!')

    form_data = {}

    form_data['name'] = input('Your name as you want to see it on the resume: ')
    form_data['email'] = input('Your email for the resume: ')
    form_data['linkedin_profile'] = input('Enter the link of your LinkedIn profile: ')
    form_data['phone_no'] = input('Enter your phone number: ')
    form_data['address'] = input ('Enter your address in one line: ')
    form_data['education'] = list()
    form_data['experience'] = list()
    form_data['extra_curriculars'] = list()
    form_data['projects'] = list()

    while True:
        education = {}
        if input('do you want to add more education(y/n): ').lower() == 'y':
            education['organization'] = input('name of organization: ')
            education['name_of_course'] = input('name of your course: ')
            education['qualification'] = input('the qualification you have or will recieve: ')
            education['date_completed'] = input('date completed or will complete: ')
            education['grade'] = input('grade recieved: ')
            education['skills'] = input('''
enter the skills you gained. Only choose and copy exactly from the list below:
1.	Creativity.
2.	Commercial awareness
3.	Interpersonal Skills.
4.	Critical Thinking.
5.	Problem Solving.
6.	Public Speaking.
7.	Customer Service Skills.
8.	Teamwork Skills.
9.	Communication.
10.	Collaboration.
11.	Accounting.
12.	Active Listening.
13.	Adaptability.
14.	Negotiation.
15.	Conflict Resolution.
16.	Decision-making.
17.	Empathy.
18.	Information analysis and research
19.	Decision Making.
20.	Management.
21.	Leadership skills.
22.	Organization.
23.	Language skills.
24.	Administrative skills
25.	Computer programming

Do not enter numbers, dots, or symbols and make sure you seperate each with a comma!
enter here:
                                        ''').lower().split(',')
            form_data['education'].append(education)
        else:
            break

    while True:
        experience = {}
        if input('do you want to add more experiance(y/n): ').lower() == 'y':
            experience['organization'] = input('name of organization: ')
            experience['name_of_role'] = input('name of your role: ')
            experience['date_start'] = input('date you started working here: ')
            experience['date_finish'] = input('date you stopped working here: ')
            experience['description'] = input('Describe your experiance breifly: ')
            experience['skills'] = input('''
enter the skills you gained. Only choose and copy exactly from the list below:
1.	Creativity.
2.	Commercial awareness
3.	Interpersonal Skills.
4.	Critical Thinking.
5.	Problem Solving.
6.	Public Speaking.
7.	Customer Service Skills.
8.	Teamwork Skills.
9.	Communication.
10.	Collaboration.
11.	Accounting.
12.	Active Listening.
13.	Adaptability.
14.	Negotiation.
15.	Conflict Resolution.
16.	Decision-making.
17.	Empathy.
18.	Information analysis and research
19.	Decision Making.
20.	Management.
21.	Leadership skills.
22.	Organization.
23.	Language skills.
24.	Administrative skills
25.	Computer programming

Do not enter numbers, dots, or symbols and make sure you seperate each with a comma!
enter here:
                                        ''').lower().split(',')
            form_data['experience'].append(experience)
        else:
            break

    while True:
        extra_curriculars = {}
        if input('do you want to add more extra curriculars(y/n): ').lower() == 'y':
            extra_curriculars['organization'] = input('name of organization: ')
            extra_curriculars['name'] = input('name of your activity: ')
            extra_curriculars['description'] = input('Describe your extra curricular breifly: ')
            extra_curriculars['skills'] = input('''
enter the skills you gained. Only choose and copy exactly from the list below:
1.	Creativity.
2.	Commercial awareness
3.	Interpersonal Skills.
4.	Critical Thinking.
5.	Problem Solving.
6.	Public Speaking.
7.	Customer Service Skills.
8.	Teamwork Skills.
9.	Communication.
10.	Collaboration.
11.	Accounting.
12.	Active Listening.
13.	Adaptability.
14.	Negotiation.
15.	Conflict Resolution.
16.	Decision-making.
17.	Empathy.
18.	Information analysis and research
19.	Decision Making.
20.	Management.
21.	Leadership skills.
22.	Organization.
23.	Language skills.
24.	Administrative skills
25.	Computer programming

Do not enter numbers, dots, or symbols and make sure you seperate each with a comma!
enter here:
                                        ''').lower().split(',')
            form_data['extra_curriculars'].append(extra_curriculars)
        else:
            break


    while True:
        project = {}
        if input('do you want to add more projects(y/n): ').lower() == 'y':
            project['name_of_project'] = input('name of your project: ')
            project['description'] = input('Describe your project breifly: ')
            project['skills'] = input('''
enter the skills you gained. Only choose and copy exactly from the list below:
1.	Creativity.
2.	Commercial awareness
3.	Interpersonal Skills.
4.	Critical Thinking.
5.	Problem Solving.
6.	Public Speaking.
7.	Customer Service Skills.
8.	Teamwork Skills.
9.	Communication.
10.	Collaboration.
11.	Accounting.
12.	Active Listening.
13.	Adaptability.
14.	Negotiation.
15.	Conflict Resolution.
16.	Decision-making.
17.	Empathy.
18.	Information analysis and research
19.	Decision Making.
20.	Management.
21.	Leadership skills.
22.	Organization.
23.	Language skills.
24.	Administrative skills
25.	Computer programming

Do not enter numbers, dots, or symbols and make sure you seperate each with a comma!
enter here:
                                        ''').lower().split(',')
            form_data['projects'].append(project)
        else:
            break
    return form_data
