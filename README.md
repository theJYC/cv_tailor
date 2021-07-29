# cv_tailor

**Technologies: Python (NumPy, pandas), Google Firebase** 

`cv_tailor` is a CLI tool that automates the CV/résumé tailoring process for job applicants submitting individual applications for specialised roles.

*This is a submission for a 24-hour virtual hackathon that took place between 2/27/21 - 2/28/21*

## Inspiration

Almost every successful job applicant goes through the tedious, but necessary, process of rewriting their CV/resume when applying for more than one specific position. 

Coupled with nit-picky Applicant Tracking Softwares (ATS) and the burden of manually reformatting the document, trying to modify one's CV can make a rather taxing experience for the applicant. 

`cv_tailor` hopes to change this. 

With `cv_tailor`'s targeted CV-rendering algorithm that matches certain professions to their inherent skillsets, the jobseeker can automate this age-old process and redirect their time and attention on the things that really matter; allowing them to put their best foot out there and to get ready for the flurry of interviews that will come their way! 


## Contributors
Aaryan Gulia<br>
Jin Young Choi<br>
Obinna Mezu<br>
Pulkit Singh


## Installation

```
sudo pip install firebase-admin
pip install pandas
pip install numpy
```
Once the dependencies are installed, clone the repository to your local machine:
```
git clone git@github.com:jinyoungch0i/cv_tailor.git
```
Within the cloned directory, open `New Terminal at Folder` and run the following command:
```
python main.py
```

For troubleshooting, please ensure that you have the latest version of Python.


## What it does

Using Firebase OAuth for the initial email sign-in, `cv_tailor` guides the user to answer a series of prompts that collect all the content of their current CV in the following the order: 
```
1) basic information 
2) education 
3) work experience 
4) technical projects 
5) extra-curriculars 
```
Once the user completes the form, they will be prompted to select from a list of professions that best matches the position they are applying for. The currently working list consists of: 
```
Software Engineer 
Lawyer 
Medical
Academic Researcher
Accounting and Finance
```
Each of these professions will be matched to a curated list of skills* that may be relevant for the role:

```
1.  creativity.
2.  commercial awareness
3.  interpersonal skills.
4.  critical thinking.
5.  problem solving.
6.  public speaking.
7.  customer service skills.
8.  teamwork skills.
9.  communication.
10. collaboration.
11. accounting.
12. active listening.
13. adaptability.
14. negotiation.
15. conflict resolution.
16. decision-making.
17. empathy.
18. information analysis and research
19. decision making.
20. management.
21. leadership skills.
22. organization.
23. language skills.
24. administrative skills
25. computer programming
```
Once the user indicates the profession they want the CV to be tailoured to, `cv_tailor` algorithm will generate a rewritten version that cherry-picks what is deemed as strictly relevant for the profession and will omit non-relevant content. 

*This `profession : skill` matching is designed on our cloud-hosted database, and allow further additions in order to enhance the scalability. 


## What we learned

Since the majority of our team are first-time hackathoners, the biggest thing we learned is that successful hackathoning requires a lot of strategy.

In fact, here are some of the things we came to agree on: 

### 1) Being more proficient in Git

We initially ran into some technical issues with regards to merging our individual branches to our remote master branch. 

Given this was our first time collaborating realtime with other developers, We learned just how important it is to make sure everyone is comfortable with source/version control in order to make for a smoother workflow. 

### 2) Being sufficiently communicative over roadblocks

Given the virtual nature of the hackathon, and the competing timezones (EST, AST, GMT, and IST) of each member, we had a difficult time remaining fully connected to one another through our designated Discord server, and keeping eachother updated every step of the way. 

We learned that its better to over-communicate than under-communicate, and also to reach out for regular feedback in order to gain objective perspectives on building more efficiently. 


## What's next for cv_tailor

Firstly, we could allow users to directly input additional skills and professions in order to crowdsource a greater diversity of professions and  scale up the code in a way that makes this application relevant to more users. Our code already includes the functionality to continuously check for updates to the skill section of the database.

Secondly, we could integrate a text analysis functionality to analyse description texts and to look for keywords. This will enable a more natural reordering of the `2) education 3) work experience 4) technical projects 5) extra-curriculars` sections in the most logical order. All the libraries we planned to use for text analysis are already imported to the code.

Further, we could add additional features such as location detection (that allows for the algorithm to take into account cultural nuances with CV design); tone and professionality analysis (that offers rephrasing the CV in whichever tone requested by user); chance of job offer (by searching the web for skills required by particular types of employers for particular roles to create a predictive model); and job application services.

Through incorporating the next set of features, `cv_tailor` could accumulate immense data on employment trends, skill sets, employees, job requirements, and secondary findings. There would be no limit as to how we could make use of the large amount of collected data in order to help job applicants further.
