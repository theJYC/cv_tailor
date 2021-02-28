## Members

Aaryan Gulia - Beginner; @Aaryan G#7734
Jin Young Choi - Beginner; @jinyoung#8918
Obinna - Beginner; @Obinna#1175
Pulkit Singh - Beginner; @hydra#6976

## Installation

```
sudo pip install firebase-admin
pip install pandas
pip install numpy
```

Once installed, run:

```
python main.py
```

For troubleshooting, please ensure that you have the latest version of Python.

## Inspiration

Almost everyone goes through a tedious, but necessary, process when applying for a job. 

Conventional wisdom states that one should be ready to do a major overhaul of their CV if its content is not so relevant for the position they are applying for. 

Coupled with nit-picky Applicant Tracking Softwares (ATS) and the burden of manually reformatting the document, trying to modify one's CV can make a rather taxing experience for the applicant. 

`cv_tailor` hopes to change this. 

With `cv_tailor`'s targeted CV-rendering process based on a custom algorithm that matches certain professions to their known desired skillsets, the jobseeker can save both their time and energy on this age-old dilemma and redirect their time and attention on the things that really matter; allowing them to put their best foot out there and to get ready for the flurry of interviews that will come their way! 

## What it does

Using Firebase AuthO for the initial email sign-in, `cv_tailor` guides the user to fill out a command-line form that collects all the content of their current CV following the standardised structure: 1) basic information, 2) education, 3) work experience, 4) technical project experience, and 5) extra-curriculars. 

Once the user completes the form, they will be prompted to select from a list of professions that best matches the position they are applying for. The currently working list is as follows: 

```
Software Engineer 
Lawyer 
Medical
Academic Researcher
Accounting and Finance
```


For each profession on this list*, we have curated a sample set of skills that the internet deemed are relevant and are necessary to demonstrate from the applicant-standpoint. They are identified during our due-dilligence process and are as follows: 

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

Once the user indicates the profession they want the CV to be tailoured to, our algorithm will run and return a no-frills rewrite of their resume, cherry-picking from their original input only the activities that our algorithm deemed as relevant according to the desired skills the profession asks for. 


*Both the list of professions and the desired skills are uploaded to Firebase, and are encoded so that further additions are not only possible but a seamless process. This will ensure that `cv_tailor` is scalable for a greater diversity of professions and skillsets, thereby allowing us to potentially meet the needs of an increasing number of people, and make our software relevant to a larger segment of the job market. 

## How we built it

Our initial architecture consisted of a full-stack, browser-based application with the following components: 

```
Front End: HTML & CSS, JavaScript
Backend: Python (NumPy, pandas), Google Firebase, Flask
```

Having divided the team into an even-split of front-end and back-end, we gradually realised that neither party had enough experience working across the full-stack, and decided that a lot of new information would have to be learned in the condensed timeline of this 24-hour hackathon. This is explained further in the next section. 

8-hours left of the hackathon, we decided to migrate our UI entirely onto the command-line, and made the necessary modifications to ensure a relatively smooth text-based UX. 

With the original full-stack idea and its relevant directories saved within `fullstack/` our revised architecture simply incorporates `Python and Firebase` as the sole technologies used, requiring a more intuitive yet tedious testing process. Nonetheless, we were happy to see that the logic of our program is uncompromised, and that there are no noteworthy errors in terms of the UX. 

## Challenges we ran into

Given that we are a beginner programmer team with no prior experience building a full-stack web application, the biggest challenge took the form of having our front-end and back-end connect with one another.

We researched extensively on the concepts of HTTPS post requests and, while we could have possibly found a 'hack' around this technical insecurity, we decided not to go forward with it given the emphasis on 'learning' and 'applying our knowledge' rather than putting together spaghetti-code that we do not fully understand fundamentally. 

Given our interest to move this project forward beyond the hackathon timeline, we are aware of the technologies we need to have a better understanding of, so that we can make the project more user-friendly and have it serve a wider number of job applicants (many of whom would understandably have a hard time navigating through our installation process). Those technologies are:

```
Front-end: AJAX, HTTP, React, Node.js
Back-end: Flask, Eel
```

## Accomplishments that we're proud of

Within the tight 24-hour deadline, we were proud to accomplish our Minimum Deliverable Product (MVP) despite all the difficulties we faced in connecting different parts of the project and having to completely revamp our UI just 8 hours before submission. 

We're also proud that we did not lose sight of the prototype-mindset; Having established a robust skeleton structure that make our backend scalable, we are excited to have achieved so much and in moving it forward beyond the hackathon. 

After all, we are convinced that `cv_tailor` is much more than a simple hackaton project-- we truly believe that we can change the dynamic of the job application process with our algorithm, if we are given more time to understand the technologies that will enable our fundamental logic. 

Considering that we were a team of beginners, We remain confident that we've put in all the effort we could to provide a deliverable that showcases the core idea of our proposition.


## What we learned

Since the majority of our team are first-time hackathoners, the biggest thing we learned is that successful hackathoning requires a lot of strategy.

In fact, here are some of the things we came to agree on: 


### 1) Being clear about existing individual competencies

We spent a significant amount of time researching new technologies that would have enabled us to make our project full-stack. 

We learned that this was not the best use of the finite time that we were given. 

### 2) Being more proficient in Git

We initially ran into some technical issues with regards to merging our individual branches to our remote origin. 

Given this was our first time collaborating realtime with other developers on an open-source projecet, We learned just how important it is to make sure everyone is comfortable with source/version control in order to make for a smoother workflow. 

### 3) Being sufficiently communicative over roadblocks

Given the virtual nature of the hackathon, and the competing timezones (EST, AST, GMT, and IST) of each member, we had a difficult time remaining fully connected to one another through our designated Discord server, and keep eachother updated every step of the way. 

We learned that its better to over-communicate than under-communicate, and also to reach out for help when needed in order to gain objective guidance on how to build more efficiently. 

## What's next for cv_tailor

`cv_tailor` is a tool with enough potential to disrupt the existing job application process.

Firstly, we will allow for users to directly input new skills and professions to our Firebase, in order to crowdsource a greater diversity of professions and  scale up the code in a way that we open the skills and professions sections for users to update and we can use simple data analysis to categorize these in Firebase. Our code already includes the functionality to continuously check for updates to the skill section of the database. Through this, any kind of job application will be able to use our services (basically, almost any human). 

Second, we were going to add text analysis features to analyse description texts looking for keywords that employers like to place all the experiences, projects, etc, in the right order that would most impress hiring managers. All the libraries we planned to use for this are already imported to the code. However, due to unplanned obstructions, we had to change our focus. 

Further, in the future, we will be adding features like location detection (CVs in different regions of the world would look different); tone and professionality analysis (text analysis to give options of rephrasing CV in whichever tone required by user); success chance (the algorithm can easily search up the web for skills required by particular types of employers for particular roles - we can then create a predictive model to predict the chances of some CVs success; job application services (when we are their favourite place to make CVs, wouldn't it be perfect if they could even submit these to companies through us?

In this process, we will accumulate immense data and employment trends, skill sets, employees, job requirements, and everything else in the industry. There is no limit to how much we can use this data to keep refining our services and eventually be smooth and perfect - a dream for any job applicant.
