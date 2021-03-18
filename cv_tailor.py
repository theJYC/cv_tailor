import numpy as np
import pandas as pd

import firebase_admin
from firebase_admin import credentials, firestore

from cv_generate import linebreak

import string


def firestore_upload(db, form_data):
    addition = db.collection('persons').document()
    addition.set({'name': form_data['name'], 'email': form_data['email'], 'phone_no': form_data['phone_no'],
                  'linkedin profile': form_data['linkedin_profile'], 'address': form_data['address']})

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
    get_data = db.collection('persons').where(
        'email', '==', form_data['email']).stream()

    our_dict = list()
    our_list = list()

    for data in get_data:
        our_dict = data.to_dict()
        data_id = data.id

    get_data = db.collection('persons').document(
        data_id).collection('education').stream()
    for data in get_data:
        our_list.append(data.to_dict())
    our_dict['education'] = our_list
    our_list = list()

    get_data = db.collection('persons').document(
        data_id).collection('extra_curriculars').stream()
    for data in get_data:
        our_list.append(data.to_dict())
    our_dict['extra_curriculars'] = our_list
    our_list = list()

    get_data = db.collection('persons').document(
        data_id).collection('experience').stream()
    for data in get_data:
        our_list.append(data.to_dict())
    our_dict['experience'] = our_list
    our_list = list()

    get_data = db.collection('persons').document(
        data_id).collection('projects').stream()
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
    profession = input('''
    Which profession would you like your CV/résumé to be tailored to? Choose from -
    Software Engineer
    Lawyer
    Medical
    Academic Researcher
    Accounting and Finance
    enter one here: ''').lower()

    get_skills = db.collection('Careers').where(
        'name', '==', profession).stream()

    for term in get_skills:
        my_list = []
        get_pro_skills = db.collection('Careers').document(
            term.id).collection('skills').stream()
        for pro_skills in get_pro_skills:
            my_list.append(pro_skills.to_dict()['name'])

    new_data = {}
    new_data['name'] = data['name']
    new_data['email'] = data['email']
    new_data['phone_no'] = data['phone_no']
    new_data['linkedin profile'] = data['linkedin profile']
    new_data['address'] = data['address']
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
    print('Great! Fill out the following form to your best ability, and cv_tailor will generate a custom cv/résumé for any specific role you wish to apply for.')

    form_data = {}

    form_data['name'] = input(
        'Full Name: ')
    form_data['email'] = input('Email: ')
    form_data['linkedin_profile'] = input(
        'LinkedIn Profile URL: ')
    form_data['phone_no'] = input('Phone Number: ')
    form_data['address'] = input('Address: ')
    form_data['education'] = list()
    form_data['experience'] = list()
    form_data['extra_curriculars'] = list()
    form_data['projects'] = list()
    linebreak()

    while True:
        education = {}
        if input('Would you like to add Education (y/n)?: ').lower() == 'y':
            education['organization'] = input('School Name: ')
            education['name_of_course'] = input('Major(s): ')
            education['qualification'] = input(
                'Degree Type: ')
            education['date_completed'] = input(
                'Graduation Year: ')
            education['grade'] = input('Grade: ')
            education['skills'] = input('''
Enter the skills you gained. Only choose and copy exactly from the list below:
1.  Creativity.
2.  Commercial Awareness
3.  Interpersonal Skills.
4.  Critical Thinking.
5.  Problem Solving.
6.  Public Speaking.
7.  Customer Service Skills.
8.  Teamwork Skills.
9.  Communication.
10. Collaboration.
11. Accounting.
12. Active Listening.
13. Adaptability.
14. Negotiation.
15. Conflict Resolution.
16. Decision-making.
17. Empathy.
18. Information Analysis and Research
19. Decision Making.
20. Management.
21. Leadership Skills.
22. Organization.
23. Language Skills.
24. Administrative Skills
25. Computer Programming

Do not enter numbers, dots, or symbols and make sure you seperate each with a comma(,)!
Enter here:
                                        ''').lower().split(',')
            form_data['education'].append(education)
            linebreak()
        else:
            break

    while True:
        experience = {}
        if input('Would you like to add Professional Experience (y/n)?: ').lower() == 'y':
            experience['organization'] = input('Company/Organisation: ')
            experience['name_of_role'] = input('Position: ')
            experience['date_start'] = input('Start date: ')
            experience['date_finish'] = input(
                'End date: ')
            experience['description'] = input(
                'One or two line description of your responsibilities: ')
            experience['skills'] = input('''
Enter the skills you gained. Only choose and copy exactly from the list below:
1.  Creativity.
2.  Commercial awareness
3.  Interpersonal Skills.
4.  Critical Thinking.
5.  Problem Solving.
6.  Public Speaking.
7.  Customer Service Skills.
8.  Teamwork Skills.
9.  Communication.
10. Collaboration.
11. Accounting.
12. Active Listening.
13. Adaptability.
14. Negotiation.
15. Conflict Resolution.
16. Decision-making.
17. Empathy.
18. Information Analysis and Research
19. Decision Making.
20. Management.
21. Leadership Skills.
22. Organization.
23. Language Skills.
24. Administrative Skills
25. Computer Programming

Do not enter numbers, dots, or symbols and make sure you seperate each with a comma(y)!
Enter here:
                                        ''').lower().split(',')
            form_data['experience'].append(experience)
            linebreak()
        else:
            break

    while True:
        extra_curriculars = {}
        if input('Would you like to add Extra Curriculars (y/n)?: ').lower() == 'y':
            extra_curriculars['organization'] = input('Organisation/Group: ')
            extra_curriculars['name'] = input('Position: ')
            extra_curriculars['description'] = input(
                'One or two line description of your responsibilities: ')
            extra_curriculars['skills'] = input('''
Enter the skills you gained. Only choose and copy exactly from the list below:
1.  Creativity.
2.  Commercial Awareness
3.  Interpersonal Skills.
4.  Critical Thinking.
5.  Problem Solving.
6.  Public Speaking.
7.  Customer Service Skills.
8.  Teamwork Skills.
9.  Communication.
10. Collaboration.
11. Accounting.
12. Active Listening.
13. Adaptability.
14. Negotiation.
15. Conflict Resolution.
16. Decision-making.
17. Empathy.
18. Information Analysis and Research
19. Decision Making.
20. Management.
21. Leadership Skills.
22. Organization.
23. Language Skills.
24. Administrative Skills
25. Computer Programming

Do not enter numbers, dots, or symbols and make sure you seperate each with a comma!
Enter here:
                                        ''').lower().split(',')
            form_data['extra_curriculars'].append(extra_curriculars)
            linebreak()
        else:
            break

    while True:
        project = {}
        if input('Would you like to add Project Experience (y/n)?: ').lower() == 'y':
            project['name_of_project'] = input('Project Name: ')
            project['description'] = input('One or two line description of your Project: ')
            project['skills'] = input('''
Enter the skills you gained. Only choose and copy exactly from the list below:
1.  Creativity.
2.  Commercial Awareness
3.  Interpersonal Skills.
4.  Critical Thinking.
5.  Problem Solving.
6.  Public Speaking.
7.  Customer Service Skills.
8.  Teamwork Skills.
9.  Communication.
10. Collaboration.
11. Accounting.
12. Active Listening.
13. Adaptability.
14. Negotiation.
15. Conflict Resolution.
16. Decision-making.
17. Empathy.
18. Information Analysis and Research
19. Decision Making.
20. Management.
21. Leadership Skills.
22. Organization.
23. Language Skills.
24. Administrative Skills
25. Computer Programming

Do not enter numbers, dots, or symbols and make sure you seperate each with a comma(,)!
Enter here:
                                        ''').lower().split(',')
            form_data['projects'].append(project)
            linebreak()
        else:
            break
    return form_data
