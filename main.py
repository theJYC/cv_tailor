from cvtailor_app import firestore_upload, firebase_get, proper_data, get_form_data
from cv_create import cv_tailor

import firebase_admin
from firebase_admin import credentials, firestore

if __name__ == '__main__':

    cred = credentials.Certificate("cv-tailor-2021-firebase-adminsdk-fksao-29fb361d14.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

while True:
    print('hi, this is a revolutionary cv building idea which can disrupt existing apps if given sufficient time to develop')

    while True:
        if input('have you filled in the cv building form before?(y/n) ').lower() == 'y':
            email = input('enter your email: ')
            get_data = db.collection('persons').where('email','==',email.lower())

            if len(get_data.get()) > 0:
                form_data = {'email': email}
                form_data = firebase_get(db,form_data)
                break
            else:
                print('the email you entered is not known, please enter n next')

        else:
            form_data = get_form_data()
            firestore_upload(db, form_data)
            form_data = firebase_get(db, form_data)
            break

    new_dict = proper_data(db, form_data)

    print('your smart CV for the role is: ')
    cv_tailor(new_dict)

    print('your normal CV is: ')
    cv_tailor(form_data)

    if input('do you want to re-run the application?(yes/no): ').lower() == 'yes':
        continue
    break
