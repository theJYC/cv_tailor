def linebreak():
    print("          ")
    print("          ")


def cv_tailor(fd):
    linebreak()

    print(f"Basic Information_")
    print("______________________________________________________________________________________________________")

    linebreak()

    print(f"Name:        {fd['name']}")
    print(f"Email:       {fd['email']}")
    print(f"Phone:       {fd['phone_no']}")
    print(f"LinkedIn:    {fd['linkedin profile']}")
    print(f"Address:     {fd['address']}")

    linebreak()

    print(f"Education_")
    print("______________________________________________________________________________________________________")

    linebreak()
    skills = []

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

    linebreak()
