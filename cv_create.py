form_data = {'name': 'Aaryan Gulia', 'email': 'aaryan.gulia@gmail.com', 'phone_no': '+974 55994789', 'linkedin_profile': 'https://www.linkedin.com/in/aaryan-gulia/', 'address': 'Doha, Qatar',
             'extra_curriculars': [{'name': 'Guitar', 'organization': 'At Home', 'description': 'I have started playing guitar since the tender age of 5', 'skills': ['creativity']}],
             'education': [{'organization': 'University College London', 'name_of_course': 'Theoretical Physics', 'qualification': 'MSci', 'date_completed': '2024', 'grade': '1st class', 'skills': ['teamwork skills', 'critical thinking']}],
             'experience': [{'organization': 'PPLPWR', 'name_of_role': 'Project Lead', 'date_start': '2020', 'date_finish': '2025', 'description': 'I love it', 'skills': ['problem solving', 'teamwork skills', 'organization', 'leaderships skills']}],
             'projects': [{'name_of_project': 'CVTailor', 'description': 'Kidding me!', 'skills': ['computer programming']}]}

# print(form_data["extra_curriculars"][0]["name"])

fd = form_data


def linebreak():
    print("          ")
    print("          ")


def cv_tailor():
    linebreak()
    print(f"Here is your tailoured CV, {form_data['name']}:")

    linebreak()
    linebreak()

    print(f"Basic Information_")
    print("______________________________________________________________________________________________________")

    linebreak()

    print(f"Name:        {fd['name']}")
    print(f"Email:       {fd['email']}")
    print(f"Phone:       {fd['phone_no']}")
    print(f"LinkedIn:    {fd['linkedin_profile']}")
    print(f"Address:     {fd['address']}")

    linebreak()

    print(f"Education_")
    print("______________________________________________________________________________________________________")

    linebreak()

    education = fd['education']

    for edu in education:
        print(f"School:      {edu['organization']}")
        print(f"Study Area:  {edu['name_of_course']}")
        print(f"Degree:      {edu['qualification']}")
        print(f"Graduation:  {edu['date_completed']}")
        print(f"Grade:       {edu['grade']}")

    string = "Skills:      "
    skills = edu['skills']
    for skill in skills:
        string += skill + ", "

    print(string[:-2])

    linebreak()

    print(f"Work_Experience_")
    print("______________________________________________________________________________________________________")

    linebreak()

    experience = fd['experience']

    for exp in experience:
        print(f"Company/Org: {exp['organization']}")
        print(f"Position:    {exp['name_of_role']}")
        print(f"Start Year:  {exp['date_start']}")
        print(f"End Year:    {exp['date_finish']}")
        print(f"Summary:     {exp['description']}")

    string = "Skills:      "
    skills = exp['skills']
    for skill in skills:
        string += skill + ", "

    print(string[:-2])
    linebreak()

    print(f"Technical_Projects_")
    print("______________________________________________________________________________________________________")

    linebreak()

    projects = fd['projects']

    for project in projects:
        print(f"Company/Org: {project['name_of_project']}")
        print(f"Position:    {project['description']}")

    string = "Skills:      "
    skills = project['skills']
    for skill in skills:
        string += skill + ", "

    print(string[:-2])
    linebreak()

    print(f"Extra-Curriculars_")
    print("______________________________________________________________________________________________________")
    linebreak()

    extra_curriculars = fd['extra_curriculars']

    for ec in extra_curriculars:
        print(f"Activity:    {ec['name']}")
        print(f"Company/Org: {ec['organization']}")

        print(f"Summary:     {ec['description']}")

    string = "Skills:      "
    skills = ec['skills']
    for skill in skills:
        string += skill + ", "

    print(string[:-2])
    linebreak()
