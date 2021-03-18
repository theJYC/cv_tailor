from cv_tailor import firestore_upload, firebase_get, proper_data, get_form_data
from cv_generate import cv_tailor

import firebase_admin
from firebase_admin import credentials, firestore

if __name__ == '__main__':

    cred = credentials.Certificate(
        "cv-tailor-2021-firebase-adminsdk-fksao-29fb361d14.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

while True:
    print('Hi there! cv_tailor is an open source CLI tool that renders a highly tailored CV/resume for a more targeted job application.')

    while True:
        if input('Have you filled out the cv_tailor form before (y/n)?: ').lower() == 'y':
            email = input('Please enter the email you used previously: ')
            get_data = db.collection('persons').where(
                'email', '==', email.lower())

            if len(get_data.get()) > 0:
                form_data = {'email': email}
                form_data = firebase_get(db, form_data)
                break
            else:
                print('The email you entered is not recognised. Please continue by pressing <enter>.')

        else:
            form_data = get_form_data()
            firestore_upload(db, form_data)
            form_data = firebase_get(db, form_data)
            break

    new_dict = proper_data(db, form_data)

    print('Your tailored CV/résumé for the role is: ')
    cv_tailor(new_dict)

    print('your general CV/résumé is: ')
    cv_tailor(form_data)

    if input('Would you like to re-run the application (yes/no)?: ').lower() == 'yes':
        continue
    break
