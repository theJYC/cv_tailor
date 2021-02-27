import numpy as np
from random import seed
from random import randint

import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

import string

import firebase_admin
from firebase_admin import credentials
cred = credentials.Certificate("cv-tailor-2021-firebase-adminsdk-fksao-29fb361d14.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#def get_form_data():



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



def proper_data(db, data, profession):
    '''
    input  file
    return python dictionary consisting of json file
    '''

    get_skills = db.collection('Careers').where('name','==',profession).stream()

    for term in get_skills:
        my_list = []
        get_pro_skills = db.collection('Careers').document(term.id).collection('skills').stream()
        for pro_skills in get_pro_skills:
            my_list.append(pro_skills.to_dict()['name'])

    new_data = {}
    new_data['name'] = data.get('name')
    new_data['email'] = data.get('email')
    new_data['phone_no'] = data.get('phone_no')
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

if __name__ == '__main__':
    print('hi, this is a revolutionary cv building idea which can disrupt existing apps if given sufficient time to develop')

if input('have you filled in the cv building form before?(y/n) ').lower() == 'y':
    email = input('enter your email: ')
    get_data = db.collection('persons').where('email','==',email.lower().split())

    if len(get_data.get()) == 0:
        form_data = {'email': email}
    else:
        print('the email you entered is not known')

    our_dict = firebase_get(db, form_data)
    profession = input('''
                       which profession do you want a CV for, choose from -
                       Software Engineer
                       Lawyer
                       Medical
                       Academic Researcher
                       Accounting and Finanance
                       enter one here:
                       ''').lower()
    new_dict = proper_data(db, our_dict, profession)
