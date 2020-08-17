# Django Simple Rest Api Project

## Setup

### Project Clone

- `git clone git@github.com:Kadermiyanyedi/PriviaSecurityInternshipChallenge.git`
- `cd PriviaSecurityInternshipChallenge`
---
### Create a virtual environment to isolate our package dependencies locally

1. Create venv
`python -m venv env`

2. Activate venv
- On Linux use :
    `source env/bin/activate`

- On Windows use :
    `env\Scripts\activate`
---
### Install Django and Django REST framework into the virtual environment
- `pip install -r requirements.txt`

### Migrate Database
- `cd blog`
- `python manage.py migrate`

### Admin Panel and Login Page
username : admin
password: admin

If you want create a new super user : 
`python manage.py createsuperuser --email admin@example.com --username admin`

### Start Server
`python manage.py runserver`

Go to localhost:8000 in your browser

### Run Test
`python manage.py test api`